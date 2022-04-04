import requests
file=requests.get('https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/text.txt')
file=file.text
dig=0
up=0
space=0
for i in file.split():
    if i.isupper():
        up+=1
    elif i.isdigit():
        dig+=1
    elif i==" ":
        space+=1
print(up, dig, space)