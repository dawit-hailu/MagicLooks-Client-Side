-params = urlib.urlcode({'subscription-key': "b998f46254d94b73b2125c9121b0e5f7",
    'analyzesFaceLandmarks': 'true',

}) 

    headers = {

        'Content-type': 'application/octet-stream',

    }

    body = "" 

    filename = 'C:/testPicutre.JPG'

    f = open('/home/pi/Desktop/image.jpg', 'rb')
    body = f.read()

    f.close()

    conn = httplib.HTTPSConnection('api.projectoxford.ai')

    conn.request("POST", "/face/v0/detections?%s" % params, body, headers)

    response = conn.getresponse("")

    data = response.read()

    print(data)

    conn.close()
