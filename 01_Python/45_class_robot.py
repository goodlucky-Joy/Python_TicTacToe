class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print("initializing {}".format(self.name))
        Robot.population += 1
        
    def die(self):
        print("{}is being destroyed!".format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))
    
    def say_hi(self):
        print("Hi, my name is {}".format(self.name))
    
    @classmethod # 데코레이터
    def how_many(cls):
        print("We have {:d} robots\n".format(cls.population))


droid1 = Robot("R001")
droid1.say_hi()	  #객체.메소드()
Robot.how_many()	#클래스.메소드()

droid2 = Robot("R002")
droid2.say_hi()   #객체.메소드()
Robot.how_many()  #클래스.메소드()

droid1.die()      #객체.메소드()
Robot.how_many()  #클래스.메소드()

droid2.die()      #객체.메소드()
Robot.how_many()  #클래스.메소드()
