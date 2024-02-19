import requests

import webbrowser

URL = input("Eenter Your Target :")

File = input("Eenter Your File :")

replace = URL.replace(URL,"https://")

x = open(File)
    
for i in x :
        
    r = requests.get(replace + URL + i)
        
    v = replace + URL + i

    t = [ v , r.status_code ]
        
    if r.status_code == 404 :

        print(t,':',"Error")

    if r.status_code == 400 :

        print(t,':',"Error")

    if r.status_code == 200 :

        print(t,':',"Conterol panle")

    if r.status_code == 200 :

        web = webbrowser.open(URL)

        print(web)

