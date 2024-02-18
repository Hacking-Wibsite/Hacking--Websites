import requests

URL = input("Eenter Your Target :")  #www.exmple.com                                         

File = input("Eenter Your File :")

replace = URL.replace(URL,"https://")

try:
    
    x = open(File)
    
    for i in x :
        
        r = requests.get(replace + URL + i)
        
        v = replace + URL + i
        
        #print(r.status_code)
        
    if r.status_code == 200 :
        
        print("Conterol panle",r.status_code,":",v)
        
    if r.status_code == 400 :
        
        print("x Error",r.status_code,":",v)
        
    if r.status_code == 404 :
        
        print("x Error",r.status_code,":",v)
        
except:
    
    print("Internet Error")


    
