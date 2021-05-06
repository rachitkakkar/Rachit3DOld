# THIS IS A STANDALONE DEMO WHICH REPRESENTS ME LEARNING OPENGL - NOT PART OF THE ENGINE
import math

import pyglet
from pyglet.gl import *
from pyglet.window import key

def load_texture(file):
    texture = pyglet.resource.texture(file)
    glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
    return pyglet.graphics.TextureGroup(texture)

class Model:
    def __init__(self):
        self.batch = pyglet.graphics.Batch()
        
        self.top = load_texture('Textures/grass_top.png')
        self.side = load_texture('Textures/grass_side.png')
        self.bottom = load_texture('Textures/dirt.png')

        tex_coords = ('t2f',(0,0, 1,0, 1,1, 0,1, ))
        x,y,z = 0,0,-1
        X,Y,Z = x+1,y+1,z+1

        self.batch.add(4,GL_QUADS,self.side,('v3f',(x,y,z, x,y,Z, x,Y,Z, x,Y,z, )),tex_coords)
        self.batch.add(4,GL_QUADS,self.side,('v3f',(X,y,Z, X,y,z, X,Y,z, X,Y,Z, )),tex_coords)
        self.batch.add(4,GL_QUADS,self.bottom,('v3f',(x,y,z, X,y,z, X,y,Z, x,y,Z, )),tex_coords)
        self.batch.add(4,GL_QUADS,self.top,('v3f',(x,Y,Z, X,Y,Z, X,Y,z, x,Y,z, )),tex_coords)
        self.batch.add(4,GL_QUADS,self.side,('v3f',(X,y,z, x,y,z, x,Y,z, X,Y,z, )),tex_coords)
        self.batch.add(4,GL_QUADS,self.side,('v3f',(x,y,Z, X,y,Z, X,Y,Z, x,Y,Z, )),tex_coords)

    def draw(self):
        self.batch.draw()


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.models = []
        self.camera = Camera()
        
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)
        self.set_minimum_size(300, 200)

    def render_model(self, model):
        self.models.append(model)

    def set_update_func(self, func):
        pyglet.clock.schedule(func)

    def run(self):
        pyglet.app.run()

    def fill(self, r, g, b):
        glClearColor(r, g, b, 1.0)

    def key_held(self, key):
        if self.keys[key]:
            return True

        return False

    def on_draw(self):
        self.clear()
        glEnable(GL_DEPTH_TEST)
        # glEnable(GL_CULL_FACE)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(70, self.width/self.height, 0.05, 1000)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glPushMatrix()
        glRotatef(-self.camera.rot[0], 1.0, 0.0, 0.0)
        glRotatef(-self.camera.rot[1], 0.0, 1.0, 0.0)
        glRotatef(-self.camera.rot[2], 0.0, 0.0, 1.0)  
        glTranslatef(-self.camera.pos[0], -self.camera.pos[1], -self.camera.pos[2])

        for model in self.models:
            model.draw()

        self.models = []

        glPopMatrix()

    def on_resize(self, width, height):
        glViewport(0, 0, width, height)

class Camera:
    def __init__(self,pos=(0,0,0),rot=(0,0)):
        self.pos = list(pos)
        self.rot = list(rot)


window = Window(width=800, height=600, caption='Demo1: A Minecraft Block', resizable=True)
window.camera = Camera((0.5,1.5,1.5),(-30,0,0))

def handle_fps_camera(camera, dt):
    s = dt*10
    rotY = -camera.rot[1]/180*math.pi
    dx,dz = s*math.sin(rotY),s*math.cos(rotY)

    if window.key_held(key.W): camera.pos[0]+=dx; camera.pos[2]-=dz
    if window.key_held(key.S): camera.pos[0]-=dx; camera.pos[2]+=dz
    if window.key_held(key.A): camera.pos[0]-=dz; camera.pos[2]-=dx
    if window.key_held(key.D): camera.pos[0]+=dz; camera.pos[2]+=dx

    if window.key_held(key.SPACE): camera.pos[1]+=s
    if window.key_held(key.LSHIFT): camera.pos[1]-=s

    if window.key_held(key.UP): camera.rot[0] += 2.5
    if window.key_held(key.DOWN): camera.rot[0] -= 2.5
    
    if window.key_held(key.LEFT): camera.rot[1] += 2.5
    if window.key_held(key.RIGHT): camera.rot[1] -= 2.5

def update(dt):
    window.fill(0.5, 0.7, 1.0)
    handle_fps_camera(window.camera, dt)
    window.render_model(Model())

window.set_update_func(update)
window.run()