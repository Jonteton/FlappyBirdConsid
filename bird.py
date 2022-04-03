

class Bird:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.velocity = 0
        self.acceleration = 0
        self.img = img

        self.center_x = x + img.get_width()/2
        self.center_y = y + img.get_height()/2

    def render(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def up(self, dt):
        self.velocity -= 30 * dt/1000
        self.y = self.y + self.velocity

    def falling(self, dt):
        self.velocity += 0 * dt/1000
        self.y = self.y + self.velocity

    def update_center_point(self):
        self.center_x = self.x + self.img.get_width() / 2
        self.center_y = self.y + self.img.get_height() / 2
