import requests
import json
import msvcrt
from termcolor import colored

webhookurl = "https://discord.com/api/webhooks/1502777901563772960/V7GkvHHoYjdoylmXVqt_aMCSvFOpvxDyKQDE_w6HMRKeNlHkNKLazDfiOHemxR_ejo2t"

logo = r"""
               _____ _             _    
              / ____| |           | |   
  _ __  _   _| (___ | |_ ___   ___| | __
 | '_ \| | | |\___ \| __/ _ \ / __| |/ /
 | |_) | |_| |____) | || (_) | (__|   < 
 | .__/ \__, |_____/ \__\___/ \___|_|\_\
 | |     __/ |                          
 |_|    |___/         

"""

print(colored(logo, "blue"))

url = input(colored("What piece of clothing do you want to check? (Paste URL): ", "blue")) + ".js"
if url == "0.js":
    url = "https://coldcultureworldwide.com/products/curved-tee-eclipse.js"

#converting resonse from requests.get to a json to look through
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
data = response.json()

variants = data["variants"]

answer = input(colored("What size do you want to bot? (XS/S/M/L/XL/XXL, All): ", "blue"))
print(colored("Press ESC to stop Scan", on_color="on_cyan"))

try:
    readStock = open("stock.json", "r")
    oldStock = json.load(readStock)
    readStock.close()
except:
    oldStock = {}

try:
    readSelectStock = open("selectstock.json", "r")
    oldSelectStock = json.load(readSelectStock)
    readSelectStock.close()
except:
    oldSelectStock = {}

save = {}
selectSave = {}


if answer == "0":

    while True:

        for variant in variants:

            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            data = response.json() #decodes json response as a python lib
            variants = data["variants"]

            availibility = variant["available"]
            size = variant["title"]

            if oldStock.get(size) != availibility:

                if availibility == False:
                    print(f"Size {size} is not Available")

                    message = {"content": f"Size {answer} is No Longer Available (Full Scan) ❌ <@724508668606808076>"}

                    requests.post(webhookurl, message)
                
                if availibility == True:
                    print(f"Size {size} is Available")

                    message = {"content": f"Size {size} has Changed and is Available (Full Scan) ✅ <@724508668606808076>"}

                    requests.post(webhookurl, message)

            save[size] = availibility
            oldStock[size] = availibility

        writeStock = open("stock.json", "w")
        json.dump(save, writeStock)
        writeStock.close()

        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\x1b':  #esc key
                break


#Individual size check
else:
    sizes = {
        "XS": 0,
        "S": 1,
        "M": 2,
        "L": 3,
        "XL": 4,
        "XXL": 5,
    }
    varNum = sizes[answer]

    while True:

        #fetching data again
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        data = response.json() #decodes json response as a python lib

        availibility = data["variants"][varNum]["available"]
        size = data["variants"][varNum]["title"]

        print(colored(f"Availibility: {availibility}", "yellow"))

        if oldSelectStock.get(size) != availibility: #.get size so it wont crash and js load it next run (still count as a change)
            
            if availibility == True:

                #notify
                print(f"Size {size} availibility has changed to: {availibility}")
                message = {"content": f"Size {answer} is Available (Selective Scan) ✅ <@724508668606808076>"}
                requests.post(webhookurl, message)

            if availibility == False:

                print(f"Size {size} availibility has changed to: {availibility}")
                message = {"content": f"Size {answer} is No Longer Available (Selective Scan) ❌ <@724508668606808076>"}
                requests.post(webhookurl, message)

        selectSave[size] = availibility
        oldSelectStock[size] = availibility

        f = open("selectstock.json", "w")
        json.dump(selectSave, f)
        f.close()


        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\x1b':  #esc key
                break

    