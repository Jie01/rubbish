country = input("your country : ")
age = int(input('your age : '))

if country == "台灣" or country == "TW":
    if age >= 18:
        print("you can drive")
    else:
        print("you can't drive")

elif country == "美國" or country == "US":
    if age >= 16:
        print("you can drive")
    else: 
        print("you can't drive")