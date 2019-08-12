import random
class Food:
    def __init__(self):
        self.x_coordinate = random.randint(2,78)
        self.y_coordinate = random.randint(2,23)
        type = random.randint(0,99)
        if type <=9 :
            self.type_food = 0 #0 == bad food (*)
        else:
            self.type_food = 1 #1 == good food (+)
    
    def print(self):
        print('x-coordinate: ', self.x_coordinate)
        print('y-coordinate: ', self.y_coordinate)
        if self.type_food==1:
            print('+')
        else:
            print('*')

    def getX(self):
        return self.x_coordinate
    def getY(self):
        return self.y_coordinate
    def getFood(self):
        if self.type_food==1:
            return '+'
        else:
            return '*'