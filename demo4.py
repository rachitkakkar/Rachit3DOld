# THIS IS A DEMO WHERE I USE MY ENGINE TO RENDER A FULL ROOM
from Rachit3D import *
import math

window = Window(width=800, height=600, caption='Demo4: A Map', resizable=True)
window.add_icon('icon.jpg')
window.camera = Camera((0, 1, 1.5),(0, 0, 0))

def handle_fps_camera(camera, dt):
    s = dt*8
    r = dt*150
    rotY = -camera.rot[1]/180*math.pi
    dx,dz = s*math.sin(rotY),s*math.cos(rotY)

    if window.key_held(key.W): camera.pos[0]+=dx; camera.pos[2]-=dz
    if window.key_held(key.S): camera.pos[0]-=dx; camera.pos[2]+=dz
    if window.key_held(key.A): camera.pos[0]-=dz; camera.pos[2]-=dx
    if window.key_held(key.D): camera.pos[0]+=dz; camera.pos[2]+=dx

    if window.key_held(key.SPACE): camera.pos[1]+=s
    if window.key_held(key.LSHIFT): camera.pos[1]-=s

    if window.key_held(key.UP): camera.rot[0] += r
    if window.key_held(key.DOWN): camera.rot[0] -= r
    if window.key_held(key.LEFT): camera.rot[1] += r
    if window.key_held(key.RIGHT): camera.rot[1] -= r

def update(dt):
    window.fill(0.5, 0.7, 1.0)
    handle_fps_camera(window.camera, dt)

    window.render(Wall((2.0, 4.0), (4.0, 4.0), 1.5, 'Textures/brick.jpg'))
    window.render(Wall((4.0, 4.0), (4.0, 3.0), 1.5, 'Textures/brick.jpg'))
    window.render(Wall((4.0, 3.0), (3.0, 2.0), 2.5, 'Textures/brick.jpg'))

    window.render(Wall((3.0, 2.0), (4.0, 1.0), 2.5, 'Textures/brick.jpg'))
    window.render(Wall((4.0, 1.0), (5.0, 1.0), 2.5, 'Textures/brick.jpg'))
    window.render(Wall((5.0, 1.0), (6.0, 2.0), 2.5, 'Textures/brick.jpg'))
    window.render(Wall((6.0, 2.0), (5.0, 3.0), 2.5, 'Textures/brick.jpg'))
    window.render(Layer((3.0, 2.0), (4.0, 1.0), (5.0, 1.0), (6.0, 2.0), 2.5, 'Textures/metal.jpg'))
    window.render(Layer((3.0, 2.0), (4.0, 3.0), (5.0, 3.0), (6.0, 2.0), 2.5, 'Textures/metal.jpg'))
    window.render(Layer((3.0, 2.0), (4.0, 3.0), (5.0, 3.0), (6.0, 2.0), 0, 'Textures/wood.jpg'))
    window.render(Layer((3.0, 2.0), (4.0, 1.0), (5.0, 1.0), (6.0, 2.0), 0, 'Textures/wood.jpg'))

    window.render(Wall((5.0, 3.0), (5.0, 4.0), 1.5, 'Textures/brick.jpg'))
    window.render(Wall((5.0, 4.0), (7.0, 4.0), 1.5, 'Textures/brick.jpg'))

window.set_update_func(update)
window.run()