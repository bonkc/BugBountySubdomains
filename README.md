# BugBountySubdomains

Simple scripts to enumerate bug bounty programs and URLs/subdomains/hosts. Useful for information gathering and hunting. 

Use the information to gather more subdomains, check for subdomain takeovers, delegation, etc. 

DISCLAIMER:

I hold no responsibility for how you use the gathered resources.

May break at any time.

Always follow HackerOne rules and program specific rules.
Always verify the enumerated programs and URLs are in-scope before bug hunting.

Example Usages:

python geth1programs.py > h1programs.txt

python geth1urls.py <programname>

Get URLs from one program.
python geth1urls.py spotify

Get URLs from all programs

for p in $(cat list.txt); do python geth1urls.py $p; done 

Some Usage Ideas:

Create a folder structure with domains
for p in $(cat h1programs.txt); do mkdir ./programs/$p; python geth1urls.py $p > ./programs/$p/domains.txt; done


