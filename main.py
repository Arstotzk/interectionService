from flask import Flask, jsonify
from db_connect import DBConnect
from rabbit import Rabbit

app = Flask(__name__)


@app.route('/info', methods=['GET'])
def get_info():
    return 'info'


@app.route('/users', methods=['GET'])
def get_users():
    connect = DBConnect()
    result = connect.ExecuteQuery('SELECT * FROM users')
    connect.Close()
    return result


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
    rabbit = Rabbit()
    rabbit.PutImage()
    return 'run'


@app.route('/find/cephalometric', methods=['POST'])
def post_find_cephalometric():
    return 'image_info'


if __name__ == '__main__':
    app.run(debug=True)
