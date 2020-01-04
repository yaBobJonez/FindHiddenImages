import requests
import random
Key = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
url = 'https://i.imgur.com/'
removedURL = "https://i.imgur.com/removed.png"
RemovedReq = requests.get(removedURL, allow_redirects=True).content
LenTxt = len(open("List.txt", 'r').readlines())


print("""
ENG: Choice type of file
UA:Оберіть тип файлу
RU:Выберите тип файла

=====================
[1]ico
[2]png
[3]jpg
[4]gif
[5]Another/Інше/Другое
""")
Choice = input()
if Choice == "1":
    while True:
        Adr = url + ''.join([random.choice(list(Key)) for x in range(7)]) + ".ico"
        RequestedImage = requests.get(Adr, allow_redirects=True).content
        if RequestedImage != RemovedReq:
            ListWrite = open("List.txt", 'a')
            print(Adr)
            open(str(LenTxt)+".ico", 'wb').write(RequestedImage)
            ListWrite.write(Adr + "\n")
            LenTxt += 1
            ListWrite.close();
if Choice == "2":
    while True:
        Adr = url + ''.join([random.choice(list(Key)) for x in range(7)]) + ".png"
        RequestedImage = requests.get(Adr, allow_redirects=True).content
        if RequestedImage != RemovedReq:
            ListWrite = open("List.txt", 'a')
            print(Adr)
            open(str(LenTxt)+".png", 'wb').write(RequestedImage)
            ListWrite.write(Adr + "\n")
            LenTxt += 1
            ListWrite.close();
if Choice == "3":
    while True:
        Adr = url + ''.join([random.choice(list(Key)) for x in range(7)]) + ".jpg"
        RequestedImage = requests.get(Adr, allow_redirects=True).content
        if RequestedImage != RemovedReq:
            ListWrite = open("List.txt", 'a')
            print(Adr)
            open(str(LenTxt)+".jpg", 'wb').write(RequestedImage)
            ListWrite.write(Adr + "\n")
            LenTxt += 1
            ListWrite.close();
if Choice == "4":
    while True:
        Adr = url + ''.join([random.choice(list(Key)) for x in range(7)]) + ".gif"
        RequestedImage = requests.get(Adr, allow_redirects=True).content
        if RequestedImage != RemovedReq:
            ListWrite = open("List.txt", 'a')
            print(Adr)
            open(str(LenTxt)+".gif", 'wb').write(RequestedImage)
            ListWrite.write(Adr + "\n")
            LenTxt += 1
            ListWrite.close();
if Choice == "5":
    print("""
    ENG: Input your type
    UA: Введіть свій тип
    RU: Введите свой тип""")
    OwnType = input()
    while True:
        Adr = url + ''.join([random.choice(list(Key)) for x in range(7)]) + OwnType
        RequestedImage = requests.get(Adr, allow_redirects=True).content
        if RequestedImage != RemovedReq:
            ListWrite = open("List.txt", 'a')
            print(Adr)
            open(str(LenTxt)+OwnType, 'wb').write(RequestedImage)
            ListWrite.write(Adr + "\n")
            LenTxt += 1
            ListWrite.close();
#r = requests.get(url, allow_redirects=True)
#open('google.ico', 'wb').write(r.content)
