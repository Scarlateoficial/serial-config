# -*- coding: utf-8 -*-
import os
import sys
import requests
import serial
import json
import platform
from tqdm import tqdm
from time import sleep
from core.auth import User

#for i in tqdm(range(1000)):
#     sleep(0.01)

#variaveis e objetos globais:
user = User()
so = platform.system()
config = open('config.json','r')
config = json.load(config)

version = config['version']
ano = config['ano']
autor = config['autor']

#funções
def login():
    email = input('\nEmail: ')
    senha = input('\nSenha: ')

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

def log(menssagem):
    print(f"[ INFO ] {menssagem}")

def main():
    start()
    r = input('Continuar (y/n): ')
    if r != "y" and r != "Y":
        return
    while True:
        r = login()
        if r['sucess'] == False:
            if r['conecao'] == True:
                log(r['error'])
                t = input('Tentar novamente ??? (y/n): ')
                if t != "y" and t != "Y":
                    log('Processo terminado pelo usuario')
                    return
                else:
                    continue
            else:
                log(r['error'])
                return
        elif r['sucess'] == True:
            log('Logado com sucesso!')
            break
        else:
            log('Erro no sistema!')
            return

    if user.check_acess():
        log('Acesso permitido')
    else:
        log('Usuario sem acesso ao sistema')
        return

if __name__ == '__main__':
    main()