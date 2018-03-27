# BugBountySubdomains

Gather programs from HackerOne using geth1programs.py

Use the programs to enumerate URLs using HackerOne's GraphQL API.

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

