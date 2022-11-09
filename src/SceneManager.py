class SceneManager(object):
    def __init__(self, scene):
        # ? Scene stack
        self.stackScene = []

        # ? Initiate first scene
        self.gotoScene(scene)
    
    def gotoScene(self, scene):
        self.scene = scene()
        self.scene.update()

    def callScene(self, scene):
        self.scene.stop()
        self.stackScene.append(self.scene)
        self.scene = scene()

    def backScene(self):
        self.scene = self.stackScene.pop()
        self.scene.start()