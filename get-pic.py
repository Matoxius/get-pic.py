#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import requests
import shutil
from datetime import datetime
from datetime import date

while True:
#set time, cam-url, filename
    now = datetime.now() #var for time
    current_time = now.strftime("%d.%m.%Y-%H%M%S") #time
    image_url = "https://urlofmy.stream/live" #URL to webcam
    filename = current_time+".jpg" #nameing the file

    #open the URL and scrape the picture
    r = requests.get(image_url, stream = True)

    #checks for success
    if r.status_code == 200:
    # set decode_content to True
        r.raw.decode_content = True

    #open folder /ssd/cam/ with write access 
        with open('/ssd/cam/'+filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
        #check for success
        print("picture retrieved: " + filename)
        print("\nnext picture in 15 seconds\n")
    time.sleep(15) #sleep 15 seconds
else:
    print("picture could not be retrieved...")
exit()
