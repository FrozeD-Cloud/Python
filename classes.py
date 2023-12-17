class Cookie:
    def __init__(self, colour):
        self.colour = colour
    def get_colour(self):
        return self.colour
    def set_colour(self,colour):
        self.colour = colour
        

    
cookie_1 = Cookie('green')

print(cookie_1.get_colour())


