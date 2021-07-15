#----------------------Script Below--------------------
from amino import Client
from amino import SubClient
from amino.lib.util.exceptions import *
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from os import path 
import json
THIS_FOLDER = path.dirname(path.abspath(__file__))
emailfile=path.join(THIS_FOLDER,"accounts.json")
dictlist=[]


cid="64365653"     #comId


with open(emailfile) as f: 
    dictlist = json.load(f)

def magicnum(): 
    toime={"start":int(datetime.timestamp(datetime.now())),"end":int(datetime.timestamp(datetime.now()))+300}
    return toime

def sendobj(sub : SubClient):
    timer=[
    magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum()
    ]
    sub.send_active_obj(timers=timer)

def log(cli : Client,email : str, password : str):
    try:
        cli.login(email=email,password=password)
        print(f"logged into {email}\n")
    except VerificationRequired:
        print(f"Verification required for {email}")
    except InvalidPassword or InvalidAccountOrPassword:
        print(f"Incorrect password for {email}") 
    except:
        print(f"An unkown error has occoured for {email}")
        pass

def task(sub : SubClient,email : str,i : int):
  try:
  	sendobj(sub)
  	print(f"Sent coin generating object for {email} times :- {i+1}")
  except:
  	return None
def threadit(acc : dict):
    email=acc["email"]
    device=acc["device"]
    password=acc["password"]
    client=Client(deviceId=device)
    log(cli=client,email=email,password=password)
    client.join_community(cid) 
    subclient=SubClient(comId=cid,profile=client.profile)
    print("Done")
    with ThreadPoolExecutor(max_workers=1) as executorx:
        _ = [executorx.submit(task, subclient,email,i)for i in range(25)]
    client.logout()
    print(f"FINISHED MINING {email}")

def main():
    print(f"{len(dictlist)} accounts loaded")
    for amp in dictlist:
    	threadit(amp)
    print("Mining with all accounts finished")
 
if __name__ == '__main__':
    main()
