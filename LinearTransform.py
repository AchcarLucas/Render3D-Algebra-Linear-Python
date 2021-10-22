'''
	Módulo Linear_Transform
	C_LinearTransform é responsável por fazer as transformações lineares de rotação, translação, escala e projeção de perspectiva
	Créditos: Lucas Campos Achcar
'''

# http://www.ic.uff.br/~aconci/Aula-7.pdf
# https://pt.wikipedia.org/wiki/Matriz_de_rota%C3%A7%C3%A3o
# Slide da professora de Álgebra Linear
# https://slideplayer.com.br/slide/377102/

import numpy as np
import Matrices as mtc

class C_LinearTransform:
	def __init__(self, angleOfView = 45., near = 1., far = 100., factor = 100., cam = [45.0, 0.0, 135,0]):
		'''
			Função construct (Inicia todas as variáveis necessárias para a utilização da classe C_LinearTransform)
			Args:
				None
			Return:
				None
		'''

		# conversor degree em rad
		self.Deg2Rad = np.pi / 180.0

		self.angleOfView = angleOfView
		self.near = near
		self.far = far
		self.factor = factor
		self.cam = cam

		# constantes usados na projeção perspectiva
		self.S = 1. / (np.tan((self.angleOfView) * self.Deg2Rad))

		self.r_3_3 = -2.0 / (self.far - self.near)
		self.r_3_4 = (self.far + self.near) / (self.far - self.near)  

	def rotateX(self, M, angle_degree):
		'''
			Matrix de Rotação (Eixo X)
			T(x, y, z, w) = M(4, 4) * M(4, 1) -> R^4
			
			T_x(x, y, z, w) = (x, y*cos(Theta) - z*sin(Theta), y*sin(Theta) + z*cos(Theta), 0)
			
			
								| 1			0				0	  			0 |			|	x	|
			T(x, y, z, w)	=	| 0			cos(Theta)		-sen(Theta) 	0 | 	* 	|	y	|
								| 0			sin(Theta)		cos(Theta)		0 |			|	z	|
								| 0			0				0 				1 |			|	0	|
						
						
			Entrada (Input): Matriz 4 x 1 e ângulo
			Saída (Output): Matriz 4 x 4
		'''

		# faz a conversão de degree em rad
		theta = angle_degree * self.Deg2Rad
		
		# decompõe o ângulo
		cos_theta = np.cos(theta)
		sin_theta = np.sin(theta)
		
		# a matrix de rotação Z é uma matrix de 4 linhas e 4 colunas
		M_ROTATE_X =	[	
							[1, 			0, 			0,			0], 
							[0, 			cos_theta, 	-sin_theta,	0], 
							[0, 			sin_theta, 	cos_theta, 	0],
							[0, 			0, 			0,			1]
						]
		
		# multiplica a matriz de rotação X pela matrix M recebida pelo parâmetro
		return mtc.C_Matrix.mul(M_ROTATE_X, M)


	def rotateY(self, M, angle_degree):
		'''
			Matrix de Rotação (Eixo Y)
			T(x, y, z, w) = M(4, 4) * M(4, 1) -> R^4
			
			T_y(x, y, z, w) = (x*cos(Theta) - z*sin(Theta), y, x*sin(Theta) + z*cos(Theta), 0)
			
			
							| cos(Theta)	0		-sen(Theta)		0 |			|	x	|
			T(x, y, z)	=	| 0				1		0				0 |		*	|	y	|
							| sin(Theta)	0		cos(Theta)		0 |			|	z	|
							| 0				0		0				1 |			|	0	|
						
						
			Entrada (Input): Matriz 4 x 1 e ângulo
			Saída (Output): Matriz 4 x 4
		'''

		# faz a conversão de degree em rad
		theta = angle_degree * self.Deg2Rad
		
		# decompõe o ângulo
		cos_theta = np.cos(theta)
		sin_theta = np.sin(theta)
		
		# a matrix de rotação Y é uma matrix de 4 linhas e 4 colunas
		M_ROTATE_Y = [
						[cos_theta,		0,		-sin_theta,		0], 
						[0,				1,		0,				0], 
						[sin_theta,		0,		cos_theta,		0],
						[0,				0,		0,				1]
					]
		
		# multiplica a matriz de rotação Y pela matrix M recebida pelo parâmetro
		return mtc.C_Matrix.mul(M_ROTATE_Y, M)

	def rotateZ(self, M, angle_degree):
		'''
			Matrix de Rotação (Eixo Z)
			T(x, y, z, w) = M(4, 4) * M(4, 1) -> R^4
			
			T_z(x, y, z, w) = (x*cos(Theta) - y*sin(Theta), x*sin(Theta) + y*cos(Theta), z, 0)
			
			
								| cos(Theta)	sen(Theta)	0	0 |		|	x	|
			T(x, y, z, w) = 	| -sin(Theta)	cos(Theta)	0 	0 | * 	|	y	|
								| 0				0			1 	0 |		|	z	|
								| 0				0			0 	1 |		|	0	|
						
						
			Entrada (Input): Matriz 4 x 1 e ângulo
			Saída (Output): Matriz 4 x 4
		'''

		# faz a conversão de degree em rad
		theta = angle_degree * self.Deg2Rad
		
		# decompõe o ângulo
		cos_theta = np.cos(theta)
		sin_theta = np.sin(theta)
		
		# a matrix de rotação Z é uma matrix de 4 linhas e 4 colunas
		M_ROTATE_Z = [
						[ cos_theta, 	sin_theta, 	0, 	0], 
						[-sin_theta, 	cos_theta, 	0,	0], 
						[0, 			0,			1,	0],
						[0, 			0, 			0,	1]
					]
		
		# multiplica a matriz de rotação Z pela matrix M recebida pelo parâmetro
		return mtc.C_Matrix.mul(M_ROTATE_Z, M)
	
	def scaleXYZ(self, M, scale=(1.0, 1.0, 1.0)):
		'''
			Matrix de Escala (Eixo XYZ)
			T(x, y, z, w) M(4, 4) * M(4, 1) -> R^4
			
			T_scale(x, y, z, w) = (scale_x*x, scale_y*y, scale_z*z, 0)
			
			
								| scale_x			0				0  			0 |		|	x	|
			T(x, y, z, w) = 	| 0					scale_y			0  			0 |  * 	|	y	|
								| 0					0				scale_z 	0 |		|	z	|
								| 0					0				0 			1 |		|	0	|
						
						
			Entrada (Input): Matriz 4 x 1 a escala
			Saída (Output): Matriz 4 x 4
		'''
		
		# A matrix de escala X, Y e Z é uma matrix de 4 linhas e 4 colunas
		M_SCALE_XYZ =	[	
							[scale[0], 		0, 		0, 			0], 
							[0, 		scale[1], 	0, 			0], 
							[0, 		0,			scale[2], 	0], 
							[0, 		0, 			0, 			1]
						]
		
		# faz a transformação linear
		return mtc.C_Matrix.mul(M_SCALE_XYZ, M)

	def translateXYZ(self, M, position = (0.0, 0.0, 0.0)):
		'''
			Matrix de posição (Eixo XYZ)
			T(x, y, z, w) = M(4, 4) * M(4, 1) -> R^4
			
			T_translate(x, y, z, w) = (x - position_x, y - position_y, z - position_z, 0)
			
			
								| 1				0				0		-position_x |
			T(x, y, z, w) = 	| 0				1				0		-position_y | 	* 	T
								| 0				0				1		-position_z |
								| 0				0				0 		1			|
						
						
			Entrada (Input): Matriz 4 x 1 a posição
			Saída (Output): Matriz 4 x 4
		'''
		
		# A matrix de posicionamento X, Y e Z é uma matrix de 4 linhas e 4 colunas
		M_POSITION_XYZ =	[	
								[1, 		0, 		0, 		position[0]], 
								[0, 		1, 		0, 		position[1]], 
								[0, 		0,		1, 		position[2]], 
								[0, 		0, 		0, 		1]
							]
		
		# faz a transformação linear
		return mtc.C_Matrix.mul(M_POSITION_XYZ, M)
		
	def perspectiveProjection(self, M):
		'''
			Matrix de projeção Perspectiva
			T(x, y, z, w) = M(4, 4) * M(4, 1) -> R^4
			
			T_perspective(x, y, z, w) = (x, y, z, 0)
			
			
								| d				0				0						0 								|		|	x	|
			T(x, y, z, w) = 	| 0				d				0						0 								| 	* 	|	y	|
								| 0				0				(-2 / (far - near))		0 								|		|	z	|
								| 0				0				0						-(far + near) / (far - near)	|		|	1	|
						
						
			Entrada (Input): Matriz 4 x 1 a posição
			Saída (Output): Matriz 4 x 4
		'''
		
		# a matrix de posicionamento X, Y e Z é uma matrix de 4 linhas e 4 colunas
		M_PROJECTION =	[		
							[self.S, 		0, 		0, 				0], 
							[0, 		self.S, 	0, 				0], 
							[0, 		0,			self.r_3_3, 	self.r_3_4], 
							[0, 		0, 			-1, 			1]
						]
		
						
		# faz a transformação linear da projeção perspectiva
		return mtc.C_Matrix.mul(M_PROJECTION, M)