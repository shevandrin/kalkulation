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
        res = True if len(res) > 0 else False
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
        res = False if user_id is None else True
        return res

    @classmethod
    def remove(cls, login):
        if User.is_exist(login):
            cursor = cnx.cursor()
            cursor.execute("DELETE FROM User WHERE login = %s", (login, ))
            cnx.commit()
            cursor.close()
            res = True
        else:
            res = False
        return res

    @classmethod
    def get_accounts(cls, user_id):
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM Account WHERE owner = %s", (user_id, ))
        res = cursor.fetchall()
        cursor.close()
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


def user_remove(data):
    if User.remove(data['login']):
        msg = "user is removed"
    else:
        msg = "the service is not available now"
    return msg


def user_accounts(data):
    res = User.get_accounts(data['user_id'])
    return res
