'''
	Módulo C_Render
	C_Render é a Classe para a renderização dos objetos na tela
'''

import pygame
import numpy as np
import Matrices as mtc
import LinearTransform
import Point
import CubeTest

class C_Render:
	def __init__(self):
		'''
			Função construct (Inicia todas as variáveis necessárias para a utilização da classe C_Render)
			Args:
				c_draw: Instância do C_Draw
			Return:
				None
		'''

		self.screenSize = pygame.display.get_window_size()

		self.listPointCube = []

		self.linearTransform = LinearTransform.C_LinearTransform(cam=[0, 0, 0])

		for p in CubeTest.CubePoint:
			self.listPointCube.append(Point.C_Point(p, self.linearTransform.factor, (255, 255, 255)))

		# lista de pontos, lista de faces, tupla de ângulos de rotação, tupla de posição, tupla de escala
		self.Object = [self.listPointCube, CubeTest.CuboFace, [0.0, 0, 0], [0, 0, 0], [1.0, 1.0, 1.0]]

	def update(self, deltaTime):
		'''
			Função responsável por atualizar os objetos na tela
			Args:
				None
			Return:
				None
		'''
		self.Object[2][0] += deltaTime * 0.01
		self.Object[2][1] += deltaTime * 0.01
		self.Object[2][2] += deltaTime * 0.01

	def render(self, screen):
		'''
			Função responsável por renderizar objetos fixos na tela (Por exemplo, eixos coordenados)
			Args:
				None
			Return:
				None
		'''

		# DESENHA OS PONTOS PRIMEIRO
		MVP = mtc.C_Matrix.identity(4)

		# faz a transformação de rotação camera
		MVP = self.linearTransform.rotateY(MVP, self.linearTransform.cam[0])
		MVP = self.linearTransform.rotateZ(MVP, self.linearTransform.cam[1])
		MVP = self.linearTransform.rotateX(MVP, self.linearTransform.cam[2])

		# Cube Point
		for p in self.Object[0]:
			# faz uma cópia das transformações da câmera (é comum a todos os pontos)
			T_MVP = MVP.copy()
			
			# faz a transformação de rotação do objeto
			T_MVP = self.linearTransform.rotateY(T_MVP, self.Object[2][0])
			T_MVP = self.linearTransform.rotateZ(T_MVP, self.Object[2][1])
			T_MVP = self.linearTransform.rotateX(T_MVP, self.Object[2][2])

			# faz a transformação da escala
			T_MVP = self.linearTransform.scaleXYZ(T_MVP, self.Object[4])

			# faz a transformação da translação
			T_MVP = self.linearTransform.translateXYZ(T_MVP, self.Object[3])

			# faz a transformação perspectiva
			T_MVP = self.linearTransform.perspectiveProjection(T_MVP)

			# transforma o ponto
			P = mtc.C_Matrix.mul(T_MVP, p.getCopyPoint())

			# faz o setting do novo ponto para dentro do objeto Point
			p.setPoint(P)

			# renderiza o ponto
			p.render(screen)

		# Cube Face
		for face in self.Object[1]:
			len_face = len(face)
			for index in range(0, len(face)):
				first_point = face[index % len_face]
				second_point = face[(index + 1) % len_face]

				pygame.draw.line(screen, (255, 255, 255), 
						(
							self.Object[0][first_point].getScreenX(),
							self.Object[0][first_point].getScreenY()
						), 
						(
							self.Object[0][second_point].getScreenX(),
							self.Object[0][second_point].getScreenY()
						)
						)
