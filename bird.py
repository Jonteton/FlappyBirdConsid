class Bird:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.velocity = 0
        self.acceleration = 0
        self.img = img

    def render(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def up(self):
        self.velocity -= 0.12
        self.y = self.y + self.velocity

    def falling(self):
        self.velocity += 0.002
        self.y = self.y + self.velocity
