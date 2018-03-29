
import os
import sys
import requests
import json
h1url = "https://hackerone.com/"
def getHTML(url):

    
    headers = {"X-Requested-With":"XMLHttpRequest", "accept": "application/json"}
    res = requests.get(h1url+ url, headers=headers)
    #print(res.json()['scopes'])

    for d in res.json()["scopes"]:
        print(d)

if __name__=="__main__":
    try:
        program = sys.argv[1]
    except:
        print ("Usage: python" + sys.argv[0] + " <program>")
    getHTML(program.strip())
