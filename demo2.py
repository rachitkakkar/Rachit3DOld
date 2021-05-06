# THIS IS A DEMO WHERE I USE MY ENGINE TO RENDER A BRICK WALL
from Rachit3D import *
import math

window = Window(width=800, height=600, caption='Demo2: A Wall', resizable=True)
window.camera = Camera((0.5, 1.5, 1.5),(-30, 0, 0))

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
    window.render(Wall((0.0, 0.0), (1.0, 0.5), 1.5, 'Textures/brick.jpg'))
    window.render(Wall((0.0, 0.0), (-1.0, 0.5), 1.5, 'Textures/brick.jpg'))
    window.render(Wall((1.0, 0.5), (2.0, 0.5), 1.5, 'Textures/brick.jpg'))

window.set_update_func(update)
window.run()