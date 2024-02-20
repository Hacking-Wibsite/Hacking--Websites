import requests

import webbrowser

URL = input("Eenter Your Target :")

File = input("Eenter Your File :")

replace = URL.replace(URL,"https://")

x = open(File)
    
for i in x :
        
    r = requests.get(replace + URL + i)

    v = replace + URL + i

    if r.status_code == 404 :

        print(v.splitlines(),"x Error 404")

    if r.status_code == 200 :

        print(v.splitlines(),"panle")
        
    if r.status_code == 200 :

        webbrowser.open(URL+i)

    if r.status_code == 400 :

        print(v.splitlines(),"x Error 400")


    #print(v.splitlines(),

    #r.status_code)


