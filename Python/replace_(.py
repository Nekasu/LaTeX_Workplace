def replace(s:str):
    '''
    功能介绍：该函数用于将latex文章中公式与符号两侧的$、\(、\)、\[与\]替换为$，以方便粘贴到markdown文件中使用

    参数列表：
    1. s：字符串，代表需要处理的latex文章段

    返回值：
    1. s：字符串，处理后的latex文章段
    '''
    s = s.replace(' ','')


    s = s.replace('\(','$')
    s = s.replace('\)','$')

    s = s.replace('\[','$$')
    s = s.replace('\]','$$')
    
    return s

if __name__ == '__main__':
    i = True
    while i == True:
        s = input('Plz input the string:')
        
        if s == 'quit':
            i = False
            print("process quit")
        else:
           s = replace(s)
           print(f"\nhere is the result:\n {s}\n\n")