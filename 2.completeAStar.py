import math 

# ---------------------------------------------------------------
# COMENTARIOS:
#	- Un tablero sin obstaculos no representa una situacion real
# 	  por lo que para marcar posibles obstaculos que entorpezcan
#	  el camino, utilizaremos 1's en el mapa en lugar de 0's
# 	  (modificaciones: 
#			variable: board,
#			funcion:  neighbors() )
#   - Por otro lado, el algoritmo es poco eficiente, ya que 
#	  contempla todos los nodos tal y como van apareciendo antes
# 	  antes de encontrar una solucion optima. Esto puede tratar
#	  de reducirse haciendo uso de alguna funcion heuristica que
# 	  ordene los nodos segun el que tenga mas probabilidades de
# 	  llegar antes a una solucion.
#	  (nuevo:
#			funcion: g()
#			funcion: f()
#			funcion: h() )
#
#
#
#	  (otras modificaciones:
#		 - se ha modificado el resultado por defecto el algoritmo,	  
#		   ahora devuelve False en lugar del ultimo nodo visitado.
#		 - se ha modificado la forma de mostrar el resultado por 
#		   pantalla, ahora si no hay camino, no da error.
#		 - se ha modificado el algoritmo, ahora ordena la lista
#		   de nodos abiertos al final de cada iteracion.
# ---------------------------------------------------------------


class Point():

	def __init__(self,x,y):

		self.x = x
		self.y = y

	def show(self):

		print '['+str(self.x)+','+str(self.y)+']'


class Nodo():

	def __init__(self,start,end,board):

		self.start = start
		self.end = end
		self.board = board

		self.hist = [start]


# VERSION ANTIGUA
def oldNeighbors(nodo):

	board = nodo.board
	point = nodo.start
	exit = []

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

# ---------------------------------------------------------------
# NUEVA VERSION
def neighbors(nodo):

	board = nodo.board
	point = nodo.start
	exit = []

	for x in range (-1,2):
		for y in range (-1,2):

			if(point.x+x>-1 and point.x+x<len(board) and
				point.y+y>-1 and point.y+y<len(board[0]) and
				  board[point.x+x][point.y+y]!=1):
				
				if(x==0 and y==0):
					pass
				else:
					aux = [Point(point.x+x,point.y+y)]
					exit = exit + aux
	return exit


# Funcion que nos devuelve el numero de pasos que llevamos dados
def g(nodo):
	return len(nodo.hist)

# Funcion que nos devuelve la distancia euclidea entre el punto final
# y el punto en el que estamos actualmente
def f(nodo):
	
	# Aunque la distancia euclidea se defina como la raiz cuadrada de las
	# las diferencias, es usual no calcular la raiz cuadrada en beneficio
	# del tiempo de ejecucion
	# return math.sqrt(abs(nodo.end.x-nodo.start.x) + abs(nodo.end.y-nodo.start.y))
	return abs(nodo.end.x-nodo.start.x) + abs(nodo.end.y-nodo.start.y)

	
# Funcion que devuelve la suma de los resultados de la funcion 'f' y 'g'
def h(nodo):
	return f(nodo)+g(nodo)

def minHeuristic(lista):
	res = 0
	heu = h(lista[0])

	for x in range(1,len(lista)):
		
		if(heu>h(lista[x])):
			
			res = x
			heu = h(lista[x])
	return res


def sortNode(lista):

	res = []
	listaAux = lista

	while(len(listaAux)!=0):

		aux = minHeuristic(listaAux)
		res = res + [listaAux[aux]]
		listaAux1 = listaAux[0:aux]
		listaAux2 = listaAux[aux+1:len(listaAux)] 
		listaAux = listaAux1 + listaAux2

	return res



# ---------------------------------------------------------------

def showNodeHeuristicList(lista):
	for x in range(len(lista)):
		print h(lista[x])

def showNodePointList(lista):
	for x in range(len(lista)):
		print lista[x].start.show()

def showPointList(vecinos):
	for x in range (len(vecinos)):
		vecinos[x].show()

def gotNode(point,closed):
	for x in range(len(closed)):
		aux = closed[x]
		if(point.x == closed[x].start.x and
			point.y == closed[x].start.y):
			return True
	return False


def aStar(nodo):

	openList = [nodo]
	closedList = []

	while(len(openList)!=0):

		currentNode = openList[0]

		if(currentNode.start.x == currentNode.end.x and
			currentNode.start.y == currentNode.end.y):
			
			return currentNode

		else:

			closedList = closedList + [currentNode]

			openList = openList[1:len(openList)]

			newPoints = neighbors(currentNode)
			
			for x in range(0,len(newPoints)):
				if(gotNode(newPoints[x],closedList)):
					pass
				else:
					if(gotNode(newPoints[x],openList)):
						pass
					else:
						
						hist = currentNode.hist + [newPoints[x]]

						nodeAux = Nodo(newPoints[x],currentNode.end,currentNode.board)
						nodeAux.hist = hist
						
						openList = openList + [nodeAux]

		# Ordenamos la lista de posibles nodos segun sus heuristicas
		# usando la funcion sortNode()
		openList = sortNode(openList)

	# Modificado
	return False



# ------------------------------------------------------
# Pruebas realizadas
# ------------------------------------------------------

# Definicion del tablero 

b1 = [0,0,0,0,0]
b2 = [0,1,1,1,0]
b3 = [0,1,0,0,0]
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
if(res!=False):
	for x in range(0,len(res.hist)):
		res.hist[x].show()
else:
	print 'No existe ningun camino'







