import math
import sys

import cairo
import pygame

import maraubotmap as mbm

class Loupe :

    def __init__(self):
        self._cx= 10.0
        self._cy= 5.0
        self._scale= 40.0
    
    # Transfomation:
    def toDrawing(self, x, y):
        dx= (x-self._cx)*self._scale
        dy= (y-self._cy)*-self._scale
        return (dx+self._dwidth, dy+self._dheight)

    def toWorld(self, pixx, pixy):
        return (0, 0)

    # Drawing:
    def initializeSurface(self, width, height):
        self._dwidth= width/2
        self._dheight= height/2
        self._surface= cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
        ctx = cairo.Context(self._surface)
        ctx.move_to(0, 0)
        ctx.line_to(0, height)
        ctx.line_to(width, height)
        ctx.line_to(width, 0)
        ctx.line_to(0, 0)

        ctx.set_source_rgba(0.9, 0.8, 0.4, 1.0)
        ctx.fill_preserve()
        ctx.set_line_width(8)
        ctx.set_source_rgba(0.76, 0.67, 0.33, 1.0)
        ctx.stroke()
        return self._surface

    def drawFrame( self ):
        pixx0, pixy0= self.toDrawing(0, 0)
        pixx1, pixy1= self.toDrawing(1, 1)
        ctx = cairo.Context(self._surface)
        ctx.set_line_width(4)
        ctx.move_to(pixx0, pixy0)
        ctx.line_to(pixx1, pixy0)
        ctx.set_source_rgba(1, 0, 0, 0.4)
        ctx.stroke()
        ctx.move_to(pixx0, pixy0)
        ctx.line_to(pixx0, pixy1)
        ctx.set_source_rgba(0, 1, 0, 0.4)
        ctx.stroke()
        ctx.arc(pixx0, pixy0, 5, 0, 2.0 * math.pi)
        ctx.set_source_rgba(0, 0, 4, 1.0)
        ctx.fill()
    
    def drawBody(self, body):
        ctx = cairo.Context(self._surface)
        ctx.set_line_width(4)
        pixx, pixy= self.toDrawing( body.x, body.y )
        pixRadius= body.radius * self._scale
        ctx.arc(pixx, pixy, pixRadius, 0, 2.0*math.pi)
        ctx.move_to(pixx, pixy)
        ctx.line_to(pixx+(math.cos(body.theta))*pixRadius, pixy+(-math.sin(body.theta))*pixRadius)
        ctx.set_source_rgb(0.7, 0.3, 0.03)
        ctx.stroke()

    def input(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit(0)
            else:
                print(event)

    def process(self, width=1200, height=800):
        pygame.init()
        pygame.display.set_mode((width, height))
        pygame.display.set_caption('MarauBot Map')
        screen = pygame.display.get_surface()
        
        bod= mbm.Body( 4.5, 2.2, 0.2, 0.4 )
        bod.speed= 1.0
        bod.drift= 0.4
        bod.rotate= 0.2

        while True:
            # Create PyGame surface from Cairo Surface
            self.initializeSurface(width, height)
            self.drawBody( bod )
            self.drawFrame()

            #self._surface.write_to_png("MyImage.png")
            # Create PyGame surface from Cairo Surface
            image = pygame.image.frombuffer(
                self._surface.get_data(), # Cairo seems to works on a BGRA suface...
                (width, height), "BGRA"
            )

            # Tranfer to Screen
            screen.blit(image, (0, 0))
            pygame.display.flip()

            self.input( pygame.event.get() )

            bod.process()