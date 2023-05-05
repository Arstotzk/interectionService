from io import BytesIO
from uuid import uuid4

from flask import Flask, jsonify, request, abort, send_file
from db_connect import DBConnect
from rabbit import Rabbit
from datetime import datetime
import storage

app = Flask(__name__)

print(datetime.now())

@app.route('/', methods=['GET'])
@app.route('/info', methods=['GET'])
def get_info():
    return 'info'


@app.route('/users', methods=['GET'])
def get_users():
    connect = DBConnect()
    result = connect.ExecuteQuery('SELECT * FROM users')
    connect.Close()
    return result

@app.route('/image/all', methods=['GET'])
def get_image_all():
    name = request.args.get("name")
    idDevice = request.args.get("idDevice")
    if name is not None and idDevice is not None:
        connect = DBConnect()
        result = connect.ExecuteQuery(
            'SELECT "Guid" FROM users WHERE "idDevice" = \'' + idDevice + '\' AND name = \'' + name + '\'')
        userUuid = result[0][0]
        print(userUuid)
        result = connect.ExecuteQuery('SELECT "Guid", image_path, "user", datetime, status FROM public.images WHERE "user" = \''+ userUuid +'\';')
        connect.Close()
        print(result)
        return result
    abort(500)
    return ""

@app.route('/image', methods=['GET'])
def get_image():
    name = request.args.get("name")
    idDevice = request.args.get("idDevice")
    imageGuid = request.args.get("imageGuid")
    if name is not None and idDevice is not None:
        connect = DBConnect()
        result = connect.ExecuteQuery(
            'SELECT "Guid" FROM users WHERE "idDevice" = \'' + idDevice + '\' AND name = \'' + name + '\'')
        userUuid = result[0][0]
        print(userUuid)
        result = connect.ExecuteQuery('SELECT "Guid", image_path, "user", datetime, status FROM public.images WHERE "Guid" = \''+ imageGuid +'\';')
        connect.Close()
        path = result[0][1] + "\\" + result[0][0]
        with open(path, "rb") as fh:
            file = BytesIO(fh.read())
        print(result)
        return send_file(file, mimetype='image/png')
    abort(500)
    return ""

@app.route('/image/points', methods=['GET'])
def get_image_points():
    name = request.args.get("name")
    idDevice = request.args.get("idDevice")
    imageGuid = request.args.get("imageGuid")
    if name is not None and idDevice is not None:
        connect = DBConnect()
        result = connect.ExecuteQuery(
            'SELECT "Guid" FROM users WHERE "idDevice" = \'' + idDevice + '\' AND name = \'' + name + '\'')
        userUuid = result[0][0]
        print(userUuid)
        result = connect.ExecuteQuery('SELECT x, y, "name", image, "Guid" FROM public.points as p '
                                      'join public.point_types as pt on p.point_type = pt."Guid"'
                                      'WHERE image = \''+ imageGuid +'\';')
        connect.Close()
        return result
    return ""


@app.route('/image/lines', methods=['GET'])
def get_image_lines():
    connect = DBConnect()
    result = connect.ExecuteQuery('SELECT * FROM lines')
    connect.Close()
    return result


@app.route('/image/params', methods=['GET'])
def get_image_params():
    connect = DBConnect()
    result = connect.ExecuteQuery('SELECT * FROM params')
    connect.Close()
    return result


@app.route('/image/point_types', methods=['GET'])
def get_image_point_types():
    connect = DBConnect()
    result = connect.ExecuteQuery('SELECT * FROM point_types')
    connect.Close()
    return result


@app.route('/image/line_types', methods=['GET'])
def get_image_line_types():
    connect = DBConnect()
    result = connect.ExecuteQuery('SELECT * FROM line_types')
    connect.Close()
    return result


@app.route('/image/param_types', methods=['GET'])
def get_image_param_types():
    connect = DBConnect()
    result = connect.ExecuteQuery('SELECT * FROM param_types')
    connect.Close()
    return result

