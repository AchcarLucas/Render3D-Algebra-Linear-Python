'''
	Main Game
	Créditos: Lucas Campos Achcar
'''

import pygame
import Render

class Game:
    def __init__(self, screenSize : (int, int), fps = 60, title='Game', icon=None, flags=0):
        self.gameRunning = True
        self.screenSize = screenSize

        self.title = title
        self.fps = fps
        self.icon = icon
        self.flags = flags

        self.initGame()

        self.render = Render.C_Render()

    def initGame(self):
        self.screen = pygame.display.set_mode(self.screenSize, flags = self.flags)
        pygame.display.set_caption(self.title)

        if(self.icon != None):
            pygame.display.set_icon(self.icon)

        pygame.font.init()

        self.gameClock = pygame.time.Clock()
        self.gameFont = pygame.font.SysFont('Arial', 35)

    def gameMain(self):
        while self.gameRunning:
            self.deltaTime = self.gameClock.tick(self.fps)
            self.screen.fill((50, 50, 50))

            for event in pygame.event.get():
                self.gameEvent(event)

            self.gameUpdate()
            self.gameRender()

            pygame.display.update()

        pygame.display.quit()

    def gameEvent(self, event):
        if(event.type == pygame.QUIT):
            self.gameRunning = False
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_ESCAPE):
                self.gameRunning = False

    def gameUpdate(self):
        self.render.update(self.deltaTime)

    def gameRender(self):
        self.render.render(self.screen)

# instancia o game e executa o gameMain
game = Game((800, 600), title='Alglin')
game.gameMain()
