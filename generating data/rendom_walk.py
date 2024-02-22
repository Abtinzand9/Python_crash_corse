from random import choice

class RandomWalk :
    """a class to genererate random numbers"""
    def __init__(self , num_points = 5000):
        """initialize the random walk"""
        self.num_points = num_points

        # start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """calculate all points in walk"""
        # keep taking steps untill we reach the limit determined
        while len(self.x_values) < self.num_points:
            # randomly choose a direction
            x_direction = choice([-1 , 1])
            y_direction = choice([-1 , 1])
            # randomly choice how far it goes
            x_distance = choice([0,1,2,3,4])
            y_distance = choice([0,1,2,3,4])
            # take setps
            x_step = x_direction * x_distance
            y_step = y_direction * y_distance
            # reject moves that go nowhere 
            if x_step==0 and y_step == 0:
                continue
            # calculate the new position
            x= self.x_values[-1] +x_step
            y = self.y_values[-1] + y_step
            # add points to lists 
            self.x_values.append(x)
            self.y_values.append(y)