with open("Students.txt", mode = 'r', encoding="utf-8") as f:
    data=f.read()
data=data.split("\n")
data=[i.split(" ") for i in data]
def adding(sur: str, name: str):
    if [sur, name] in data:
        return print("This student is here ")
    for i in data:
        if i[0]> sur:
            data.insert(data.index(i), [sur, name])
        elif i[0]==sur:
            if i[1]>name:
                data.insert(data.index(i), [sur, name])
    if not [sur, name] in data: data.append([sur, name])
    with open("Students.txt", mode='w', encoding="utf-8") as f:
        for i in data:
            f.write("".join(i[0]+" "+i[1]+"\n"))
    return
def find(sur: str, name: str):
    if [sur, name] in data:
        return print("This student is here ")
    else:
        return print("This student isn't in this group ")
def update(sur: str, name:str, newsur:str, newname:str):
    o=0
    if newsur=="" and newname=="": return print("There is nothing to change ")
    elif not[sur, name] in data: return print("This student isn't in this group ")
    elif newsur=="":
        o=data.index([sur, name])
        data[o][1]=newname
        with open("Students.txt", mode='w', encoding="utf-8") as f:
            for i in data:
                f.write("".join(i[0] + " " + i[1] + "\n"))
    elif newname=="":
        o = data.index([sur, name])
        data[o][0] = newsur
        data.sort(key=rtr)
        with open("Students.txt", mode='w', encoding="utf-8") as f:
            for i in data:
                f.write("".join(i[0] + " " + i[1] + "\n"))
    else:
        o = data.index([sur, name])
        data[o][1] = newname
        data[o][0]= newsur
        data.sort(key=rtr)
        with open("Students.txt", mode='w', encoding="utf-8") as f:
            for i in data:
                f.write("".join(i[0] + " " + i[1] + "\n"))
    return
def rtr(d:list):
    return d[0]
def delete(sur: str, name:str):
    if not[sur, name] in data: print("This student isn't here")
    else:
        data.remove([sur, name])
        with open("Students.txt", mode='w', encoding="utf-8") as f:
            for i in data:
                f.write("".join(i[0] + " " + i[1] + "\n"))
    return
delete("b", "bb")
print(data)
