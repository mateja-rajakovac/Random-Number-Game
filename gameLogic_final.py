import random

class Game:
    def __init__(self):
        self.number = random.randint(1, 10)
        self.life = 4

    def true_false(self, choice):
        try:
            number_choice = int(choice)
        except ValueError:
            return "INVALID_INPUT"
        if number_choice < 1 or number_choice > 10:
            return "INVALID_INPUT"
        if number_choice == self.number:
            return "CHOICE_WON"
        else:
            self.life -= 1
            return "FALSE_INPUT"

    def game_over(self, choice):
        if self.get_lifes() <= 0:
            return True
        else:
            return False

    def get_lifes(self):
        return self.life