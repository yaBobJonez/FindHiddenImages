#####################################
#                                   #
#       Autor:RostislavFisher       #
#       Country:Ukraine             #
#####################################
import requests
import random

print("""
ENG: Choice Service
UA:Оберіть сервіс
RU:Выберите сервис

=====================
[1]Imgur
[2]LightShot
[3]
""")

ChoiceService = input()
if ChoiceService == "1":
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
        Key = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        url = 'https://i.imgur.com/'
        removedURL = "https://i.imgur.com/removed.png"
        RemovedReq = requests.get(removedURL, allow_redirects=True).content
        LenTxt = len(open("List.txt", 'r').readlines())
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
if ChoiceService == "2":
    import bs4
    Key = '123456789qwertyuiopasdfghjklzxcvbnm'
    url = 'https://prnt.sc/'
    LenTxt = len(open("List.txt", 'r').readlines())
    
    removedURL = "https://prnt.sc/18jgksdgh"
    RemovedReq = requests.get(removedURL, headers={'User-Agent': 'Mozilla/5.0'})
    RemovedReq = bs4.BeautifulSoup(RemovedReq.text, "html.parser")
    print(RemovedReq)
    RemovedReq = RemovedReq.find('img', id='screenshot-image')['src']
    while True:
        Adr = url + ''.join([random.choice(list(Key)) for x in range(6)])
        

        RequestedImage = requests.get(Adr, headers={'User-Agent': 'Mozilla/5.0'})
        RequestedImage = bs4.BeautifulSoup(RequestedImage.text, "html.parser")
        RequestedImage = RequestedImage.find('img', id='screenshot-image')['src']
        print(RequestedImage)
        print(RemovedReq)
        import time
        if RequestedImage != RemovedReq:
            ListWrite = open("List.txt", 'a')
            print(Adr + "########")
            ListWrite.write(Adr + "\n")
            LenTxt += 1
            
            ListWrite.close();
            RequestedImage = requests.get(RequestedImage, allow_redirects=True).content
            open(str(LenTxt)+".png", 'wb').write(RequestedImage)
    
