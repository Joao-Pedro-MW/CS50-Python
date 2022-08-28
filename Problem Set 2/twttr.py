txt = input("Input: ")
char = ["a","A","e","E","i","I","o","O","u","U"]
for i in char:txt = txt.replace(i,"")
print(txt)