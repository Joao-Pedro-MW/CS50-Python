user = (str(input("Como você foi cumprimentado? ")).lower()).strip()
user = user[0:6]
if "hello" in user:
    print("$0")
elif user[0] == "h":
    print("$20")
else:
    print("$100")
