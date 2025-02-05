# Beautiful soup doesn't know how to open a URL it can parse in that onlyy...
# For that we'll use "requests" module
# For understanding latest version of html we use html5lib
# bs4 - Beautiful soup library

import requests
from bs4 import BeautifulSoup
import html5lib

# For opening a url

response = requests.get('https://en.wikipedia.org/wiki/Fallacy')

print(response.status_code)   # for checking whether the page is responsive or not

# print(response.content)

# Syntax: BeautifulSoup(content,'parselib')
soup = BeautifulSoup(response.content,'html5lib')

# print(soup)

# print(soup.prettify())


## ---> How to get the information we want particularly


# soup.find(tag_name,attrs)
table_of_content = soup.find("ul",attrs={"id":"mw-panel-toc-list"})

# print(table_of_content)

list_text = table_of_content.find_all("div",attrs={"class":"vector-toc-text"})  # we can use soup.find_all also

# print(list_text)

# for i in list_text:
#     print(i.text.strip())    # .text means which is inside that div 

# for i in list_text:
#     print(i.span)

# # For just printing that content without letters

for i in list_text:
    value = i.text.lstrip()

    for char in value:
        if char.isnumeric() or char=='\t' or char=='\n':
            continue
        elif char=='.':
            print("",end='\t')
        else:
            print(char,end="")
    print()
