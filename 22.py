import statistics
import requests
import matplotlib.pyplot as plt

file=requests.get('https://raw.githubusercontent.com/dm-fedorov/python3_intro/master/lesson_10/temper.stat')
file=file.text
file=file.split("\n")
file.remove("")
file=[float(i) for i in file]
print(max(file), min(file), statistics.mean(file))
unique=[]
non=[]
for i in file:
    if i in unique:
        unique.remove(i)
        non.append(i)
    elif not i in non:
        unique.append(i)
print(len(unique))
x=[]
while i!=len(file):
    x.append(i)
    i+=1

plt.plot(x, file)
plt.show()
