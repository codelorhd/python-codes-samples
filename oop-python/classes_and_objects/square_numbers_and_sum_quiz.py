class Point:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        sqX = self.x**2
        sqY = self.y**2
        sqZ = self.z**2

        return sum([sqX, sqY, sqZ])
