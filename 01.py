country = input("your country : ")
age = int(input('your age : '))

if country == '台灣':
    if age >= 18:
        print("you can drive")
    else:
        print("you can't drive")