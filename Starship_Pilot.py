import pyglet
from pyglet.window import key

window = pyglet.window.Window(fullscreen=True)

pyglet.resource.path.append('./images')
pyglet.resource.reindex()

def center_anchor(img):
    img.anchor_x = img.width // 2
    img.anchor_y = img.height // 2

planet_image = pyglet.image.load('Saturn_1.png')
center_anchor(planet_image)

class Planet(pyglet.sprite.Sprite):
    def __init__(self, image, x=0, y=0, batch=None):
        super(Planet, self).__init__(
            image, x, y, batch=batch)
        self.x = x
        self.y = y

center_x = int(window.width/2)
center_y = int(window.width/2)

planet = Planet(planet_image, center_x, center_y, None)

@window.event
def on_draw():
    window.clear()
    planet.draw()


ship_image = pyglet.image.load('ship.png')
center_anchor(ship_image)

class Ship(pyglet.sprite.Sprite):
    def __init__(self, image, x=0, y=0,
                 dx=0, dy=0, rotv=0, batch=None):
        super(Ship, self).__init__(
            image, x, y, batch=batch)
        self.x =x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.rotation = rotv
        self.thrust = 200.0
        self.rot_spd = 100.0
        self.rot_left = False
        self.rot_right = False
        self.engines = False
    def update(self, dt):
        if self.rot_left:
            self.rotation -= self. rot_spd * dt
        of self.rot_right:
            self.rotation += self.rot_spd * dt
    def update(dt):
        ship.update(dt)
    pyglet.clock.schedule_interval(update, 1/60.0)
    

ship = Ship(ship_image, x=center_x + 300, y=center_y,
            dx=0, dy=150, rotv=-90)

@window.event
def on_draw():
    window.clear()
    planet.draw()
    ship.draw()


from pyglet.window import key
@window.event

def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
        ship.rot_left = True
    if symbol == key. RIGHT:
        ship.rot_right = True
    if symbol == key.Up:
        ship.engines = True

@window.event
def on_key_release(symbol, modifiers):
    if symbol == key.LEFT:
        ship.rot_left = False
    if symbol == key. RIGHT:
        ship.rot_right = False
    if symbol == key.Up:
        ship.engines = False


        

pyglet.app.run()


