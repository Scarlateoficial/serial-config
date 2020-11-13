# -*- coding: utf-8 -*-
import os
import sys
import requests
import serial
import json
import platform
from time import sleep
from core.auth import User
from core import defs

#variaveis e objetos globais:
user = User()
so = platform.system()
config = open('config.json','r')
config = json.load(config)
alerts = []

version = config['version']
ano = config['ano']
autor = config['autor']

#funções
def login():
    email = input('Email: ')
    senha = input('Senha: ')
    print()

    r = user.login(email=email, senha=senha)
    return r

def start():
    print(f'------- Bem vindo ao Serial-Config v{version}-------')
    sleep(0.5)
    print(f'-- Copyright (C) {ano} by {autor} --')
    sleep(0.5)
    print('----- Faça Login para utilizar o sistema -----')
    sleep(0.5)
    print('\n----------------------------------------------\n')
    sleep(0.5)

def menu():
    os.system('clear')
    for alert in alerts:
        defs.log(alert)
    
    print('\n\nEscolha uma opção')
    print(' 0 - Configurar/Modificar dispositivo')
    print(' 1 - Observar serial')
    print(' 2 - Buscar dispositivo')
    print(' 3 - Ver log de dispositivo')
    print(' 4 - Finalisar programa')

    t = input('\n :')

    if t == '0':
        defs.config_dispositivo()
    elif t == '1':
        defs.observa_serial()
    elif t == '2':
        defs.busca_dispositivo()
    elif t == '3':
        defs.logs_dispositivo()
    elif t == '4':
        return False
    else:
        alerts.append('Opção invalida')
        menu()

def main():
    start()
    r = input('Continuar (y/n): ')
    if r != "y" and r != "Y":
        return

    os.system('clear')
    while True:
        r = login()
        if r['sucess'] == False:
            if r['conecao'] == True:
                defs.log(r['error'])
                t = input('Tentar novamente ??? (y/n): ')
                if t != "y" and t != "Y":
                    defs.log('Processo terminado pelo usuario')
                    return
                else:
                    continue
            else:
                defs.log(r['error'])
                return
        elif r['sucess'] == True:
            defs.log('Logado com sucesso!')
            break
        else:
            defs.log('Erro no sistema!')
            return

    if not user.verificado:
        defs.log('Verifique seu email para ter acesso ao sistema!')
        return
    if user.check_acess():
        defs.log('Acesso permitido')
    else:
        defs.log('Usuario sem acesso ao sistema')
        return

    while True:
        if menu():
            continue
        else:
            break

    defs.log('Processo finalizado')
    return

if __name__ == '__main__':
    main()