from robot import Robot
from robot import Person

if __name__ == "__main__":
    robot1 = Robot("Tom", "red", 30)
    robot2 = Robot("Jerry", "blue", 40)

    robot1.introduce_self()
    robot2.introduce_self()

    person1 = Person("Alice", "aggressive", False, robot1)
    person1.robotOwned.introduce_self()
