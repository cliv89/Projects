from ursina import*
import random
from ursina.prefabs.hot_reloader import*
app = Ursina()


num0 = load_texture("0.png")
num1 = load_texture("1.png")
num2 = load_texture("2.png")
num3 = load_texture("3.png")
num4 = load_texture("4.png")
num5 = load_texture("5.png")
num6 = load_texture("6.png")
num7 = load_texture("7.png")
num8 = load_texture("8.png")
num9 = load_texture("9.png")
nums = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]

window.fullscreen = False

class Flappy(Entity):
    def __init__(self):
        super().__init__(
            model = "cube",
            scale = (0.8, 0.7, 0.001),
            texture = load_texture("jumping.png"),
            collider = "box",
            z = -1
            )

    def update(self):
        self.y -= 2*time.dt
        if held_keys["space"]:
            self.texture = load_texture("falling.png")

        else:
            self.texture = load_texture("jumping.png")
        if self.y <= -2.6:
            self.y = 1

    def input(self, key):
        if key == "space":
            self.y += 0.7
            sound = Audio('wing.ogg', volume=2)

class Background(Entity):
    def __init__(self):
        super().__init__(
            model = "cube",
            scale = (25, 8.5, -1),
            texture = load_texture("background"))

    def update(self):
        self.x -= 0.5*time.dt
        if self.x <= -2.5:
            self.x = 5.18

class Base(Entity):
    def __init__(self):
        super().__init__(
            model = "cube",
            y = -3.5,
            scale = (26, 1.6, 0.001),
            texture = load_texture("base"),
            z = -2
        )

    def update(self):
        self.x -= 2.5*time.dt
        if self.x <= -5:
            self.x = 5.8
point_count = 0
index = 0
score_pos = -1

class Pipe(Entity):
    def __init__(self,rotation=(0, 0, 0), x = 7, y = -2):
        super().__init__(
            model = "cube",
            y = y,
            x = x,
            scale = (0.8, 4.3, 0.001),
            texture = load_texture("pipe.png"),
            collider = "box",
            rotation = rotation,
            z = -1
            )

    def update(self):
        self.x -= 2*time.dt
        global point_count
        global score_pos
        global index
        if self.x <= crash.x + 0.007:
            if self.x >= crash.x - 0.001:
                point_count += 1

                # if point_count == 2:
                #     point_count = 1
                #     index += 1
                #     score_pos -= 0.001
                #     Level(nums[index], z = score_pos)
                #     #print(index)
                #     if index >= 9:
                #         index = 0

class Level(Entity):
    def __init__(self, texture = num0, x = 0.2, z = -0.1):
        super().__init__(
            model = "cube",
            texture = texture,
            scale = (0.4, 0.5, 0.01),
            z = z,
            x = x,
            y = 2
            )

Base()

def pipe_len():
    pipe_dist = 0
    # pipe_count = 0
    # global pipe_count

    for i in range(90):
        pipe_dist += 3.5
        pipe_height = random.uniform(-4.5, -1.5)
        start = Pipe(x = 7 + pipe_dist, y = pipe_height)
        pipe_open = start.y + 6.7
        pipe_orientation = Pipe(rotation = (0, 0, 180), y = pipe_open, x = start.x)

crash = Flappy()

Background()

def update():
    crash_hit = crash.intersects()

    if crash_hit.hit:
        sound = Audio('hit.wav', volume = 2)
        crash.rotation = (0, 0, 180)
        application.pause()
        gameover = Entity(model="cube", texture=load_texture("crashover1.png"), z= -3, scale =(6.5, 3.8), x= 0.01, y = 0)

pipe_len()
 
def input(key):

    if held_keys["q"]:
        application.quit()

    if key == "r":
        window.fullscreen = False

app.run()