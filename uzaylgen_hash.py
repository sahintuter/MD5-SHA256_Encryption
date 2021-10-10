import hashlib

print("""
                      _                        _               _     
 _   _ ______ _ _   _| | __ _  ___ _ __       | |__   __ _ ___| |__  
| | | |_  / _` | | | | |/ _` |/ _ \ '_ \ _____| '_ \ / _` / __| '_ \ 
| |_| |/ / (_| | |_| | | (_| |  __/ | | |_____| | | | (_| \__ \ | | |
 \__,_/___\__,_|\__, |_|\__, |\___|_| |_|     |_| |_|\__,_|___/_| |_|
                |___/   |___/                                        
""")
print("""

[+] MD5 şifreleme    (1)
[+] SHA256 şifreleme (2)

""")

while True:
    secim= int(input("Seçiminiz: \n"))

    if secim==1:
        print("MD5 şifrelemeyi seçtiniz\n")
        girdi = input("Şifrelenecek metin: ")
        sifre= hashlib.md5(girdi.encode('utf-8')).hexdigest()
        print("\n Şifrelenmiş metin " + sifre)
        break
    elif secim==2:
        print("SHA256 şifrelemeyi seçtiniz\n")
        girdi2 = input("\n Şifrelenecek metin: ")
        sifre2= hashlib.sha256(girdi2.encode('utf-8')).hexdigest()
        print("Şifrelenmiş metin: " + sifre2)
        break
    else:
        print("Yanlış seçim girdiniz.")





