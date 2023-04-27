from flask import Flask, request
from mysql import connector

from registration import user_registration, user_remove, user_accounts
from account import account_create, account_delete

from conn import dbconfig
app = Flask(__name__)
app.config['MYSQL_USER'] = dbconfig['user']
app.config['MYSQL_PASSWORD'] = dbconfig['password']

cnx = connector.connect(user=dbconfig['user'],
                        password=dbconfig['password'],
                        host=dbconfig['host'],
                        database=dbconfig['database'])


@app.route('/')
def index():
    if cnx.is_connected():
        msg = "Connected"
    else:
        msg = "Not connected"
    return '<h1>' + msg + '</h1>'


@app.route('/user/<name>')
def user(name):
    return 'hi, %s' % name


@app.route('/api/user/register', methods=['POST'])
def u_register():
    request_data = request.get_json()
    result = user_registration(request_data)
    return result


@app.route('/api/user/delete', methods=['POST'])
def u_delete():
    request_data = request.get_json()
    result = user_remove(request_data)
    return result


@app.route('/api/user/get_accounts', methods=['GET'])
def u_accounts():
    request_data = request.get_json()
    result = user_accounts(request_data)
    return result


@app.route('/api/account/create', methods=['POST'])
def acc_create():
    request_data = request.get_json()
    result = account_create(request_data)
    return result


@app.route('/api/account/delete', methods=['POST'])
def acc_delete():
    request_data = request.get_json()
    result = account_delete(request_data)
    return result


if __name__ == '__main__':
    app.run(debug=True)
