

# ---------------------------------------------------------------
# COMENTARIOS:
#	- Algoritmo de búsqueda en profundidad iterativa modificado.
#	  En la version previa, la busqueda iterativa se realizaba de
#	  una forma 'no informada', contemplando la profundidad del 
#	  arbol de decision como medio para iterar. En esta version 
#	  'informada', se utiliza el valor de la heuristica de cada 
# 	  nodo base de la iteracion como tope, de modo que si en algun
#	  momento, el valor de alguno de los nodos sucesores supera
# 	  el valor actual de la heuristica, se termina con la ejecucion 
#	  del algoritmo y se empieza con la mayor de las heuristicas 
#	  que lo sobrepasen.
#	- (Otros comentarios:
#	  	Menor rapidez a la hora de encontrar un camino optimo
#		Algoritmo completo
#		Problemas a la hora de parar en caso de no existir ningun
#		camino posible
#			 *** SEGUIMOS TENIENDO QUE DISCUTIR ESTE TEMA***
#		Menor coste de memoria 
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
		# self.it = 0

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


def depthAStar(nodo):

	openList = [nodo]
	closedList = []

	while(len(openList)!=0):

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

# ---------------------------------------------------------------

# Funcion auxiliar para saber si la heuristica de algun nodo excede 
# el limite pasado por parametro
def existsLimit(lista,heu):
	for x in range (len(lista)):
		if(h(lista[x]) > heu):
			return True
	return False

# Funcion auxiliar para averiguar la heuristica mas alta de una lista
# de nodos
def maxHeuristic(lista):
	res = 0
	for x in range(len(lista)):
		aux = h(lista[x])
		if(aux>res):
			res = aux
	return res

# Funcion auxiliar para 
def minMaxHeuristic(lista,heu):
	res = maxHeuristic(lista)
	for x in range(len(lista)):
		aux = h(lista[x])
		if(aux < res and aux > heu):
			res = aux
	return res


def iterativeDepthAStarAux(nodo,heu):

	openList = [nodo]
	closedList = []
	

	while(len(openList)!=0):

		currentNode = openList[len(openList)-1]		

		if(currentNode.start.x == currentNode.end.x and
			currentNode.start.y == currentNode.end.y):
			
			return currentNode

		else:

			closedList = closedList + [currentNode]

			openList = openList[0:len(openList)-1]

			newPoints = neighbors(currentNode)

			# Lista auxiliar para guardar los nuevos nodos que obtenemos
			# en cada iteracion.
			newNodes = []

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

						# Añadimos a la lista auxiliar todos los nuevos
						# nodos que vamos obteniendo
						newNodes = newNodes + [nodeAux]

			# Si algun nodo, tiene heurisitca superior a la pasada por
			# parametro, paramos la iteracion y devolvemos el minimo
			# de los valores que sobrepasan la heuristica actual.
			# Sino, agregamos a abiertos todos los nuevos nodos.
			if(existsLimit(newNodes,heu)):
				return minMaxHeuristic(newNodes,heu)
			else:
				openList = openList + newNodes


		
	return False


def iterativeDepthAStar(nodo):

	# Heuristica base para la primera iteracion.
	heu = h(nodo)

	res = 0
	
	# Iteramos mientras la variable res no sea una instancia de la
	# clase Nodo (vease, el algoritmo siga devolviendo un valor).
	while(not isinstance(res,Nodo)):

		# Llamada al algoritmo auxiliar que recibe el valor de la 
		# heuristica como uno de sus parametros.
		res = iterativeDepthAStarAux(nodo,heu)

		# Actualizamos el valor de res para que, en caso de que sea un valor
		# lo utilicemos como nueva heuristica en la siguiente iteracion.
		heu = res

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







