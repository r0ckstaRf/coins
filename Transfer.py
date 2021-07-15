from amino import Client
from amino import SubClient
from amino.lib.util.exceptions import *
from concurrent.futures import ThreadPoolExecutor
from os import path
import json

THIS_FOLDER = path.dirname(path.abspath(__file__))
emailfile=path.join(THIS_FOLDER,"accounts.json")
dictlist=[]


cid="64365653"     #comId


endlink="iz5qs2"    #end link of Blog only


blog=Client().get_from_code(endlink).objectId
totalcoin=0
with open(emailfile) as f:
    dictlist = json.load(f)
dicklis=dictlist.reverse()
def log(cli : Client,email : str, password : str):
    try:
        cli.login(email=email,password=password)
    except VerificationRequired:
        print(f"Verification required for {email}")
    except InvalidPassword or InvalidAccountOrPassword:
        print(f"Incorrect password for {email}")
    except:
        print(f"An unkown error has occoured for {email}")

def threadit(acc : dict):
    global totalcoin
    email=acc["email"]
    device=acc["device"]
    password=acc["password"]
    client=Client(deviceId=device)
    log(cli=client,email=email,password=password)
    try:
    	client.join_community(cid)
    	subclient=SubClient(comId=cid,profile=client.profile)
    except Exception as e:
    	print(e)
    try:
        subclient.lottery()
    except: 
        pass
    coins=int(client.get_wallet_info().totalCoins)
    totalcoin += coins
    if coins !=0:
        subclient.send_coins(coins=coins,blogId=blog)
        print(f"Transferred {coins} coins from {email}")
    else:
        print(f"Balance 0 in {email}\n") 
    print(f"Total coins till now :- {totalcoin}\n")
    client.logout()

def main():
    print(f"{len(dictlist)} accounts loaded")
    for amp in dictlist:
    	threadit(amp)
    print(f"Collected all coins from {len(dictlist)} ids")

if __name__ == '__main__':
    main()
    