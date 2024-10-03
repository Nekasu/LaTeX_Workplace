def remove_dollor(s:str):
    '''
    功能介绍：该函数用于移除文件名中的空格，并添加下划线；去除文件名中的“.”符号, 以防止被系统错误的认为为文件扩展名. 以方便复制粘贴到文件名中

    参数列表：
    1. s：字符串，代表需要处理的文件名

    返回值：
    1. s：字符串，处理后的文件名
    '''
    s = s.replace(' ','_')
    s = s.replace('.', '_')
    
    return s

if __name__ == '__main__':
    i = True
    while i == True:
        s = input('Plz input the string:')
        
        if s == 'quit':
            i = False
            print("process quit")
        else:
           s = remove_dollor(s)
           print(f"\nhere is the result:\n{s}\n\n")