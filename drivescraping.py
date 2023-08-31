import lxml.html
import requests
import re
from pprint import pprint
page = requests.get("https://drive.google.com/drive/u/0/folders/1JTSUjJZv2ihedLsb2mD6OXsuAJNzQKAj")
text=str(page.content)
tree = lxml.html.fromstring(page.content)
price = str(tree.xpath('//html/body/script[21]/text()'))
#print(price)


#print(text)
#18VqdbvLK9l3mlKjiYuH6abu1RU9Jq39f
def Convert(string):
    li = list(string.split(" "))
    return li

convert=Convert(price)
chars2remove='''][}{'''
for char in chars2remove:
    price = price.replace(char, '')
data_id_list=[item for item in convert if item.startswith('data:["driveweb;')]

removes=str(data_id_list)
removes=price.replace(",", ' ')
removes=removes.split()

 
# initializing check letter
check = '"'
 
# printing original list

 
# using list comprehension + lower()
# Words starting with specific letter
res = [idx for idx in removes if idx[0].lower() == check.lower()]
res=str(res)

emails = re.findall(r'https://drive.google.com/file/d/+[\w/.-]+', res) ## ['alice@google.com', 'bob@abc.com']
ids=[]
for email in emails:
    # do something with each found email string
    email=email.replace("https://drive.google.com/file/d/","")
    email=email.replace("/view","")
    ids.append(email)
print(ids)
durl = 'https://drive.google.com/uc?export=download&id='+ids[0]
response = requests.get(durl)
with open(ids[0]+".png", "wb") as f:
    f.write(response.content)
#for id in ids:

  #  response =  requests.get(durl)
   # header = response.headers['Content-Disposition']
   # file_name = re.search(r'filename="(.*)"', header).group(1)
   # with open(file_name,'wb') as f:
   #     f.write(response.content)