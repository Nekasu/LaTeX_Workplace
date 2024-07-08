import random

path = './pos.txt'

with open(path, 'w') as f:
    for i in range(1,100):
        # 生成第一个随机数，在[1, 11]闭区间内  
        random_num1 = random.randint(1, 11)

        # 生成第二个随机数，只能是1或2
        random_num2 = random.choice([1, 2])

        # 生成第三个随机数，只能是1, 2, 3中的任意一个
        random_num3 = random.choice([1, 2, 3])
        
        random_num4 = random.randint(1,22)
        
        if random_num2 == 1:
            lan = '左'
        else:
            lan = '右'
            
        if random_num3 == 1:
            pos = '上面'
        elif random_num3 == 2:
            pos = '中间'
        else:
            pos = '下面'
        
        if random_num4 < 11:
            f.write(f"第{i}条引用, 在第{random_num1}页, {lan}栏, {pos}部分, 使用第{random_num4}篇文献\n")
        else:
            f.write(f"第{i}条引用, 在第{random_num1}页, {lan}栏, {pos}部分, 使用倒数第{23-random_num4}篇文献\n")