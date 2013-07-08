
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

		self.open = [start]
		self.closed = []

		self.way = []

	def showOpen(self):
		print self.open

	def showClosed(self):
		print self.closed

def neighbors(nodo):

	board = nodo.board
	point = nodo.open[0]
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



b1 = [0,0,0,0]
b2 = [0,0,0,0]
b3 = [0,0,0,0]
board = [b1,b2,b3]

p1 = Point(0,1)
p2 = Point(2,3)

nodo = Nodo(p1,p2,board)

vecinos = neighbors(nodo)

def showList(vecinos):
	for x in range (len(vecinos)):
		vecinos[x].show()


def gotPoint(point,closed):
	for x in range(len(closed)):
		aux = closed[x]
		if(aux.x==point.x and aux.y==point.y):
			return True
	return False



def aStar(nodo):

	while(len(nodo.open)!=0):

		pointNow = nodo.open[0]
		showList(nodo.open)

		if(pointNow.x == nodo.end.x and pointNow.y == nodo.end.y):
			return pointNow
		
		else:
			vecinos = neighbors(nodo)
			nodo.closed = nodo.closed+[pointNow]
			

			newPoints = []

			for x in range(len(vecinos)):
				if(gotPoint(vecinos[x],nodo.closed)):
					pass
				else:
					newPoints = newPoints + [vecinos[x]]
			print 'nuevos puntos'
			showList(newPoints)
			nodo.open = nodo.open+newPoints
			nodo.open = nodo.open[1:len(nodo.open)-1]

	print 'terminado'


print 'EMPEZANDO'
aStar(nodo)






