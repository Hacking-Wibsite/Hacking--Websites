try :
    import requests

    import webbrowser

    URL = input("Eenter Your Target :")

    Login = open(input("Eenter Your File :")).read().split()

    Counter = 1
    
    for Password in Login :

        r = requests.get(URL+Password)
            
        if r.status_code == 404 :

            print(Counter,':',URL+Password,"404 Error")

        elif r.status_code == 200 :

            print(Counter,':',URL+Password,"200 admin")

            file = open("passwrod1.txt","a")
            
            file.write(URL+Password+"\n")
            
            file.close()

            webbrowser.open(URL+Password)
            
        Counter += 1
except :
    print("Internet Error")
