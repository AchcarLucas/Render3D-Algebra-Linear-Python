'''
	File de Teste - Cubo 3D
	Créditos: Lucas Campos Achcar
'''

CubeVerticesGross = [1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,1,1,1,1,1,-1,1,-1,1,-1,1,1]
CubeFaceGross = [0,1,2,3,4,5,5,6,0,4,1,6,1,3,2,0,3,5,0,6,1,3,7,4,5,4,6,4,7,1,1,7,3,0,2,3]

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