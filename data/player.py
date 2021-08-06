class Player:
    def __init__(self, image, initial_x, initial_y, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(initial_x, initial_y)

    def move(self, x):
        self.pos = self.pos.move(x * self.speed, 0)
