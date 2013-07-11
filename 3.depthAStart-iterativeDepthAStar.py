

# ---------------------------------------------------------------
# COMENTARIOS:
#	- Algoritmo modificado para que realice una busqueda en profundidad
#	  en lugar de una busqueda en anchura 'depthAStar'. El unico cambio
#	  importante en el algoritmo es que en lugar de coger el primer 
#	  termino de la lista de nodos abiertos, se coge el ultimo agregado
#	- Por otro lado, tambien se implementado una version iterativa de 
#	  este mismo algoritmo 'iterativeDepthAStar', en el que se van
#	  estudiando, de forma iterativa y con busqueda en profundidad,
#	  los distintos niveles del algoritmo
#	  (Observaciones:
#			1. Para ello, se ha agregado un campo 'it' a la clase Nodo
#			de modo que se pueda llevar la cuenta de cuantas veces se
# 			pueden expandir los hijos de dicho nodo en cada iteracion	
#	  		2. Este algoritmo no es muy fiable, ya que de no existir
#			camino ninguno entre el punto de partida y el final, el
#			propio algoritmo seguiria aumentando la cota de profundidad,
#			y por tanto ejecutandose infinitamente)
#
#		###TENEMOS QUE HABLAR DE ESTE ASUNTO###
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

# ---------------------------------------------------------------

		# Agregado
		self.it = 0

# ---------------------------------------------------------------


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


def g(nodo):
	return len(nodo.hist)

def f(nodo):
	
	return abs(nodo.end.x-nodo.start.x) + abs(nodo.end.y-nodo.start.y)

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

# ---------------------------------------------------------------

def depthAStar(nodo):

	openList = [nodo]
	closedList = []

	while(len(openList)!=0):

		# En lugar de coger el primer valor de la lista de nodos
		# por explorar, cogemos el ultimo que haya entrado
		currentNode = openList[len(openList)-1]	

		print 'Current'	
		currentNode.start.show()

		if(currentNode.start.x == currentNode.end.x and
			currentNode.start.y == currentNode.end.y):
			
			return currentNode

		else:

			closedList = closedList + [currentNode]

			# Borramos de la lista el ultimo valor
			openList = openList[0:len(openList)-1]

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

	return False


# Funcion auxiliar que empieza el algoritmo con un numero 'ite' de
# niveles de profundidad posibles por explorar
def iterativeDepthAStarAux(nodo,ite):

	openList = [nodo]
	closedList = []
	depth = ite

	# Numero de iteraciones pendientes/posibles
	nodo.it = depth

	while(len(openList)!=0):

		currentNode = openList[len(openList)-1]		

		if(currentNode.start.x == currentNode.end.x and
			currentNode.start.y == currentNode.end.y):
			
			return currentNode

		else:

			closedList = closedList + [currentNode]

			openList = openList[0:len(openList)-1]

			# Si no quedan iteraciones por evaluar en el nodo
			# actual, no buscamos sus puntos adyacentes
			if(currentNode.it>0):

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

							# Agregamos el valor de la iteracion actual
							# reduciendola en una unidad
							nodeAux.it = currentNode.it-1

							openList = openList + [nodeAux]

		
	return False


# Funcion base para la llamada del algoritmo recursivo
# Esta funcion se encargara de empezar a iterar el algoritmo empezando
# por un numero de profundidades posibles igual a 1 e incrementandolo 
# en caso de que no haya solucion
def iterativeDepthAStar(nodo):

	res = False 
	nIterations = 1

	while(res==False):

		# Llamada al algoritmo auxiliar que recibe el numero de iteraciones
		# como uno de sus parametros
		res = iterativeDepthAStarAux(nodo,nIterations)
		nIterations +=1

	return res

# ---------------------------------------------------------------






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
res = iterativeDepthAStar(nodo)


# Mostramos la lista de nodos recorridos hasta llegar al punto final
print 'RESULTADO'
if(res!=False):
	for x in range(0,len(res.hist)):
		res.hist[x].show()
else:
	print 'No existe ningun camino'







