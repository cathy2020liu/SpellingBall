class Ball:
    life = 5

    def __init__(self):
        self.life = 5

    def move_right(self):
        self.life -= 1

    def is_fall(self) -> bool:
        return self.life == 0
