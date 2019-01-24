#!/usr/bin/python
#print 'Content-type: text/html\n\n'

# The following lines require manual changes
username = "webadmin" # enter your username
password = "P@ssword" # enter your password
# This example establishes a https connection, but doesn't provide the server certificate validation.
# Production code should implement certificate validation.
# -------------------------------------------------
import httplib
import base64
import json


# create HTTP basic authentication string, this consists of
# "username:password" base64 encoded
auth = base64.encodestring("%s:%s"%(username,password))[:-1]
webservice = httplib.HTTPSConnection("devicecloud.digi.com")

# to what URL to send the request with a given HTTP method
webservice.putrequest("GET", "/ws/DataPoint/00000000-00000000-00409DFF-FF63DC12/xbee.serialIn/[00:13:A2:00:41:76:6A:3F]!.json")

# add the authorization string into the HTTP header
webservice.putheader("Authorization", "Basic %s"%auth)

webservice.endheaders()

# get the response
response = webservice.getresponse()
statuscode = response.status
statusmessage = response.reason
response_body = response.read()

# print the output to standard out
json.dumps(response_body)

import webbrowser
new = 2 # open in a new tab, if possible

# open a public URL, in this case, the webbrowser docs
url = "http://docs.python.org/library/webbrowser.html"
webbrowser.open(url,new=new)

# open an HTML file on my own (Windows) computer
url = "file://X:/MiscDev/language_links.html"
webbrowser.open(url,new=new)
