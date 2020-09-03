import requests
import random

print("""
EN: Choose a hosting
UA: Оберіть хостінг
RU: Выберите хостинг
=====================
[1]Imgur
[2]LightShot
""")

Formats = {"1": ".ico", "2": ".png", "3": ".jpg", "4": ".gif"}
def generate(Format):
    Key = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    url = 'https://i.imgur.com/'
    removedURL = "https://i.imgur.com/removed.png"
    RemovedReq = requests.get(removedURL, allow_redirects=True).content
    LenTxt = len(open("List.txt", 'r').readlines())
    while True:
        Adr = url + ''.join([random.choice(list(Key)) for x in range(7)]) + Format
        RequestedImage = requests.get(Adr, allow_redirects=True).content
        if RequestedImage != RemovedReq:
            ListWrite = open("List.txt", 'a')
            print(Adr)
            open(str(LenTxt)+Format, 'wb').write(RequestedImage)
            ListWrite.write(Adr + "\n")
            LenTxt += 1
            ListWrite.close();

ChoiceService = input()
if ChoiceService == "1":
    print("""
EN: Choose a type of files
UA: Оберіть тип файлу
RU: Выберите тип файла
=====================
[1]ico
[2]png
[3]jpg
[4]gif
[5]Other/Інше/Другое
    """)
    Choice = input()
    if Choice == "5":
        print("""
EN: Input your type
UA: Введіть свій тип
RU: Введите свой тип
        """)
        OwnType = input()
        generate("." + OwnType)
    else:
        generate(Formats[Choice])
if ChoiceService == "2":
    import bs4
    Key = '123456789qwertyuiopasdfghjklzxcvbnm'
    url = 'https://prnt.sc/'
    LenTxt = len(open("List.txt", 'r').readlines())
    
    removedURL = "https://prnt.sc/18jgksdgh"
    RemovedReq = requests.get(removedURL, headers={'User-Agent': 'Mozilla/5.0'})
    RemovedReq = bs4.BeautifulSoup(RemovedReq.text, "html.parser")
    RemovedReq = RemovedReq.find('img', id='screenshot-image')['src']
    print("""
EN: Choose the amount of files
UA: Оберіть кількість файлів
RU: Выберите количество файлов

=====================
    
    """)
    FileAmount = int(input())
    FileLen = 0
    while FileAmount > FileLen:
        Adr = url + ''.join([random.choice(list(Key)) for x in range(6)])
        

        RequestedImage = requests.get(Adr, headers={'User-Agent': 'Mozilla/5.0'})
        RequestedImage = bs4.BeautifulSoup(RequestedImage.text, "html.parser")
        RequestedImage = RequestedImage.find('img', id='screenshot-image')['src']
        if RequestedImage != RemovedReq:
            ListWrite = open("List.txt", 'a')
            print(Adr)
            ListWrite.write(Adr + "\n")
            LenTxt += 1
            
            ListWrite.close();
            RequestedImage = requests.get(RequestedImage, allow_redirects=True).content
            open(str(LenTxt)+".png", 'wb').write(RequestedImage)
            FileLen = FileLen + 1
