import httplib, urllib, base64

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': 'b998f46254d94b73b2125c9121b0e5f7',
}

params = urllib.urlencode({
    # Request parameters
    'returnFaceId': 'true'
})

f = open('/home/pi/Desktop/image.jpg', 'rb')
body = f.read()

f.close()

try:
    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print(e)
