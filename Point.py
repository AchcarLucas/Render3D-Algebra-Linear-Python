'''
	Módulo C_Point
	C_Point é a Classe Responsável para a Manipulação de Pontos na Tela
'''

import pygame

class C_Point:
	def __init__(self, point=[0, 0, 0], factor = 100., color = (0, 0, 0), scale = 4.0):	
		'''
			Função construct (Inicia todas as variáveis necessárias para a utilização da classe C_Point)
			Args:
				None
			Return:
				None
		'''

		# ponto original
		self.point =	[
								[point[0]], [point[1]], [point[2]], [1]
						]
		# faz uma cópia do ponto para possível consulta
		self.copy_point = self.point.copy()

		self.factor = factor
		self.color = color
		self.scale=scale

		self.screenSize = pygame.display.get_window_size()
		
	def render(self, screen):
		'''
			Função responsável por renderizar o ponto na tela utilizando as transformações lineares
			Args:
				c_draw: Instância da classe C_Draw
			Return:
				None
		'''

		pygame.draw.circle(screen, self.color, [int(self.getScreenX()),  int(self.getScreenY())], int(self.scale), 0)
		
	'''
		Funções getters e setters
	'''

	def getFactor(self):
		return self.factor

	def getX(self):
		return self.point[0][0]
		
	def getY(self):
		return self.point[1][0]
		
	def getZ(self):
		return self.point[2][0]

	def getScreenX(self):
		return self.getX() * self.factor + (self.screenSize[0] / 2)
		
	def getScreenY(self):
		return self.getY() * self.factor + (self.screenSize[1] / 2)
		
	def getScreenZ(self):
		return self.getZ() * self.factor

	def getCopyScreenX(self):
		return self.copy_point[0][0]
		
	def getCopyScreenY(self):
		return self.copy_point[1][0]
		
	def getCopyScreenZ(self):
		return self.copy_point[2][0]
		
	def setScreenX(self, x):
		self.point[0][0] = x
		
	def setScreenY(self, y):
		self.point[1][0] = y
		
	def setScreenZ(self, z):
		self.point[2][0] = z
		
	def setPoint(self, M):
		self.point = M

	def getPoint(self):
		return self.point.copy()
		
	def getCopyPoint(self):
		return self.copy_point.copy()
