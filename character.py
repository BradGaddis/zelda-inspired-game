import pygame

class Character(pygame.sprite.Sprite):
    
    def __init__(self, sprite):
        ballrect = sprite.get_rect()
        self.speed = 2
        size = width, height = 320, 240

        #move the character
        def update():
            ballrect = ballrect.move(self.speed)
            if ballrect.left < 0 or ballrect.right > width:
                self.speed[0] = -self.speed[0]
            if ballrect.top < 0 or ballrect.bottom > height:
                self.speed[1] = -self.speed[1]
                


        