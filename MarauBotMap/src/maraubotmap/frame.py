import math
import sys

import cairo
import pygame

class Frame :

    def __init__(self):
        self._width= 800
        self._height= 600
    
    def initializeSurface(self):
        self._surface= cairo.ImageSurface(cairo.FORMAT_ARGB32, self._width, self._height)
        return self._surface

    def drawFrame( self ):
        ctx = cairo.Context(self._surface)
        ctx.set_line_width(4)
        ctx.move_to(100, 100)
        ctx.line_to(120, 100)
        ctx.set_source_rgba(1, 0, 0, 1.0)
        ctx.stroke()
        ctx.move_to(100, 100)
        ctx.line_to(100, 80)
        ctx.set_source_rgba(0, 1, 0, 1.0)
        ctx.stroke()
        ctx.arc(100, 100, 5, 0, 2.0 * math.pi)
        ctx.set_source_rgba(0, 0, 4, 1.0)
        ctx.fill()
    
    def drawBody(self, x, y, radius):
        ctx = cairo.Context(self._surface)
        ctx.set_line_width(15)
        ctx.arc(x, y, radius, 0, 2.0 * math.pi)
        ctx.set_source_rgb(0.8, 0.8, 0.8)
        ctx.fill_preserve()
        ctx.set_source_rgb(1, 1, 1)
        ctx.stroke()

    def input(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit(0)
            else:
                print(event)


    def process(self):
        pygame.init()
        pygame.display.set_mode(( self._width, self._height ))
        screen = pygame.display.get_surface()

        radius= 10

        while True:
            # Create PyGame surface from Cairo Surface
            self.initializeSurface()
            radius=  min(600, radius+10)
            self.drawBody(250, 200, radius )
            self.drawFrame()


            #self._surface.write_to_png("MyImage.png")

            # Create PyGame surface from Cairo Surface
            image = pygame.image.frombuffer(
                self._surface.get_data(), # Cairo seems to works on a BGRA suface...
                (self._width, self._height), "BGRA"
            )

            # Tranfer to Screen
            screen.blit(image, (0, 0))
            pygame.display.flip()

            self.input( pygame.event.get() )