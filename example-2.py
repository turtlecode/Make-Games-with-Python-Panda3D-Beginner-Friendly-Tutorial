from direct.showbase.ShowBase import ShowBase
from panda3d.core import NodePath
from panda3d.core import GeomNode

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        cube = self.loader.loadModel("models/box")
        cube.reparentTo(self.render)
        cube.setScale(1, 1, 1)
        cube.setPos(0, 10, 0)

app = MyApp()
app.run()