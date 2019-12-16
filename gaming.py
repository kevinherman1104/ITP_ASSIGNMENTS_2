import pygame

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                image = pygame.image.load(path)
                _image_library[path] = image
        return image
 
pygame.init()
screen = pygame.display.set_mode((1000, 900))
done = False
is_blue = True
x = 30
y = 30
 
clock = pygame.time.Clock()
 
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
         
        screen.fill((255, 255, 255))
        screen.blit(get_image('JUTX6294.jpg'), (x,y))       

        
        pygame.display.flip()
        clock.tick(60)