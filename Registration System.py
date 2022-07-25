try:
    name = input()
    # your code goes here
    if len(name) < 4:
        raise Exception
    else:
        print("Account Created")
except:
    print("Invalid Name")