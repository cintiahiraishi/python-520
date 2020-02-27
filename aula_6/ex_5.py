
import pymongo


client = pymongo.MongoClient()
db = client.projeto

def users_update(email, password):
    db.users.update({
        'email':email,
    }, {
        '$set':{
            'password': password
        }
    })

email= input ('Digite seu email: ')
password= input ('Digite sua senha: ')

users_update(email,password)