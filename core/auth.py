# -*- coding: utf-8 -*-
import requests

Api_dados = 'http://192.168.0.107:8000/api/'
credenciais_api_dados = ("julio","15052005")
min_cargo = 'A'

class User():
    id = None
    nome = ''
    token = ''
    cargo = ''
    verificado = False

    def check_acess(self, cargo_min = min_cargo):
        return self.cargo >= cargo_min

    def login(self, email='',senha=''):
        if self.id != None:
            return {
                "sucess":False,
                "auth": False,
                "conecao":True,
                "error":"Usuario já autenticado.",
            }
        else:
            r = 0
            try:
                r = requests.post(Api_dados+"login/",data={"email": email, "password": senha}, auth=credenciais_api_dados)
            except:
                return {
                    "sucess":False,
                    "auth": False,
                    "conecao":False,
                    "error":"Não foi possivel realizar conexão com o servidor",
                }

            if r.status_code != 200 and r.status_code != "200":
                return {
                    "sucess":False,
                    "auth": False,
                    "conecao":True,
                    "error":f"Erro na requisição, erro: {str(r.status_code)}",
                }
            else:
                data = r.json()
                if data['sucess'] == True and data['auth'] == True:
                    self.id = data['dados']['id']
                    self.nome = data['dados']['nome']
                    self.token = data['dados']['user_token']
                    self.cargo = data['dados']['cargo']
                    self.verificado = data['dados']['is_trusty']

                    return {
                        "sucess":True,
                        "auth": True,
                    }
                else:
                    return {
                        "sucess":False,
                        "auth": False,
                        "conecao":True,
                        "error":f"Não foi possivel realizar a autenticação, erro: {data['error']}",
                    }