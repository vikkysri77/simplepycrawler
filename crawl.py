import urllib.request
import re

print("Paste the URL: " )

#GET THE INPUT URL
inputUrl = input()

#SEND A REQUEST TO THE ENTERED URL
contents = urllib.request.urlopen(inputUrl).read().decode("utf-8")

#GENERATE A REGEX PATTERN THAT STARTS WITH <a & ENDS WITH </a>
regex= re.compile("<a.*</a>")

#APPLY THE REGEX PATTERN ON THE RETREIVED HTML CONTENT
match = re.findall(regex, contents)

#PRINT OUT THE LIST OF LINKED URLS
for link in match:
    regex2 = re.compile("\"http.*\"")
    match2 = re.findall(regex2,link)
    if match2:
        print (*match2, sep="/n")
