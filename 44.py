import requests
import random
file=requests.get('https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/responses.txt')
file=file.text
file=file.split("\n")
print("If you want to end session, write stop ")
i=0
while i==0:
    print("Ask your question ")
    s=input()
    if s=="stop":
        print("Good luck!")
        break
    print(random.choice(file))
