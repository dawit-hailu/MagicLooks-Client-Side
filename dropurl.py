import json
import dropbox
import datetime
import requests

suffix = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
filename = "image-" + suffix + ".jpg"
 
client = dropbox.client.DropboxClient('FMaIIK2lHrAAAAAAAAAACX6-g31v4l6G3PLKlgjpPSMoJDA_F__Uefuo9x--ckYA')
f = open('/home/pi/Desktop/image.jpg', 'rb')
response = client.put_file(filename, f)
print "uploaded:", response

