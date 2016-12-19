import httplib, urllib, base64

try:
    conn = httplib.HTTPSConnection('magiclooks.herokuapp.com')
    conn.request("GET", "/users/3/mirrors")
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print(e)
