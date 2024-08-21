 
import pygame

import numpy as np

def main():
    click_counter = 0
    score = 0
    pygame.init()
    width= 1000
    height=1000
    sce=pygame.display.set_mode((width,height))
    buble = pygame.image.load("GJ image-1.png")
    back = pygame.image.load("bg.PNG")

    def put_buble_at_0_0(x,y):

        sce.blit(back, (x,y))
    x = (width*0.0)
    y = (height*0.0)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        sce.blit(buble,(350,250))
        pygame.display.flip()
        put_buble_at_0_0(x,y)

    
       



#main()
if __name__ == "__main__":
    main()
