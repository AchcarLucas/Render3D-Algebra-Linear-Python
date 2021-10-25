'''
	File de Teste - Cubo 3D
	Créditos: Lucas Campos Achcar
'''

CubeVerticesGross = [   1.000000, 1.000000, -1.000000, 
                        1.000000, -1.000000, -1.000000, 
                        1.000000, 1.000000, 1.000000,
                        1.000000, -1.000000, 1.000000,
                        -1.000000, 1.000000, -1.000000,
                        -1.000000, -1.000000, -1.000000,
                        -1.000000, 1.000000, 1.000000,
                        -1.000000, -1.000000, 1.000000]
                        
                        
CubeFaceGross = [
                4, 2, 0,
                2, 7, 3,
                6, 5, 7,
                1, 7, 5,
                0, 3, 1,
                4, 1, 5,
                
                4, 6, 2,
                2, 6, 7,
                6, 4, 5,
              
                1, 3, 7,
                0, 2, 3,
                4, 0, 1
]

CubeVertices = []
CubeFace = []

# Cada vertice compreende 3 componentes (x, y, z)
for index in range(0, len(CubeVerticesGross), 3):
    CubeVertices.append([CubeVerticesGross[index], CubeVerticesGross[index + 1], CubeVerticesGross[index + 2]])

# Cada face compreende 3 vertices
for index in range(0, len(CubeFaceGross), 3):
    CubeFace.append([CubeFaceGross[index], CubeFaceGross[index + 1], CubeFaceGross[index + 2]])

print('Python File Cube Test')
print('========== Cube Vertices ===========')
print(CubeVertices)
print('========== Cube Face ===========')
print(CubeFace)
print('=====================')