
import psycopg2
import psycopg2.extras


connection = psycopg2.connect(
    user='admin',
    password='4linux',
    host='localhost',
    port=5432,
    database='projeto'
)
cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

####SOLUCAO 1

def find_user_by_email(email):
    cursor.execute('''

        SELECT * FROM users

        WHERE users.email = \'{}\';

    '''.format(email))
    return cursor.fetchone()

email = input('Digite seu email: ')

user = find_user_by_email(email)

if user:
    if password == user['password']:
        print('Autenticado')
    else:
        print('Algo errado aconteceu')

def verifica_senha (email, password):
    cursor.execute('''

        SELECT * FROM users

        WHERE users.email = \'{}\' and
        users.password =  \'{}\'
    ;

    '''.format(email,password))
    return cursor.fetchone()

email = input('Digite seu email: ')
password = input('Digite sua senha: ')

verifica_senha(email,password)

if user:
    if password == user['password']:
        print('Autenticado')
    else:
        print('Algo errado aconteceu')

print ('Senha correta!')