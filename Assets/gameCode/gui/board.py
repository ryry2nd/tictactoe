import pygame

class Board:
    def __init__(self, RES):
        self.WIDTH = RES[0]
        self.HEIGHT = RES[1]
        self.peaces = []
        self.grid = [
            [
                pygame.Rect(0, 0, self.WIDTH//3, self.HEIGHT//3),
                pygame.Rect(self.WIDTH//3, 0, self.WIDTH//3, self.HEIGHT//3),
                pygame.Rect((self.WIDTH*2)//3, 0, self.WIDTH//3, self.HEIGHT//3)
            ],
            [
                pygame.Rect(0, self.HEIGHT//3, self.WIDTH//3, self.HEIGHT//3),
                pygame.Rect(self.WIDTH//3, self.HEIGHT//3, self.WIDTH//3, self.HEIGHT//3),
                pygame.Rect((self.WIDTH*2)//3, self.HEIGHT//3, self.WIDTH//3, self.HEIGHT//3)
            ],
            [
                pygame.Rect(0, (self.HEIGHT*2)//3, self.WIDTH//3, self.HEIGHT//3),
                pygame.Rect(self.WIDTH//3, (self.HEIGHT*2)//3, self.WIDTH//3, self.HEIGHT//3),
                pygame.Rect((self.WIDTH*2)//3, (self.HEIGHT*2)//3, self.WIDTH//3, self.HEIGHT//3)
            ]
        ]

    def draw(self, WIN):
        pygame.draw.line(WIN, (255, 255, 255), (0, self.HEIGHT//3), (self.WIDTH, self.HEIGHT//3))
        pygame.draw.line(WIN, (255, 255, 255), (0, (self.HEIGHT*2)//3), (self.WIDTH, (self.HEIGHT*2)//3))
        pygame.draw.line(WIN, (255, 255, 255), (self.WIDTH//3, 0), (self.WIDTH//3, self.HEIGHT))
        pygame.draw.line(WIN, (255, 255, 255), ((self.WIDTH*2)//3, 0), ((self.WIDTH*2)//3, self.HEIGHT))

        for i in self.peaces:
            self.letterDraw(WIN, i)

    def peaceIsTaken(self, rect):
        for i in self.peaces:
            if i[0].x == rect.x and i[0].y == rect.y:
                return False
        return True

    def click(self):
        for col in self.grid:
            for rect in col:
                if rect.collidepoint(pygame.mouse.get_pos()) and self.peaceIsTaken(rect):
                    self.peaces.append((rect, len(self.peaces)%2))
    
    def goBack(self):
        if len(self.peaces):
            self.peaces.pop()

    def letterDraw(self, WIN, xData):
        x = xData[0][0]
        y = xData[0][1]

        if xData[1]:
            pygame.draw.circle(WIN, (255, 255, 255), (x+100, y+100), 100)
        else:
            pygame.draw.line(WIN, (255, 255, 255), (x, y), (x+200, y+200), 10)
            pygame.draw.line(WIN, (255, 255, 255), (x+200, y), (x, y+200), 10)