from pyglet.gl import *
from pyglet.window import key

from .Camera import Camera

class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.batch = pyglet.graphics.Batch()
        self.camera = Camera()
        
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)
        self.set_minimum_size(300, 200)

    def render(self, obj):
        if obj.type == 'wall':
            self.batch.add(4, GL_QUADS, obj.texture, ('v3f', (obj.x1, 0.0, obj.y1, obj.x2, 0.0, obj.y2, obj.x2, obj.height, obj.y2, obj.x1, obj.height, obj.y1)), obj.tex_coords)

        if obj.type == 'layer':
            self.batch.add(4, GL_QUADS, obj.texture, ('v3f', (obj.x1, obj.height, obj.y1, obj.x2, obj.height, obj.y2, obj.x3, obj.height, obj.y3, obj.x4, obj.height, obj.y4)), obj.tex_coords)

    def set_update_func(self, func): pyglet.clock.schedule(func)
    def run(self): pyglet.app.run()
    def fill(self, r, g, b): glClearColor(r, g, b, 1.0)
    def add_icon(self, icon): self.set_icon(pyglet.image.load(icon))
    
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

        self.batch.draw()

        glPopMatrix()

    def on_resize(self, width, height):
        glViewport(0, 0, width, height)