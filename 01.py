country = input("your country : ")
age = int(input('your age : '))

if country == '台灣' | country == "Taiwan":
    if age >= 18:
        print("you can drive")
    else:
        print("you can't drive")

elif country == "美國" | country == "US":
    if age >= 16:
        print("you can drive")
    else: 
        print("you can't drive")