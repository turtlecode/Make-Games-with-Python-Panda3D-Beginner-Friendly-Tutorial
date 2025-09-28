from direct.showbase.ShowBase import ShowBase
from direct.task import Task
import random

class SimpleGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Camera setup
        self.camera.setPos(0, -20, 10)
        self.camera.lookAt(0, 10, 0)

        # Player cube
        self.player = self.loader.loadModel("models/box")
        self.player.reparentTo(self.render)
        self.player.setPos(0, 10, 0)
        self.player.setColor(0, 0, 1, 1)  # Blue

        # Goal cube
        self.goal = self.loader.loadModel("models/box")
        self.goal.reparentTo(self.render)
        self.goal.setScale(0.7)  # Make it more visible
        self.goal.setPos(3, 10, 0)
        self.goal.setColor(1, 0, 0, 1)  # Red

        # Movement speed
        self.speed = 0.2

        # Dictionary to track pressed keys
        self.keys = {"up": False, "down": False, "left": False, "right": False}

        # Counter for how many times player reached goal
        self.goal_count = 0

        # Key events
        self.accept("arrow_up", self.set_key, ["up", True])
        self.accept("arrow_up-up", self.set_key, ["up", False])
        self.accept("arrow_down", self.set_key, ["down", True])
        self.accept("arrow_down-up", self.set_key, ["down", False])
        self.accept("arrow_left", self.set_key, ["left", True])
        self.accept("arrow_left-up", self.set_key, ["left", False])
        self.accept("arrow_right", self.set_key, ["right", True])
        self.accept("arrow_right-up", self.set_key, ["right", False])

        # Update task
        self.taskMgr.add(self.update, "UpdateTask")

    def set_key(self, key, value):
        self.keys[key] = value

    def update(self, task):
        x, y, z = self.player.getPos()

        if self.keys["up"]:
            z += self.speed
        if self.keys["down"]:
            z -= self.speed
        if self.keys["left"]:
            x -= self.speed
        if self.keys["right"]:
            x += self.speed

        self.player.setPos(x, y, z)

        # Check if player reached the goal (X-Z plane)
        px, py, pz = self.player.getPos()
        gx, gy, gz = self.goal.getPos()
        distance = ((px - gx)**2 + (pz - gz)**2)**0.5  # Ignore Y axis
        if distance < 1.0:  # Collision threshold
            self.goal_count += 1
            print(f"Congratulations! You reached the goal! Count: {self.goal_count}")
            
            # Move goal to a new safe position within camera view
            new_x = random.uniform(-2, 2)  # Keep within camera bounds
            new_z = random.uniform(-2, 2)
            self.goal.setPos(new_x, 10, new_z)

        return Task.cont

app = SimpleGame()
app.run()
