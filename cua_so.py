import pygame
import os
  
pygame.init()

ASSETS_PATH = './'
FPS = 60
clock = pygame.time.Clock()
  
# Create Screen
x_screen = 900
y_screen = 600
screen = pygame.display.set_mode((x_screen, y_screen))
screen.fill((255,255,255))
x_mid = x_screen // 2
y_mid = y_screen // 2

# Title of screen
pygame.display.set_caption("Wero - Wordle")

# Text title
title_size = 50

font_title = pygame.font.SysFont("Times New Roman", title_size, bold=True)
font_end_game = pygame.font.SysFont("comicsans", 100)

x_namegame = (x_screen // 2)
y_namegame = 0

wordle = font_title.render('Worlde', True, (0, 0, 0))
vietnam = font_title.render('VietNam', True, (255, 51, 153))
game_win = font_end_game.render('You win', True, (0, 255, 0))
game_lose = font_end_game.render('You lose', True, (0, 50, 100))

#color, x, y, width, height, text, text_size, text_color, font_name
class button():
    def __init__(self, color, x, y, width, height, text='', text_size=40, text_color=(0,0,0), font_name='comicsans'):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_size = text_size
        self.text_color = text_color
        self.font_name = font_name
    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        if self.text != '':
            font = pygame.font.SysFont(self.font_name, self.text_size)
            text = font.render(self.text, True, self.text_color)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True    
        return False

class province_map():
    def __init__(self, image_list, x, y, width, height):
        self.image_list = image_list
        self.image = None
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    def load_image(self):
        for image in self.image_list:
            self.surface = pygame.image.load(os.path.join(ASSETS_PATH, image))
    def draw_image(self):
        self.image = self.surface
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        pygame.draw.rect(screen, True, (self.x - 3, self.y - 3, self.width + 6, self.height + 6), 0, border_radius = 3)
        screen.blit(self.image, (self.x, self.y))

#image_list, x, y, width, height
def draw_image(image_list, x, y, width, height):
    images = province_map(image_list, x, y, width, height)
    images.load_image()
    images.draw_image()

# running game
exit = False
result = None
hint_image_list = ["Da_Nang.png"]
image_position = ((30, 100), (30, 400))
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit = True
        if event.type == pygame.QUIT:
            exit = True
    screen.blit(wordle, wordle.get_rect(center = (x_namegame - 90, 20)))
    screen.blit(vietnam, vietnam.get_rect(center = (x_namegame + 90, 20)))
    draw_image(["Da_Nang.png"], image_position[0][0], image_position[0][1], 370, 250)
    if result == "win":
        winning_rect = button((0,150,0), x_mid - 250, y_mid - 100, 500, 200, 'You win', 100, (255, 255, 0))
        winning_rect.draw(screen)
    elif result == "lose":
        winning_rect = button((255,255,0), x_mid - 250, y_mid - 100, 500, 200, 'You lose', 100, (255, 0, 0))
        winning_rect.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
