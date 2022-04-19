import pygame

pygame.init()
pygame.font.init()

class Board:
    SIZE = 500
    def __init__(self, RES: tuple) -> None:
        self.WIDTH = RES[0]
        self.HEIGHT = RES[1]
        self.START = (self.WIDTH/2-250, 0)
        self.win = 0
        self.peaces = []
        self.grid = [
            [
                pygame.Rect(self.START[0], self.START[1], self.SIZE/3, self.SIZE/3),
                pygame.Rect(self.SIZE/3+self.START[0], self.START[1], self.SIZE/3, self.SIZE/3),
                pygame.Rect((self.SIZE*2)/3+self.START[0], self.START[1], self.SIZE/3, self.SIZE/3)
            ],
            [
                pygame.Rect(self.START[0], self.SIZE/3+self.START[1], self.SIZE/3, self.SIZE/3),
                pygame.Rect(self.SIZE/3+self.START[0], self.SIZE/3+self.START[1], self.SIZE/3, self.SIZE/3),
                pygame.Rect((self.SIZE*2)/3+self.START[0], self.SIZE/3+self.START[1], self.SIZE/3, self.SIZE/3)
            ],
            [
                pygame.Rect(self.START[0], (self.SIZE*2)/3+self.START[1], self.SIZE/3, self.SIZE/3),
                pygame.Rect(self.SIZE/3+self.START[0], (self.SIZE*2)/3+self.START[1], self.SIZE/3, self.SIZE/3),
                pygame.Rect((self.SIZE*2)/3+self.START[0], (self.SIZE*2)/3+self.START[1], self.SIZE/3, self.SIZE/3)
            ]
        ]

    def draw(self, WIN: pygame.surface) -> None:
        pygame.draw.line(WIN, (255, 255, 255), (self.START[0], self.SIZE/3), (self.START[0]+self.SIZE, self.SIZE/3))
        pygame.draw.line(WIN, (255, 255, 255), (self.START[0], (self.SIZE*2)/3), (self.START[0]+self.SIZE, (self.SIZE*2)/3))
        pygame.draw.line(WIN, (255, 255, 255), (self.SIZE/3 + self.START[0], self.START[1]), (self.SIZE/3 + self.START[0], self.SIZE))
        pygame.draw.line(WIN, (255, 255, 255), ((self.SIZE*2)/3+self.START[0], self.START[1]), ((self.SIZE*2)/3+self.START[0], self.SIZE))

        for i in self.peaces:
            self.letterDraw(WIN, i[0], i[1])
        


    def peaceIsTaken(self, rect: pygame.Rect) -> bool:
        for i in self.peaces:
            if i[0].x == rect.x and i[0].y == rect.y:
                return False
        return True

    def click(self) -> int:
        if self.win:
            pass
        else:
            for col in self.grid:
                for rect in col:
                    if rect.collidepoint(pygame.mouse.get_pos()) and self.peaceIsTaken(rect):
                        self.peaces.append((rect, len(self.peaces)%2))
            
            win = self.checkWin()
            if win:
                self.win = win
    
    def goBack(self) -> None:
        if len(self.peaces):
            self.peaces.pop()
        self.win = 0

    def letterDraw(self, WIN: pygame.surface, rect: pygame.Rect, typeP: bool) -> None:
        if typeP:
            pygame.draw.circle(WIN, (255, 255, 255), rect.center, rect.width/2)
        else:
            pygame.draw.line(WIN, (255, 255, 255), (rect.x, rect.y), (rect.x+rect.width, rect.y+rect.height), 10)
            pygame.draw.line(WIN, (255, 255, 255), (rect.x, rect.y+rect.width), (rect.x+rect.width, rect.y), 10)
    
    def restart(self) -> None:
        self.peaces.clear()
        self.win = 0
    
    def checkWin(self) -> str:
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for peace in self.peaces:
            xPos = round(((-3*self.START[0])+(3*peace[0].x))/self.SIZE)
            yPos = round(((-3*self.START[1])+(3*peace[0].y))/self.SIZE)
            if peace[1]:
                board[xPos][yPos] = 1
            else:
                board[xPos][yPos] = -1
        
        possible = []
        for i in range(3):
            possible.append(board[i][0] + board[i][1] + board[i][2])
        for i in range(3):
            possible.append(board[0][i] + board[1][i] + board[2][i])
        possible.append(board[0][0] + board[1][1] + board[2][2])
        possible.append(board[0][2] + board[1][1] + board[2][0])

        if 3 in possible:
            return "o"
        elif -3 in possible:
            return "x"
        elif not 0 in possible:
            return "no one"