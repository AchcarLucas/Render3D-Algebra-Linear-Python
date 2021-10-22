'''
	File de Teste - Cubo 3D
	Créditos: Lucas Campos Achcar
'''

CubeVertices = [
                # 0
                [1, 1, 1], 
                # 1
                [1, 1, -1], 
                # 2
                [1, -1, -1],
                # 3
                [1, -1, 1], 
                # 4
                [-1, 1, 1],
                # 5
                [-1, 1, -1], 
                # 6
                [-1, -1, -1], 
                # 7
                [-1, -1, 1]
           ]

CuboFace    =   [
                    # Face Direita
                    [
                        0,
                        1,
                        2,
                        3
                    ],
                    # Face Esquerda
                    [
                        4,
                        5,
                        6,
                        7
                    ],
                    # Face Inferior
                    [
                        0,
                        1,
                        5,
                        4
                    ],
                    # Face Superior
                    [
                        3,
                        2,
                        6,
                        7
                    ],
                    # Face Frontal
                    [
                        0,
                        3,
                        7,
                        4
                    ],
                    # Face Traseira
                    [
                        1,
                        2,
                        6,
                        5
                    ],
            ]

print('Python File Cube Test')
print('========== Cube Vertices ===========')
print(CubeVertices)
print('========== Cube Face ===========')
print(CuboFace)
print('=====================')