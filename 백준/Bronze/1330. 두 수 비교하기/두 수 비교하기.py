a = input().split(" ")
if int(a[0]) > int(a[1]):
    print(">")
elif int(a[0]) < int(a[1]):
    print("<")
elif int(a[0]) == int(a[1]):
    print("==")