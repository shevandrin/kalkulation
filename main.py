from flask import Flask, request
from mysql import connector

from registration import user_registration
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


@app.route('/api/register', methods=['POST'])
def register():
    request_data = request.get_json()
    result = user_registration(request_data)
    return result


if __name__ == '__main__':
    app.run(debug=True)
