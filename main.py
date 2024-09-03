import pygame
import sys
import random


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_open = False
        self.is_mine = False
        
class Board:
    def __init__(self, width, height, num_mines):
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.game_over = False
        self.cells = [[Cell(x, y) for x in range(width)] for y in range(height)]
        self.place_mines()
        
        
    def place_mines(self):
        mines = 0
        
        while mines < self.num_mines:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height -1)
            if not self.cells[x][y].is_mine:
                self.cells[x][y].is_mine = True
                mines += 1  

    def draw_board(self, screen):
        cell_size = 40
        for row in self.cells:
            for cell in row:
                rect = pygame.Rect(cell.x * cell_size, cell.y * cell_size, cell_size, cell_size)
                if cell.is_open:
                    color = (200, 200, 200) #açık hücre rengi
                    pygame.draw.rect(screen, color, rect)
                    pygame.draw.rect(screen, (0, 0, 0), rect, 1)
                    
                    if cell.is_mine:
                        pygame.draw.circle(screen, (255, 0, 0), rect.center, cell_size // 4)
                        self.game_over = True
                    else:
                        number = str(self.calculate_neighbors(cell.y, cell.x))
                        font = pygame.font.Font(None, 36)
                        text = font.render(number, True, (0, 0, 255))
                        text_rect = text.get_rect(center=(cell.x * cell_size + 20, cell.y * cell_size + 20))
                        screen.blit(text, text_rect)
                else:
                    color = (100, 100, 100) #kapalı hücre rengi
                    pygame.draw.rect(screen, color, rect)
                    pygame.draw.rect(screen, (0, 0, 0), rect, 1)
    
    def calculate_neighbors(self, x, y):
        mines = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if self.cells[nx][ny].is_mine:
                        mines += 1
        if mines == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        self.cells[nx][ny].is_open = True
            
        return mines

    def handle_click(self, pos):
        cell_size = 40
        x, y = pos
        x //= cell_size
        y //= cell_size
        if 0 <= x < self.width and 0 <= y < self.height:
            self.cells[y][x].is_open = True


    def check_win(self):
        for row in self.cells:
            for cell in row:
                if not cell.is_mine and not cell.is_open:
                    return False
        return True
        
    
    def draw_message(self, screen, message):
        font = pygame.font.Font(None, 74)
        text = font.render(message, True, (255, 0, 0))
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() //2))
        screen.blit(text, text_rect)
        
        
pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Minesweeper")
icon = pygame.image.load('mine.png')
pygame.display.set_icon(icon)




width = 10
height = 10
mines = 15
board = Board(width, height, mines)

running = True
game_won = False

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not board.game_over:
            pos = pygame.mouse.get_pos()
            board.handle_click(pos)
            if board.check_win():
                board.game_over = True
                game_won = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                board = Board(width, height, mines)
                game_won = False

         
    screen.fill((255, 255, 255))
    
    board.draw_board(screen)
    
    if board.game_over:
        if game_won:
            board.draw_message(screen, "You Win!")
        else:
            board.draw_message(screen, "Game Over!")
    
    pygame.display.flip()