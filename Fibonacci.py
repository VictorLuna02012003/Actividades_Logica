#Serie de el fibonacci, que muestre los primeros 50 numeros
#x = 0
#y = 0
#z = 1

#elementos = []
#while len(elementos)<=50:
#    elementos.append(x)
#    x = y + z 
#    y = z
#    z = x  
#
#
#for i in elementos:
#    print(i)

x = 0
y = 1

for i in range(50):
    print(x)
    temp = x
    x = y
    y = temp + x