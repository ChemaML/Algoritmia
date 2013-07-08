# ---------------------------------------------------------------
# COMENTARIOS:
#	- Primera implementacion del algoritmo A* o 'A estrella'.
#	- Se trata de una implementacion de una estructura muy basica
#	- sobre la que trabajar comodamente mas adelante.
# 	- No se han tenido en cuenta la posibilidad de obstaculos en 
#	  el tablero utilizado, siendo una estructura plana la
#	  utilizada para las pruebas.
#	- No se ha tenido en cuenta ningun tipo de heuristica que 
#	  ayude a la consecucion del problema.
# ---------------------------------------------------------------



# Representacion de cada uno de los puntos del tablero usando
# una estructura 'Punto' con campos 'x' e 'y' acordes a las 
# coordenadas de la matriz utilizada para la representacion
# del medio

class Point():

	def __init__(self,x,y):

		self.x = x
		self.y = y

	def show(self):

		print '['+str(self.x)+','+str(self.y)+']'

# Representacion de cada uno de los pasos parciales que da el 
# algoritmo de busqueda mediante:
# At. start: punto asociado en el que se haya el problema parcial
# At. end: punto final o meta del problema
# At. board: array bidimensional utilizado para la representacion
# 			representacion del medio
# At. hist: historial de puntos por los que ha pasado el problema
#			hasta llegar al punto actual

class Nodo():

	def __init__(self,start,end,board):

		self.start = start
		self.end = end
		self.board = board

		# Inicializamos el historial con una lista donde el unico
		# termino con el que empezara, es el punto inicial del
		# problema
		self.hist = [start]


# Funcion utilizada para encontrar los posible sucesores de un nodo
# Los sucesores de un nodo son aquellos puntos que se encuentran 
# adyacentes al punto en el que se encuentra el problema (nodo.start)

def neighbors(nodo):

	board = nodo.board
	point = nodo.start
	exit = []

	# Recorremos todos los posibles puntos alrededor del punto dado
	# usando un doble bucle desde -1 a 1 sumando para cada componente
	# ambos terminos
	#
	# Un ejemplo grafico del recorrido que hacemos sobre los vecinos
	# puede ser el siguiente:
	#
	# 0 0 0 0 0		0 0 0 0 0
	# 0 0 0 0 0 	0 1 2 3 0
	# 0 0 X 0 0  -> 0 4 X 5 0
	# 0 0 0 0 0		0 6 7 8 0
	# 0 0 0 0 0		0 0 0 0 0
	#
	# A priori, todos los puntos adyacentes al dado, que se encuentren
	# dentro del tablero, son considerados como posibles sucesores

	for x in range (-1,2):
		for y in range (-1,2):

			if(point.x+x>-1 and point.x+x<len(board) and
				point.y+y>-1 and point.y+y<len(board[0])):
				
				if(x==0 and y==0):
					pass
				else:
					aux = [Point(point.x+x,point.y+y)]
					exit = exit + aux
	return exit

# Funcion utilizada para realizar un seguimiento de la traza del 
# problema a la hora de su implementacion. Dada una lista de puntos
# ejecuta la funcion show() propia de la clase punto para mostrarlos
# por pantalla

def showList(vecinos):
	for x in range (len(vecinos)):
		vecinos[x].show()

# Funcion utilizada para el filtrado de puntos en una lista de nodos
# devolviendo verdadero si alguno de los nodos de la lista esta en
# un punto del problema equivalente al punto pasado como parametro

def gotNode(point,closed):
	for x in range(len(closed)):
		aux = closed[x]
		if(point.x == closed[x].start.x and
			point.y == closed[x].start.y):
			return True
	return False


def aStar(nodo):

	# Lista de nodos en cola por visitar
	openList = [nodo]
	# Lista de nodos que ya han sido visitados
	closedList = []

	# Bucle principal
	while(len(openList)!=0):

		# Nodo actual sobre el que se trabaja en cada iteracion
		# En una primera aproximacion usaremos el primero de la
		# lista de abiertos
		currentNode = openList[0]

		# Condicion de parada: punto inicial = punto final
		if(currentNode.start.x == currentNode.end.x and
			currentNode.start.y == currentNode.end.y):
			
			# Si se cumple la condicion, dejmos de iterar
			break

		else:

			# Agregamos el nodo actual a la lista de nodos visitados
			closedList = closedList + [currentNode]

			# Eliminamos el primer termino de la lista de abiertos
			openList = openList[1:len(openList)]

			# Hallamos los posibles nodos a los que podemos accede
			# desde el punto actual
			newPoints = neighbors(currentNode)
			

			# Para cada termino en 'nuevosPuntos', si no existe algun 
			# nodo en la lista de abiertos o cerrados que lo contenga,
			# lo agregamos a la lista de abiertos para estudiarlo mas
			# adelante
			for x in range(0,len(newPoints)):
				if(gotNode(newPoints[x],closedList)):
					pass
				else:
					if(gotNode(newPoints[x],openList)):
						pass
					else:
						
						# Modificamos el historial de nodos visitados
						# agregando el nodo actual a la lista
						hist = currentNode.hist + [newPoints[x]]

						# Creamos un nuevo nodo con los datos actualizados
						nodeAux = Nodo(newPoints[x],currentNode.end,currentNode.board)
						nodeAux.hist = hist

						# Agregamos el nuevo nodo a la lista de abiertos
						openList = openList + [nodeAux]

	return currentNode

# ------------------------------------------------------
# Pruebas realizadas
# ------------------------------------------------------

# Definicion del tablero 

b1 = [0,0,0]
b2 = [0,0,0]
b3 = [0,0,0]
board = [b1,b2,b3]

# Punto inicial
pInicio = Point(0,0)

# Punto final
pFin = Point(2,2)

# Variable nodo sobre la que ejecutar el algoritmo
nodo = Nodo(pInicio,pFin,board)


print 'EMPEZANDO'
res = aStar(nodo)

# Mostramos la lista de nodos recorridos hasta llegar al punto final
print 'RESULTADO'
for x in range(0,len(res.hist)):
	res.hist[x].show()






