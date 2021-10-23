'''
	Módulo C_Render
	C_Render é a Classe para a renderização dos objetos na tela
	Créditos: Lucas Campos Achcar
'''

import pygame
import numpy as np
import Matrices as mtc
import LinearTransform
import Point

import CubeTest
import SphereTest
import MonkeyTest

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

		self.listVerticesCube = []
		self.listVerticesSphere = []
		self.listVerticesMonkey = []

		self.linearTransform = LinearTransform.C_LinearTransform(cam=[0, 180, 0])

		for p in CubeTest.CubeVertices:
			self.listVerticesCube.append(Point.C_Point(p, self.linearTransform.factor, (255, 255, 255), scale = 1.0))

		for p in SphereTest.SphereVertices:
			self.listVerticesSphere.append(Point.C_Point(p, self.linearTransform.factor, (255, 255, 255), scale = 1.0))

		for p in MonkeyTest.MonkeyVertices:
			self.listVerticesMonkey.append(Point.C_Point(p, self.linearTransform.factor, (255, 255, 255), scale = 1.0))

		# lista de pontos, lista de faces, tupla de ângulos de rotação, tupla de posição, tupla de escala, if render point, if render line, len face
		self.Cube = [self.listVerticesCube, CubeTest.CubeFace, [0.0, 0, 0], [0, 0, 0], [1.0, 1.0, 1.0], False, True, len(CubeTest.CubeFace)]
		self.Sphere = [self.listVerticesSphere, SphereTest.SphereFace, [0.0, 0, 0], [0, 0, 0], [2.0, 2.0, 2.0], False, True, len(SphereTest.SphereFace)]
		self.Monkey = [self.listVerticesMonkey, MonkeyTest.MonkeyFace, [0.0, 0, 0], [0, 0, 0], [2.0, 2.0, 2.0], False, True, len(MonkeyTest.MonkeyFace)]

		self.Object = self.Monkey

		self.increaseDT = 0.0

	def update(self, deltaTime):
		'''
			Função responsável por atualizar os objetos na tela
			Args:
				None
			Return:
				None
		'''
		#self.Object[2][0] += deltaTime * 0.01
		#self.Object[2][1] += deltaTime * 0.01
		#self.Object[2][2] += deltaTime * 0.01

		#self.increaseDT += deltaTime * 0.001

		#self.Object[4][0] = self.Object[4][1] = self.Object[4][2] = np.abs(np.cos(self.increaseDT)) + .5

	def render(self, screen):
		'''
			Função responsável por renderizar objetos fixos na tela (Por exemplo, eixos coordenados)
			Args:
				None
			Return:
				None
		'''

		# matriz identidade 4x4
		MVP = mtc.C_Matrix.identity(4)

		# faz a transformação de rotação camera
		MVP = self.linearTransform.rotateY(MVP, self.linearTransform.cam[0])
		MVP = self.linearTransform.rotateZ(MVP, self.linearTransform.cam[1])
		MVP = self.linearTransform.rotateX(MVP, self.linearTransform.cam[2])

		# faz a transformação de rotação do objeto
		MVP = self.linearTransform.rotateY(MVP, self.Object[2][0])
		MVP = self.linearTransform.rotateZ(MVP, self.Object[2][1])
		MVP = self.linearTransform.rotateX(MVP, self.Object[2][2])

		# faz a transformação da escala
		MVP = self.linearTransform.scaleXYZ(MVP, self.Object[4])

		# faz a transformação da translação
		MVP = self.linearTransform.translateXYZ(MVP, self.Object[3])

		# faz a transformação perspectiva
		MVP = self.linearTransform.perspectiveProjection(MVP)

		# Render Vertices
		for p in self.Object[0]:

			# transforma o ponto
			P = mtc.C_Matrix.mul(MVP, p.getCopyPoint())

			# faz o setting do novo ponto para dentro do objeto Point
			p.setPoint(P)

			# renderiza o ponto
			if(self.Object[5]):
				p.render(screen)

		if(self.Object[6]):
			for face in self.Object[1]:
				len_face = len(face)
				for index in range(0, len_face):
					first_point = face[index]
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