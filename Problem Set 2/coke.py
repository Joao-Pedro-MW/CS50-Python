coke,values,flag = 50,int(),True
while coke != 0:
    value = input("Insert a coin: ")
    if (value == "25") or (value == "10") or (value == "5"):
        value = int(value)
        values += value
        coke -= value
        if values > 50:
            print(f"Change owed: {values-50}")
            break
        print(f"Amount due: {coke}")
    else:
        print(f"Amount due: {coke}")