# coding=utf-8
class Robot:
    ''' 表示一个带有名字的机器人'''
    # 一个类变量, 用来计数机器人的数量
    population = 0

    def __init__(self,name):
        ''' 初始化数据 '''
        self.name = name
        print(f'Initializing{self.name}')

        # 当有人被创建时
        # 将会增加人口数量
        Robot.population += 1
    
    def die(self):
        '''我挂了'''
        print(f'{self.name}is being destroyes!')
        Robot.population -= 1

        if Robot.population == 0:
            print(f'{self.name}was the last one')
        else:
            print(f'There are still {Robot.population} robots working')
    
    def say_hi(self):
        ''' 来自机器人的诚挚问候'''
        print(f'Greetings, my masters call me {self.name}')

    @classmethod
    def how_many(cls):
        '''打印当前人口数量'''
        print(f'We have {cls.population} robots.')

droid1 = Robot('R2-D2')
droid1.say_hi()
Robot.how_many()

droid2 = Robot('C-3PO')
droid2.say_hi()
Robot.how_many()

print('\nRobots can do some work here.\n')

print('Robots have finished their work. So let\'s destroy them.')
droid1.die()
droid2.die()

Robot.how_many()