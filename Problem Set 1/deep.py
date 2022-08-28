respostas = ["42","forty-two","fortytwo"]
user = (str(input("Input the Value: ")).replace(" ","")).lower()
if user in respostas:
    print("Yes")
else:
    print("No")