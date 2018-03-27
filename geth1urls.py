import os
import sys
import requests
import json
import tldextract


def cleanURL(url):
    return ('.'.join(tldextract.extract(url.encode('cp850',errors='replace')))) 

def query (program):
    url = "https://hackerone.com/graphql"

    query = "query Team_assets($first_0:Int!) {query {\n    id,\n    ...F0\n  }\n}\nfragment F0 on Query {\n  _team:team(handle:\"" + program +"\") {\n    handle,    _structured_scopes:structured_scopes(first:$first_0,archived:false,eligible_for_submission:true) {\n      edges {\n        node {\n                   asset_type,\n          asset_identifier }     },\n   },\n   },\n  id\n}"
    headers = {"X-Requested-With":"XMLHttpRequest", "accept": "application/json"}
    html = requests.post(url, json = {"query":query,"variables":{"first_0":100,"first_1":50}}
    , headers=headers)
    try:
        for d in html.json()["data"]["query"]["_team"]["_structured_scopes"]["edges"]:
            if (d["node"]["asset_type"] == "URL"):
                print cleanURL((d["node"]["asset_identifier"].strip()))
    except Exception as e:
        print ("error: " + str(e))
        print(program + " program doesn't exist")
        pass


if __name__ == '__main__':
    try:
        program = sys.argv[1]
    except:
        print ("Usage: python" + sys.argv[0] + " <program>")
    query(program.strip())
