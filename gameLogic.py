import random

class Game:
    def __init__(self):
        self.number = random.randint(1, 10)
        self.life = 4

    def true_false(self, choice):
        if len(choice) != 1:
            return False
        try:
            number_choice = int(choice)
        except ValueError:
            self.life -= 1
            return False
        if number_choice == self.number:
            return True
        else:
            self.life -= 1
            return False
    
    def get_lifes(self):
        return self.life