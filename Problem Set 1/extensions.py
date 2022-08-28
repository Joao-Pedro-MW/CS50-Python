user_input = str(input("Input the Value: ")).rsplit(".")
image = ["gif","jpeg","jpg","png"]
application = ["pdf","zip"]
text = ["txt"]
user = (user_input[-1].lower()).strip()
if user in image:
    if user == "jpg":
        user = "jpeg"
    print(f"image/{user}")
elif user in application:
    print(f"application/{user}")
elif user in text:
    print(f"text/plain")
else:
    print("application/octet-stream")