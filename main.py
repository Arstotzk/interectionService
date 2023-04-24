from uuid import uuid4

from flask import Flask, jsonify, request, abort
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
    name = request.form.get("name")
    idDevice = request.form.get("idDevice")
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

@app.route('/image/points', methods=['GET'])
def get_image_points():
    connect = DBConnect()
    result = connect.ExecuteQuery('SELECT * FROM points')
    connect.Close()
    return result


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
        result = connect.ExecuteInsertQuery('INSERT INTO public.images ("Guid", image_path, "user", "datetime", "status")'
                                            'VALUES (\''+uuid.__str__()+'\', \''+path+'\', \''+userUuid+'\', '
                                            'current_timestamp, \'processing\') '
                                            'RETURNING \'Новая запись добавлена.\';')
        connect.Close()
        rabbit = Rabbit()
        rabbit.PutImage(uuid.__str__())
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
        result = connect.ExecuteInsertQuery('INSERT INTO public.users("idDevice", name) '
                                            'VALUES (\''+idDevice+'\', \''+name+'\') '
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
