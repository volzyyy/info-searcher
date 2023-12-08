import requests
import json
import logging 
#Please get the apis from this website: https://www.abstractapi.com/api
keyForPhone = ""
keyForEmail = ""
keyForScreeenShot = ""
while True:
  try:
    banner = """
    
                                                                                     
                                                                                     
                                                                                     
                                                                                     
                                                                                     
                                                                                     
                                                                                     
                                                                                     
                                                                                     
                                                                                     
 ██▓ ███▄    █   █████▒▒█████       ██████ ▓█████ ▄▄▄       ██▀███   ▄████▄   ██░ ██ 
▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒   ▒██    ▒ ▓█   ▀▒████▄    ▓██ ▒ ██▒▒██▀ ▀█  ▓██░ ██▒
▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒   ░ ▓██▄   ▒███  ▒██  ▀█▄  ▓██ ░▄█ ▒▒▓█    ▄ ▒██▀▀██░
░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░     ▒   ██▒▒▓█  ▄░██▄▄▄▄██ ▒██▀▀█▄  ▒▓▓▄ ▄██▒░▓█ ░██ 
░██░▒██░   ▓██░░▒█░   ░ ████▓▒░   ▒██████▒▒░▒████▒▓█   ▓██▒░██▓ ▒██▒▒ ▓███▀ ░░▓█▒░██▓
░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░    ▒ ▒▓▒ ▒ ░░░ ▒░ ░▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ░▒ ▒  ░ ▒ ░░▒░▒
 ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░    ░ ░▒  ░ ░ ░ ░  ░ ▒   ▒▒ ░  ░▒ ░ ▒░  ░  ▒    ▒ ░▒░ ░
 ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒     ░  ░  ░     ░    ░   ▒     ░░   ░ ░         ░  ░░ ░
 ░           ░            ░ ░           ░     ░  ░     ░  ░   ░     ░ ░       ░  ░  ░
                                                                    ░                
                                                                                     
                                                                                     
                                                                                     
                                                                                     
                                                                                     
                                                                                     
                                                                                     
                                                                                     
                                                                                     
                                                                                     

                                   made by volzy
                                   Github: https://github.com/volzyyy
"""
    print(banner)
    op = """Options:  
  [+] - 1: IP info. Get info of an ip address.It will also return an image containing Long and Lat
  [+] - 2: Phone number info. This will return info of an phone number.
  [+] - 3: Email info.This will return info about a email address
  [+] - 4: Screenshot website.This will screenshot a website.
  [+] - e: press e to exit
  """
    print(op)
    inp = input("Please enter an option: ")
    if inp == "1":
      try:
        inp = input("Please enter an ip: ")
    

        header = {"Accept": "application/json"}
        response = requests.get(f"http://ip-api.com/json/{inp}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query")
        val = response.json()
        lang = val["lat"]
        lin = val["lon"]
        print("OK: "+str(response.ok))

        print(val)
        inpfn = input("please enter a file name to make (please add .jpeg at the end of the file name): ")
        re = requests.get(f"https://maps.geoapify.com/v1/staticmap?apiKey=647699309aa547cebfee5adc9007171c&style=osm-bright&width=600&height=800&format=jpeg&center=lonlat:{lin},{lang}")
        filef = re.content
        with open(inpfn,"wb") as file:
            file.write(filef)
        print(f"made a file {inpfn}.This contains the picture")
      except ValueError as e:
        logging.error(e)  
      except KeyError as e:
        logging.error(e)
        print("If the error says 'lat' you most likely did not add an ip.Please try again")
    elif inp == "2":
        inf = input("enter a phone number to be searched: ")
        phone = requests.get(f"https://phonevalidation.abstractapi.com/v1/?api_key={keyForPhone}&phone={inf}")
        vall = phone.json()
        print(vall)
    elif inp == "3":
      inpemail = input("Enter the email: ")
      reem = requests.get(f"https://emailvalidation.abstractapi.com/v1/?api_key={keyForEmail}&email={inpemail}")
      dat = reem.json()
      print(dat)
    elif inp == "4":
      infff = input("enter the website to take a screenshot make sure to include the HTTP(S) protocol too: ")
      ss = requests.get(f"https://screenshot.abstractapi.com/v1/?api_key={keyForScreeenShot}&url={infff}")
      screen = ss.content
      
      newfn = input("Enter a name for the screenshot taken (please make sure to add an .jpeg at the end): ")
      with open(newfn,"wb") as file:
        file.write(screen)
        print("made file")
    elif inp == "e":
      break
  except:
    print("something wrong happend")
