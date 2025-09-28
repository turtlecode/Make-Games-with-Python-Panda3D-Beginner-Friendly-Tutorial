from direct.showbase.ShowBase import ShowBase
from direct.task import Task

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Load the cube model
        self.cube = self.loader.loadModel("models/box")
        self.cube.reparentTo(self.render)
        self.cube.setScale(1, 1, 1)
        self.cube.setPos(0, 10, 0)

        # Movement speed
        self.speed = 0.1

        # Dictionary to track pressed keys
        self.keys = {"up": False, "down": False, "left": False, "right": False}

        # Bind key events
        self.accept("arrow_up", self.set_key, ["up", True])
        self.accept("arrow_up-up", self.set_key, ["up", False])

        self.accept("arrow_down", self.set_key, ["down", True])
        self.accept("arrow_down-up", self.set_key, ["down", False])

        self.accept("arrow_left", self.set_key, ["left", True])
        self.accept("arrow_left-up", self.set_key, ["left", False])

        self.accept("arrow_right", self.set_key, ["right", True])
        self.accept("arrow_right-up", self.set_key, ["right", False])

        # Add the update task
        self.taskMgr.add(self.update, "UpdateTask")

    def set_key(self, key, value):
        self.keys[key] = value

    def update(self, task):
        x, y, z = self.cube.getPos()

        if self.keys["up"]:
            z += self.speed
        if self.keys["down"]:
            z -= self.speed
        if self.keys["left"]:
            x -= self.speed
        if self.keys["right"]:
            x += self.speed

        self.cube.setPos(x, y, z)
        return Task.cont

app = MyApp()
app.run()