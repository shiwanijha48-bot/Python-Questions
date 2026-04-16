un_pw = {"john": "j123", "mary" : "m456", "tom":"t897","ken":"k427","harry":"h546"}
un_br = {"john": "CSE", "mary" : "CSE", "tom":"AIML","ken":"AIML","harry":"CY"}
# ------------- two ways of storing student name and branch of their course------------
di = {"john": ["j123", "CSE"], "mary" : ["m456","CSE"],  "tom":["t897", "AIML"],"ken":["k427", "AIML"],"harry":["h546", "CY"]}
username = input("Enter your Username:")
if username in di:
    password = input("Enter your Password:")
    if password in di[username][0]:
        branch = input("Enter your Branch:")
        if branch in di[username][1]:
            if branch == "CSE":
                print("Welcome to branch CSE")
            elif branch == "AIML":
                print("Welcome to branch AIML")
            elif branch == "CY":
                print("Welcome to branch CY")
        else:
            print("Branch not found")
    else:
        print("Password is not correct")
else:
    print("Invalid Username")
