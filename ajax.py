import httplib, urllib, base64

def get_users():
    try:
        conn = httplib.HTTPSConnection('magiclooks.herokuapp.com')
        conn.request("GET", "/users/3/mirrors")
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print(e)


def get_face_ids():

    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': '046cc674fd024894bf21f1f57203d3d7'
    }
    f = open('/home/pi/Desktop/new.jpg', 'rb')
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
        print str(data.split('"')[9])
        conn.close()
    except Exception as e:
        print(e)

#faceId = get_face_ids()
#identify(faceId)
get_users()

