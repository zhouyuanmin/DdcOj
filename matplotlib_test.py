import argparse
import base64
from matplotlib_oj import review_matplotlib

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Matplotlib oj for python')
    parser.add_argument('--answer', help='give the answer of matplotlib', default="{'ddcmaker':'1'}")
    parser.add_argument('--data', help='give the user code', default='print("error")')
    parser.add_argument('--scores', help='give scores', default='0')
    parser.add_argument('--match', default=0.9)
    parser.add_argument('--debug', default="False")
    args = parser.parse_args()
    answer = eval(base64.b64decode(args.answer.encode()))
    data = base64.b64decode(args.data.encode()).decode()
    scores = eval(base64.b64decode(args.scores.encode()))
    match = float(args.match)
    debug = args.debug
    test_data = {
        'code': data,
        'answer': answer,
        'match': match,
        'scores': scores
    }
    _data = test_data
    # print(test_data)

    # 测试结果
    _data_ = {
        'code': """
from matplotlib import pyplot as plt
from random import choice


class RandomWalk(object):
    def __init__(self, num_points=5000):
        self.num_points = num_points  # 坐标点的个数
        self.x_values = [0]  # x坐标
        self.y_values = [0]  # y坐标

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            # 方向
            x_direction = choice([1, -1])
            y_direction = choice([1, -1])
            # 距离
            x_distance = choice([0, 1, 2, 3, 4])
            y_distance = choice([0, 1, 2, 3, 4])

            if x_distance != 0 or y_distance != 0:
                # 下一个点的坐标
                next_x = self.x_values[-1] + x_direction * x_distance
                next_y = self.y_values[-1] + y_direction * y_distance

                # 将坐标点添加到属性中
                self.x_values.append(next_x)
                self.y_values.append(next_y)


plt.figure()
rw = RandomWalk(5000)
rw.fill_walk()
a = plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
    """,
        'answer': {
            'x': '3f72eb5354f62ec74033a4d674c52d9b',
            'y': '152122e1726775ea3da02b74c90c1066'
        },
        'scores': {
            'x': 50,
            'y': 50
        },
        'match': 0.9
    }
    # _data = _data_
    _result = review_matplotlib(
        code=_data.get('code'),
        answer=_data.get('answer'),
        match=_data.get('match'),
        scores=_data.get('scores'),
        debug=False
    )
    print(_result)
