from conn import cnx


class User:
    def __init__(self, login, user_name, password):
        self.user_name = user_name
        self.login = login
        self.password = password

    @classmethod
    def is_exist(cls, login):
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM User WHERE login = %s", (login, ))
        res = cursor.fetchall()
        if len(res) > 0:
            res = True
        else:
            res = False
        cursor.close()
        return res

    @classmethod
    def register(cls, login, user_name, password):
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO User (login, user_name, password) VALUES (%s, %s, %s)",
                       (login, user_name, password))
        user_id = cursor.lastrowid
        cnx.commit()
        cursor.close()
        if user_id is None:
            res = False
        else:
            res = True
        return res


def user_registration(data):
    if User.is_exist(data['login']):
        msg = 'login \'' + data['login'] + '\' is not unique'
    else:
        if User.register(data['login'], data['user_name'], data['password']):
            msg = 'user ' + data['user_name'] + ' has registered'
        else:
            msg = 'the service is not available now'
    return msg
