import os
import sys
import requests
import json
import tldextract

programs = []

def getHTML(url):

        headers = {"X-Requested-With":"XMLHttpRequest", "accept": "application/json"}
        html = requests.get(url, headers=headers)
        safe_html = (html.text).encode('cp850',errors='replace')
        return (safe_html)


def getPrograms(pages):
    for x in range(1,pages):
            res = getHTML("https://hackerone.com/programs/search?query=bounties%3Ayes&sort=published_at%3Adescending&page=" + str(x))
            split = res.split(",")
            #jhtml = json.loads(safe_html)
            for parts in split:
                if '"url"' in parts:
                    programs.append((parts).split(":")[1].strip('"'))


if __name__ == "__main__":
    getPrograms(6)
    for program in programs:
        print (program.strip("/"))
