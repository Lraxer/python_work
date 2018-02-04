from random import choice
import matplotlib.pyplot as plt 


class RandomWalk():
    def __init__(self, num_points=5000):
        self.num_points = 5000
        self.x_values = [0]
        self.y_values = [0]
    
    def get_step(self):
        direction = choice([1,-1])
        distance = choice([0,1,2,3,4])
        step = direction * distance
        return step

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

def hide():
    """隐藏坐标轴"""
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

if __name__  ==  '__main__':
    while True:
        rw = RandomWalk(50000)  #直接修改__init__中的参数值
        rw.fill_walk()

        point_numbers = list(range(rw.num_points))
        plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,s=1)
        
        # 突出起点终点
        # plt.scatter(0,0,c='green',s=70)
        # plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',s=70)

        hide()

        plt.show()

        keep_running = input("Make another walk(y/n)?")
        if keep_running == 'n':
            break;