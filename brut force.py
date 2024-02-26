import requests

import webbrowser

URL = input("Eenter Your Target :")

File = input("Eenter Your File :")

replace = URL.replace(URL,"https://")

x = open(File)

counter = 1
    
for i in x :
        
    r = requests.get(replace + URL + i )

    v = replace + URL + i

    #print(v.rstrip())

    if r.status_code == 404 :

        print(str(counter)+" : "+v.rstrip(),"Error 404")

    if r.status_code == 400 :

        print(str(counter)+" : "+v.rstrip(),"Error 404")

    if r.status_code == 200 :

        print(str(counter)+" : "+v.rstrip(),"panle 200")

        webbrowser.open(URL+i)

    counter += 1

