name='A'
num='0'
num_telefonos={}
for x in range (1):
    name=input('Ingrese el nombre del usuario: ')
    num=input('Ingrese el número de telefono del usuario: ')
    num_telefonos[name]={num}
name= input('Ingrese el nombre de usuario, para consultar el numero de telefono: ')
print(num_telefonos[name])
