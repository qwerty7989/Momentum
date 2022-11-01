from src.Dependencies import *

class main(object):
    def __init__(self):
        # ? System Screen / Resolution
        self.screen = pygame.display.set_mode(
            [WINDOW_WIDTH , WINDOW_HEIGHT],
            pygame.RESIZABLE,
            vsync = 1)

        self.RUNNING = True
        self.run()

    def run(self):
        while self.RUNNING == True:
            pygame.display.flip()

if __name__ == "__main__":
    pygame.init()

    main()

    pygame.quit()