@app.route('/image/point/coordinate', methods=['POST'])
def post_image_point_coordinate():
    name = request.form.get("name")
    idDevice = request.form.get("idDevice")
    pointGuid = request.form.get("pointGuid")
    x = request.form.get("x")
    y = request.form.get("y")
    if name is not None and idDevice is not None:
        connect = DBConnect()
        result = connect.ExecuteQuery(
            'SELECT "Guid" FROM users WHERE "idDevice" = \'' + idDevice + '\' AND name = \'' + name + '\'')
        userUuid = result[0][0]
        print(userUuid)
        result = connect.ExecuteChangeDataQuery('UPDATE public.points '
                                      'SET x=' + x + ', y=' + y + ' '
                                      'WHERE "Guid"= \'' + pointGuid +'\''
                                      'RETURNING \'Координата точки обновлена.\';')
        connect.Close()
        return result
    return ""

@app.route('/find/points', methods=['POST'])
def post_find_points():
    print(request.args)
    print(request.form)
    print(request.files)
    name = request.form.get("name")
    idDevice = request.form.get("idDevice")
    image_file = request.files.get("imageFile")
    if image_file is not None:
        uuid = uuid4()
        path = storage.SaveFile(image_file, uuid.__str__())
        connect = DBConnect()
        result = connect.ExecuteQuery(
            'SELECT "Guid" FROM users WHERE "idDevice" = \'' + idDevice + '\' AND name = \'' + name + '\'')
        userUuid = result[0][0]
        result = connect.ExecuteChangeDataQuery('INSERT INTO public.images ("Guid", image_path, "user", "datetime", "status")'
                                            'VALUES (\'' + uuid.__str__() +'\', \'' + path +'\', \'' + userUuid +'\', '
                                            'current_timestamp, \'processing\') '
                                            'RETURNING \'Новая запись добавлена.\';')
        connect.Close()
        rabbit = Rabbit()
        rabbit.PutImage(uuid.__str__())
        return 'complete'
    return "error"

@app.route('/find/params', methods=['POST'])
def post_find_params():
    print(request.args)
    print(request.form)
    print(request.files)
    name = request.form.get("name")
    idDevice = request.form.get("idDevice")
    imageGuid = request.form.get("imageGuid")
    if imageGuid is not None:
        connect = DBConnect()
        result = connect.ExecuteQuery(
            'SELECT "Guid" FROM users WHERE "idDevice" = \'' + idDevice + '\' AND name = \'' + name + '\'')
        userUuid = result[0][0]

        connect.Close()
        rabbit = Rabbit()
        rabbit.FindParams(imageGuid)
        return 'complete'
    return "error"

@app.route('/user/new', methods=['POST'])
def post_user_new():
    print(request.args)
    print(request.form)
    print(request.files)
    name = request.form.get("name")
    idDevice = request.form.get("idDevice")
    if name is not None and idDevice is not None:
        connect = DBConnect()
        result = connect.ExecuteChangeDataQuery('INSERT INTO public.users("idDevice", name) '
                                            'VALUES (\'' + idDevice +'\', \'' + name +'\') '
                                            'RETURNING \'Новый пользователь создан.\';')
        connect.Close()
        return result
    abort(500)
    return ""

@app.route('/user', methods=['GET'])
def get_user():
    print(request.args)
    print(request.form)
    print(request.files)
    name = request.args.get("name")
    idDevice = request.args.get("idDevice")
    if name is not None and idDevice is not None:
        connect = DBConnect()
        result = connect.ExecuteQuery(
            'SELECT * FROM users WHERE "idDevice" = \''+idDevice+'\' AND name = \''+name+'\'')
        connect.Close()
        if len(result) != 0:
            data = {'isUserExist': True}
            print(data)
            return jsonify(data)
        else:
            data = {'isUserExist': False,
                    'error': 'That name and device not registered'}
            print(data)
            return jsonify(data)
    data = {'isUserExist': False,
            'error': 'Name or device cannot be empty'}
    print(data)
    return jsonify(data)

@app.route('/find/cephalometric', methods=['POST'])
def post_find_cephalometric():
    return 'image_info'


if __name__ == '__main__':
    app.run(host='192.168.31.168', port=5000, debug=True, threaded=False)
