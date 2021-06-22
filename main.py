from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

#CUBE (VOXEL) CLASS
class Voxel(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = 'white_cube',
            color = color.white,
            highlight_color = color.lime)

#ONCLICK CREATE CUBE
    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position = self.position + mouse.normal)

app = Ursina()

for z in range(15):# in one dir
    for x in range(15):# in the other dir
        voxel = Voxel(position = (x,0,z))# make blocks

player = FirstPersonController()

app.run()