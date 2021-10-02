#!/usr/bin/python
#matrice
import re
import time
import datetime
import argparse

#autrre
import time
import hmac
import urllib
import requests
import hashlib
import base64
import sys
import json






try:
    print("on try")
    #cours du SOL
    content=requests.get("https://api.coingecko.com/api/v3/coins/solana")
    data=content.json()
    SOLEURcours=str(data['market_data']['current_price']['eur'])
    SOL24h=str(data['market_data']['price_change_percentage_24h_in_currency']['eur'])
    SOL7j=str(data['market_data']['price_change_percentage_7d_in_currency']['eur'])


    #cours du BTC
    content=requests.get("https://api.coingecko.com/api/v3/coins/bitcoin")
    data=content.json()
    BTCEURcours=str(data['market_data']['current_price']['eur'])
    BTC24h=str(data['market_data']['price_change_percentage_24h_in_currency']['eur'])
    BTC7j=str(data['market_data']['price_change_percentage_7d_in_currency']['eur'])


    #cours du EGLD
    content=requests.get("https://api.coingecko.com/api/v3/coins/elrond-erd-2")
    data=content.json()
    EGLDEURcours=str(data['market_data']['current_price']['eur'])
    EGLD24h=str(data['market_data']['price_change_percentage_24h_in_currency']['eur'])
    EGLD7j=str(data['market_data']['price_change_percentage_7d_in_currency']['eur'])
    #cours du ETH
    content=requests.get("https://api.coingecko.com/api/v3/coins/ethereum")
    data=content.json()
    ETHEURcours=str(data['market_data']['current_price']['eur'])
    ETHD24h=str(data['market_data']['price_change_percentage_24h_in_currency']['eur'])
    ETHD7j=str(data['market_data']['price_change_percentage_7d_in_currency']['eur'])
    print("on stock")
    now = datetime.datetime.now()  # recup date
    timestamp = time.mktime(now.timetuple())  # convertion
    h=datetime.datetime.fromtimestamp(int(timestamp)).strftime('%H')
    m=datetime.datetime.fromtimestamp(int(timestamp)).strftime('%M')           
    mon_fichier = open("data.txt", "w") #on cree le fichier ou tout est stocke
    mon_fichier.write(str("MAJ @ "+str(h)+":"+str(m)+" || SOLANA : "+str(SOLEURcours)[:5]+" EUR | Var 24h : "+str(SOL24h)[:4]+"% | Var 7j : "+str(SOL7j)[:5]+"% ||  BITCOIN : "+str(BTCEURcours)[:5]+" EUR | Var 24h: "+str(BTC24h)[:4]+"% | Var 7j: "+str(BTC7j)[:4]+"% || ELROND : "+str(EGLDEURcours)[:6]+" EUR | "+" Var 24h : "+str(EGLD24h)[:3]+"%  | Var 7j: "+str(EGLD7j)[:3]+"% || ETHEREUM : "+str(ETHEURcours)[:5]+" EUR | Var 24h : "+str(ETHD24h)[:4]+"% | Var 7j : "+str(ETHD7j)[:5]+"% " ))

    mon_fichier.close()
    mon_fichier = open("data.txt", "a") # on rajoute des infos dans le fichier
    ## RIEN A RAJOUTER NOW
    mon_fichier.close()



    
except:

    print("on bug")
    time.sleep(5)



