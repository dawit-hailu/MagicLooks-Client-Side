import httplib, urllib, base64, json, picamera,time, RPi.GPIO as GPIO


def signIn(personId):
    try:
        headers = {
            'Content-Type': 'application/json'
        }

        body = '{"personId":"'+ personId +'"}'        
        conn = httplib.HTTPSConnection('magiclooks.herokuapp.com')
        conn.request("PUT", "/mirrors/1", body, headers)
        response = conn.getresponse()
        data = response.read()
        print(json.loads(data)["status"])
        conn.close()
    except Exception as e:
        print(e)

def signOut():
    try:
        conn = httplib.HTTPSConnection('magiclooks.herokuapp.com')
        conn.request("DELETE", "/mirrors/1")
        response = conn.getresponse()
        data = response.read()
        print(json.loads(data)["status"])
        conn.close()
    except Exception as e:
        print(e)


def getFaceId():

    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': '046cc674fd024894bf21f1f57203d3d7'
    }
    with picamera.PiCamera() as camera:
        camera.rotation = 90
        camera.capture('image.jpg')
    camera.close()
    
    f = open('/home/pi/Desktop/image.jpg', 'rb')
    body = f.read()

    f.close()
    
    try:
        conn = httplib.HTTPSConnection('api.projectoxford.ai')
        conn.request("POST", "/face/v1.0/detect?returnFaceId=true&returnFaceLandmarks=false", body, headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return str(data.split('"')[3])

    except Exception as e:
        print(e)

def identify(faceId):

    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '046cc674fd024894bf21f1f57203d3d7'
    }
    body = '{"personGroupId":"magiclooks","faceIds":['+ '"' + faceId + '"' +'],"maxNumOfCandidatesReturned":1,"confidenceThreshold":0.5}'
    
    params = urllib.urlencode({
    })
    
    try:
        conn = httplib.HTTPSConnection('api.projectoxford.ai')
        conn.request("POST", "/face/v1.0/identify?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        return str(data.split('"')[9])
        conn.close()
    except Exception as e:
        print(e)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.IN)
while True:
    i=GPIO.input(37)
    if i==0:
        print "No intruders",i
        time.sleep(0.5)
    elif i==1:
        print "intruder detected",i
        signOut()
        faceId = getFaceId()
        personId = identify(faceId)
        signIn(personId)
        time.sleep(2)



