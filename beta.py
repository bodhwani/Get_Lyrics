import urllib.request
req = urllib.request.Request("http://savemedia.com/watch?v=XCWmONajkOg&list=RDMMXCWmONajkOg")
response = urllib.request.urlopen(req)
print(response.read())
