# ? Import Dependencies for class object usage 
from src import Globe 

class StartScene(object):
    def __init__(self):
        self.selectIndex = 0

        # ? Click or not?
        self.confirm = False

    def update(self):
        if self.confirm == False:
            pass
        else:
            if self.selectIndex == 0: # ? Start
                Globe.Game.SceneManager.gotoScene()

    def draw(self, screen):
        pass