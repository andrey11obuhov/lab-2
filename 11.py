a= input("write 1 number ")
b=input("write 2 number ")
op= input("Write operator ")
if op=="/":
        try:
            print(int(a)/int(b))
        except ValueError:
            print( " There is a mistake in numbers ")
        except ZeroDivisionError:
            print("You can't divide on zero")
elif op=="+":
        try:
            print(int(a)+int(b))
        except ValueError:
            print( " There is a mistake in numbers ")
elif op=="-":
        try:
            print(int(a)-int(b))
        except ValueError:
            print( " There is a mistake in numbers ")
