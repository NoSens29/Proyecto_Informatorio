class contacto():
	def __init__(self,nombre,telefono,email):
		self.nombre=nombre
		self.telefono=telefono
		self.email=email
#solucion 2
#metodo
	def aniadir(self):
		agenda[self.nombre]= [self.telefono,self.email]	

class Agenda:
	def __init__(self):
		self.lista_de_contactos= []
	def aniadir(self,contacto):
		self.lista_de_contactos.append(contacto)

agenda= Agenda()			
agenda.aniadir(contacto)

agenda2= Agenda()
agenda2.actualizar(contacto)

nombre_usuario= input('Nombre: ')
telefono_usuario= input('Telefono:')
email_usuario= input('email: ')

registro= contacto(nombre_usuario,telefono_usuario,email_usuario)
registro.aniadir()
#solucion 1
#funcion
'''
def aniadir(datos):
	agenda[datos.nombre]= [datos.telefono,datos.email]

aniadir(registro)
