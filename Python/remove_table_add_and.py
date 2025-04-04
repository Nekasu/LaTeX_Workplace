import pyperclip
#  使用 pyperclip.copy() 方法将字符串复制到剪贴板

def remove_dollor(s:str):
    '''
    功能介绍：该函数用于移除文件名中的table，并添加符‘&’；并在最后加上双反斜杠'\\'，用于复制Word表格到LaTeX表格中

    注意！需要一行一行复制

    参数列表：
    1. s：字符串，代表需要处理的文件名

    返回值：
    1. s：字符串，处理后的文件名
    '''
    s = s.replace('\t',' & ')
    s = s.replace('\n',' \\\\')

    return s

if __name__ == '__main__':
    i = True
    while i == True:
        s = input('Plz input the string:')
    # s ='''1	1	0	0	0	0	0	0	0	0	0
    # '''
        if s == 'quit':
            i = False
            print("process quit")
        else:
            s = remove_dollor(s)
            # s += '\\\\'
            print(f"\nhere is the result:\n{s}\n\n")
            pyperclip.copy(s)
            print("结果已复制到剪贴板！")