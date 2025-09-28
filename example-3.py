from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Load the cube model
        self.cube = self.loader.loadModel("models/box")
        self.cube.reparentTo(self.render)
        self.cube.setScale(1, 1, 1)
        self.cube.setPos(0, 10, 0)

        # Movement speed (step size)
        self.speed = 0.5

        # Bind arrow key controls
        self.accept("arrow_up", self.move_up)
        self.accept("arrow_down", self.move_down)
        self.accept("arrow_left", self.move_left)
        self.accept("arrow_right", self.move_right)

    def move_up(self):
        # Increase the Z value to move upward
        x, y, z = self.cube.getPos()
        self.cube.setPos(x, y, z + self.speed)

    def move_down(self):
        # Decrease the Z value to move downward
        x, y, z = self.cube.getPos()
        self.cube.setPos(x, y, z - self.speed)

    def move_left(self):
        # Decrease the X value to move left
        x, y, z = self.cube.getPos()
        self.cube.setPos(x - self.speed, y, z)

    def move_right(self):
        # Increase the X value to move right
        x, y, z = self.cube.getPos()
        self.cube.setPos(x + self.speed, y, z)

# Create the app and run it
app = MyApp()
app.run()