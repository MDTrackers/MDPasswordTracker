import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil

os.system("cls")

# Author : MDTrackers
# Youtube : www.youtube.com/channel/UCGsKXfbCyhZoLIRukYUQyYQ
# Instagram : www.instagram.com/mdtrackers/

allpsa = ""

def backed() :
    print(color.WHITE+"Press Enter to return to the menu...")
    input()
    os.system("cls")
    startmenu()

os.system('color')

def startmenu() :
    print(color.Blue+"""

    ███╗░░░███╗██████╗░  ████████╗██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░░██████╗
    ████╗░████║██╔══██╗  ╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗██╔════╝
    ██╔████╔██║██║░░██║  ░░░██║░░░██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝╚█████╗░
    ██║╚██╔╝██║██║░░██║  ░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗░╚═══██╗
    ██║░╚═╝░██║██████╔╝  ░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║██████╔╝
    ╚═╝░░░░░╚═╝╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═════╝░
    """)
    print(color.Blue+"Created By MDTrackers")
    print(color.RED+"Youtube : www.youtube.com/channel/UCGsKXfbCyhZoLIRukYUQyYQ")
    print(color.RED+"Instagram : www.instagram.com/mdtrackers")
    print(color.WHITE)
    print()
    print(color.Blue+"Well, now choose one of these options")
    print(color.WHITE)
    print("1 =========> Show all usernames and passwords of the database")
    print("2 =========> Display all card numbers in the database")
    print("3 =========> Clear")
    print("0 =========> Exit")
    print()
    intnum = input("Select One > ")
    print("")
    if intnum=="3" :
        os.system("cls")
        startmenu()
    if intnum=="1" :
        print(allpsa)
        backed()
    if intnum=="0" :
        print(color.Blue+"Goodbye, have a good day")
        print(color.WHITE)
        exit()
    if intnum=="2" :
        print(color.Blue+"Coming Soon...")
        print("")
        backed()
    if intnum=="" :
        print(color.Blue+"Please select an option")
        backed()
class color : 
   Blue = '\033[96m'
   GREEN = '\033[92m'
   RED = '\033[91m'
   WHITE = '\033[0m'

print(color.Blue+"""

███╗░░░███╗██████╗░  ████████╗██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░░██████╗
████╗░████║██╔══██╗  ╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗██╔════╝
██╔████╔██║██║░░██║  ░░░██║░░░██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝╚█████╗░
██║╚██╔╝██║██║░░██║  ░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗░╚═══██╗
██║░╚═╝░██║██████╔╝  ░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║██████╔╝
╚═╝░░░░░╚═╝╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═════╝░
""")

print(color.Blue+"Created By MDTrackers")
print(color.RED+"Youtube : www.youtube.com/channel/UCGsKXfbCyhZoLIRukYUQyYQ")
print(color.RED+"Instagram : www.instagram.com/mdtrackers")

print(color.WHITE)

lcc = input("Local State > ")
lgg = input("Login Data > ")

FileName = 116444736000000000
NanoSeconds = 10000000

mypasswordlist = []

def mstr_key():
    try:
     with open(lcc,
              "r", encoding='utf-8') as f:
        local_state = f.read()
        local_state = json.loads(local_state)
    except:
        exit()
    master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = master_key[5:]  # removing DPAPI
    master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
    return master_key


def decrypt_payload(cipher, payload):
    return cipher.decrypt(payload)

def chr_gn(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)

def decrypt_password(buff, master_key):
    try:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = chr_gn(master_key, iv)
        decrypted_pass = decrypt_payload(cipher, payload)
        decrypted_pass = decrypted_pass[:-16].decode()  # remove suffix bytes
        return decrypted_pass
    except Exception as e:
        return "Chrome < 80"

urls = []
myusers = []


def psw_get():
    master_key = mstr_key()
    login_db = lgg
    try:
        shutil.copy2(login_db,
                     "Loginvault.db")  # making a temp copy since Login Data DB is locked while Chrome is running
    except:
        print("[*] Brave Browser Not Installed !!")
    conn = sqlite3.connect("Loginvault.db")
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
        for r in cursor.fetchall():
            url = r[0]
            username = r[1]
            encrypted_password = r[2]
            decrypted_password = decrypt_password(encrypted_password, master_key)
            if username != "" or decrypted_password != "":
                mypasswordlist.append(decrypted_password)
                urls.append(url)
                myusers.append(username)
    except Exception as e:
        pass

    cursor.close()
    conn.close()
    try:
        os.remove("Loginvault.db")
    except Exception as e:
        pass


paa = ""
psw_get()
lenall = len(urls)

a = 0
while(a < lenall) :
    allpsa += color.RED+"Website : "+urls[a] + "\n" + color.GREEN+"User : " + myusers[a] + "\n" + color.Blue+"Password : " + mypasswordlist[a] + "\n\n"
    a+=1

mycardnumber = []
mycardexpiremon = []
mycardexpireyear = []
mycardpassword = []

def crdt_aa():
    master_key = mstr_key()
    login_db = os.environ[
                   'USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\default\Web Data'
    shutil.copy2(login_db,
                     "CCvault.db")  # making a temp copy since Login Data DB is locked while Chrome is running
    conn = sqlite3.connect("CCvault.db")
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM credit_cards")
        for r in cursor.fetchall():
            username = r[1]
            encrypted_password = r[4]
            decrypted_password = decrypt_password(encrypted_password, master_key)
            expire_mon = r[2]
            expire_year = r[3]
            mycardnumber.append(decrypted_password)
            mycardexpiremon.append(expire_mon)
            mycardexpireyear.append(expire_year)

    except Exception as e:
        pass

    cursor.close()
    conn.close()
    try:
        os.remove("CCvault.db")
    except Exception as e:
        pass

print()
print(color.Blue+"Well, now choose one of these options")
print(color.WHITE)
print("1 =========> Show all usernames and passwords of the database")
print("2 =========> Display all card numbers in the database")
print("3 =========> Clear")
print("0 =========> Exit")
print()
intnum = input("Select One > ")
print("")

if intnum=="3" :
    os.system("cls")
    startmenu()
if intnum=="1" :
    print(allpsa)
    backed()
if intnum=="0" :
    print(color.Blue+"Goodbye, have a good day")
    print(color.WHITE)
    exit()
if intnum=="2" :
    print(color.Blue+"Coming Soon...")
    print("")
    backed()
if intnum=="" :
    print(color.Blue+"Please select an option")
    backed()