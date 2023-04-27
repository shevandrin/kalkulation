from conn import cnx


class Account:
    def __int__(self, account_id, account_name, owner, corr):
        self.account_id = account_id
        self.account_name = account_name
        self.owner = owner
        self.corr = corr

    @classmethod
    def is_exist(cls, account_id):
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM Account WHERE account_id = %s", (account_id,))
        res = cursor.fetchall()
        res = True if len(res) > 0 else False
        cursor.close()
        return res

    @classmethod
    def create(cls, account_name, owner):
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO Account (account_name, owner) VALUES (%s, %s)", (account_name, owner))
        account_id = cursor.lastrowid
        cnx.commit()
        cursor.close()
        res = False if account_id is None else True
        return res

    @classmethod
    def delete(cls, account_id):
        if Account.is_exist(account_id):
            print(account_id)
            cursor = cnx.cursor()
            cursor.execute("DELETE FROM Account WHERE account_id = %s", (account_id, ))
            cnx.commit()
            cursor.close()
            res = True
        else:
            res = False
        return res


def account_create(data):
    if Account.create(data['account_name'], data['account_owner']):
        msg = 'New Account ' + data['account_name'] + ' is created'
    else:
        msg = 'the service is not available now'
    return msg


def account_delete(data):
    if Account.delete(data['account_id']):
        msg = "Account is deleted"
    else:
        msg = 'the service is not available now'
    return msg
