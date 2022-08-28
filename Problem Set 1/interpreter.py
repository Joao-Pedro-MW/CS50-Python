expression = str(input("Informe a expressão: ")).split()
v1,opt,v2 = float(expression[0]),expression[1],float(expression[2])
if opt =="*": result = v1 * v2
if opt =="+": result = v1 + v2
if opt =="/": result = v1 / v2
if opt =="-": result = v1 - v2
print(result)