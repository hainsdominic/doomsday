class Meteor:
    def __init__(self, image, initial_x, initial_y, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(initial_x, -100)

    def move(self):
        self.pos = self.pos.move(0, self.speed)
