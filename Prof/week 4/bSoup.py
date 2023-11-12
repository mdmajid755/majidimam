from bs4 import BeautifulSoup
import requests

searchTerm = input("enter search term: ")
myParams = {"q": searchTerm}
r = requests.get('https://search.yahoo.com/search', myParams)

soup = BeautifulSoup(r.text, "html.parser")
#print(soup.prettify)

results = soup.find("ol",{"class" : "searchCenterMiddle"})
divs = results.find_all("div",{"class": "algo-sr"})

for div in divs:
    a = div.find("a")
    #print(a.attrs)
    link_text = a.attrs["aria-label"]
    link_href = a.attrs["href"]

    if link_text and link_href:
        print("-----------------------------------")
        print(link_text)
        print(link_href +"\n")
        if div.next_sibling:
            print ("next Sib: \n" + div.next_sibling.text + "\n")
        
        if div.previous_sibling:
            print ("Previous Sib: \n" + div.previous_sibling.text + "\n")


    targetParent = a.parent.parent.parent

    topDiv = targetParent.find('div', {'class': 'compText'})
    if topDiv:
        print(topDiv.text + "\n")

    # pChildrenList = targetParent.children
    # for child in pChildrenList:
    #     print(child.name)    
    # print()