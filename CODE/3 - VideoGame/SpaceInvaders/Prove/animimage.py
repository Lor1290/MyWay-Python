##    animimage - Simple animated Sprite extension for pygame
##
##    This file is free software; you can redistribute it and/or
##    modify it under the terms of the GNU Library General Public
##    License as published by the Free Software Foundation; either
##    version 2 of the License, or (at your option) any later version.
##
##    This code is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
##    Library General Public License for more details.
##
##    You should have received a copy of the GNU Library General Public
##    License along with this file; if not, write to the Free
##    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
##
##    Nicola Cassetta
##    ncassetta@tiscali.it

"""pygame module with animated Sprite class

This module contains a simple AnimSprite (animated Sprite) class to be used
within pygame. It is a subclass of the Sprite object, so it can be added
and deleted to groups via usual pygame methods.
Before using an AnimSprite you must call the set_images() method which
initializes the list of its frames, then you can make the animation
to progress calling the update() method on a Group it belongs. When
subclassing AnimSprite class remember, if you subclass the update()
method, to call the base class method.

"""

import pygame.sprite

class AnimSprite(pygame.sprite.Sprite):
    def __init__(self, *args):
        """
    You can add the AnimSprite to one or more Group here. You
    should consider creating a Group of only AnimSprites, so you
    can call update() on it making all animation progress.
        """
        pygame.sprite.Sprite.__init__(self, *args)
        self.images = []
        self.rate = 1
        self.loop = False
        self.img_frame = 0
        self.rate_counter = 0
        self.running = True
        
    def set_images(self, img_list):
        """
    Sets the list of the animation frames
        """
        for obj in img_list:
            if isinstance(obj, str):
                self.images.append(pygame.image.load(obj).convert_alpha())
            elif isinstance(obj, pygame.Surface):
                self.images.append(obj)
        self.img_number = len(self.images)
        self.rect = self.images[0].get_rect()
        self.img_frame = 0
        self.rate_counter = 0

    def anim_stop(self, frame=None):
        self.running = False
        if frame:
            self.img_frame = 0
            update(self)
    
    def anim_start(self, frame=None):
        if frame:
            self.img_frame = frame
        self.running = True
        self.rate_counter = 0
        update(self)
        

    def set_rate(self, new_rate):
        self.rate = new_rate
        self.rate_counter = 0

    def update(self):
        self.image = self.images[self.img_frame]
        if self.running:
            self.rate_counter += 1
            if self.rate_counter >= self.rate:
                self.rate_counter -= self.rate
                self.img_frame += 1
                if self.img_frame == self.img_number:
                    self.img_frame = 0
                    if not self.loop:
                        self.kill()


#pygame.display.init()
#clk = pygame.time.Clock()
#screen = pygame.display.set_mode((640, 480))

#l = ["explosion2-0.gif", "explosion2-1.gif", "explosion2-2.gif",
#     "explosion2-3.gif", "explosion2-4.gif", "explosion2-5.gif", "explosion2-6.gif",]
#img = AnimatedImage(l, (50, 50))
#img.set_rate(2)

#done = False
#while not done:
#    for event in pygame.event.get():
#        if event.type == QUIT:
#            done = True

#    screen.fill((0, 0, 0))
#    img.paint(screen)
#    pygame.display.flip()
#    clk.tick(30)

#pygame.quit()
