class SceneManager(object):
    def __init__(self, sceneList, sceneName):
        self.scene = None

        # ? Scene list
        self.sceneList = sceneList

        # ? Scene stack
        self.stackScene = []

        # ? Initiate first scene
        self.gotoScene(sceneName)
    
    def gotoScene(self, sceneName): # ? Go to next scene without saving previous scene
        self.scene = self.sceneList[sceneName]()

    def callScene(self, sceneName): # ? Change scene and saving the previous scene
        self.stackScene.append(self.scene)
        self.scene = self.sceneList[sceneName]()

    def backScene(self): # ? Back to previous scene
        self.scene = self.stackScene.pop()