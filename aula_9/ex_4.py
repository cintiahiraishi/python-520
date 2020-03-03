#https://viacep.com.br/ws/01001000/json/
import requests
import unittest

def get_endereco(cep):
    return requests.get('https://viacep.com.br/ws/{}/json/'.format(cep)).json()

class TestGetEndereco(unittest.TestCase):

    def test_get_endereco(self):
        cep = '01001000'
        resposta = get_endereco(cep)
        self.assertEqual(
            resposta['logradouro'],
            'Praça da Sé'   
        )

#cep = input('Digite seu cep: ')
#print(get_endereco(cep))
        
if __name__ == '__main__':
    unittest.main()
