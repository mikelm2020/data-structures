from grid import Grid
from custom_array import Array


class Cube:
    def __init__(self, axes, rows, columns, fill_value=None):
        self.area = Array(axes)
        for axe in range(axes):
            self.area[axe] = Grid(rows, columns, fill_value)

    def get_depth(self):
        return len(self.area)

    def get_height(self):
        return self.area[0].get_height()

    def get_width(self):
        return self.area[0].get_width()

    def __getitem__(self, index):
        return self.area[index]

    def __str__(self):
        result = ""
        for axe in range(self.get_depth()):
            result += f"Matrix {axe} \n"
            for row in range(self.get_height()):
                for col in range(self.get_width()):
                    result += str(self.area[axe][row][col]) + " "

                result += "\n"
            result += "\n"

        return str(result)

    def __random_fill__(self):
        import random

        for axe in range(self.get_depth()):
            for row in range(self.get_height()):
                for col in range(self.get_width()):
                    self.area[axe][row][col] = random.randint(1,100)

    if __name__ == '__main__':

        from cube import Cube
        cubex = Cube(2, 3, 4)
        print(f"La profundidad es: {cubex.get_depth()} el alto es {cubex.get_height()} y el largo es {cubex.get_width()}")
        cubex.__random_fill__()
        print(cubex.__str__())
        