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
    # while i == True:
        # s = input('Plz input the string:')
    s ='''
Method	Backbone	Depth	Img_size	Seg(val)	Seg(test)
ToCo	vit-small-patch16-224	8	$224\\times 224$	55.0	52.7
SS-EPA	vit-small-patch16-224	8	$224\\times 224$	57.6	50.2
ToCo	vit-base-patch16-384	12	$384\\times 384$	71.1	71.8
SS-EPA	vit-base-patch16-384	12	$384\\times 384$	71.7	71.9
ToCo	vit-base-patch16-224	12	$224\\times 224$	71.1	72.2
SS-EPA	vit-base-patch16-224	12	$224\\times 224$	72.4	73.3
    '''
    
    if s == 'quit':
        i = False
        print("process quit")
    else:
        s = remove_dollor(s)
        # s += '\\\\'
        print(f"\nhere is the result:\n{s}\n\n")
        pyperclip.copy(s)
        print("结果已复制到剪贴板！")