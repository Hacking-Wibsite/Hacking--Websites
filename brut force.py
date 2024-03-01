import requests

import webbrowser

URL = input("Eenter Your Target :")

Login = open(input("Eenter Your File :"),"r").read().split()

for i in Login :

    r = requests.get(URL+i)

    if r.status_code == 404 :

        print(URL+i,"404 Error")

    elif r.status_code == 200 :

        print(URL+i,"200 Aadmin")

        webbrowser.open(URL+i)
        
    else:
        
        print("internet Error")

        
