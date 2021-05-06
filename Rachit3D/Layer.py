import pyglet
from pyglet.gl import *

from .Texturing import load_texture

class Layer:
    def __init__(self, point1, point2, point3, point4, height, texture):
        self.x1, self.y1 = point1
        self.x2, self.y2 = point2
        self.x3, self.y3 = point3
        self.x4, self.y4 = point4
        self.height = height

        self.type = 'layer'
        
        self.texture = load_texture(texture)
        self.tex_coords = ('t2f',(0, 0, 1, 0, 1, 1, 0, 1,))