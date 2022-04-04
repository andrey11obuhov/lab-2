import requests
file=requests.get('http://dfedorov.spb.ru/python3/src/romeo.txt')
file=file.text
f=file.replace("\n"," " )
f=f.replace("  ", " ")

f=f.split(' ')
f.remove('')
print(f)
d={i:round(f.count(i)/len(file),3) for i in f}
print(d)