"""
This script counts the occurrence of names across multiple lists, each representing authors of different academic papers on style transfer techniques.

The `name_list_create` function takes a list of names and a dictionary. It iterates through the list, checking if each name already exists in the dictionary. If the name is not present, it adds the name with a count of 1. If the name is already in the dictionary, it increments the count.

The main script:
1. Defines several name lists, each representing authors from different academic papers.
2. Initializes an empty dictionary `full_name_list` to store the names and their counts.
3. Loops through the 8 name lists (from `nameList1` to `nameList8`), calling `name_list_create` to update `full_name_list` with the counts of each author's occurrences.
4. Prints the updated dictionary after processing each list, showing the accumulation of name frequencies across the lists.

This approach helps in identifying the most frequent contributors to the academic papers listed.
"""
import os

from tomlkit import value

def name_list_create(name_list1, name_dict):
    for name in name_list1:
        if name not in name_dict:
            name_dict[name] = 1
        elif name in name_dict:
            name_dict[name] += 1
    
    return name_dict

if __name__ == '__main__':
    # ArtBank: Artistic Style Transfer with Pre-trained Diffusion Model and Implicit Style Prompt Bank
    nameList1 = ['Zhanjie Zhang', 'Quanwei Zhang', 'Guangyuan Li', 'Wei Xing', 'Lei Zhao', 'Jiakai Sun', 'Zehua Lan', 'Junsheng Luan', 'Yiling Huang', 'Huaizhong Lin']
    
    # Rethink arbitrary style transfer with transformer and contrastive learning
    nameList2 = ['Zhanjie Zhang', 'Jiakai Sun', 'Guangyuan Li', 'Lei Zhao', 'Quanwei Zhang', 'Zehua Lan', 'Haolin Yin', 'Wei Xing', 'Huaizhong Lin']
    
    # StyleSinger: Style Transfer for Out-of-Domain Singing Voice Synthesis
    nameList3 = ['Yu Zhang', 'Rongjie Huang', 'Ruiqi Li', 'JinZheng He', 'Yan Xia', 'Feiyang Chen', 'Xinyu Duan', 'Baoxing Huai', 'Zhou Zhao']
    
    # AdaCM: Adaptive ColorMLP for Real-Time Universal Photo-Realistic Style Transfer
    nameList4 = ['Honglin Lin', 'Yong Liu']
    
    # MicroAST: Towards Super-fast Ultra-Resolution Arbitrary Style Transfer
    nameList5 = ['Zhizhong Wang', 'Lei Zhao', 'Zhiwen Zuo', 'Ailin Li', 'Haibo Chen', 'Wei Xing', 'Dongming Lu']
    
    # Preserving Structural Consistency in Arbitrary Artist and Artwork Style Transfer
    nameList6 = ['Jingyu Wu', 'Lefan Hou', 'Zejian Li', 'Jun Liao', 'Li Liu', 'Lingyun Sun']
    
    # StyleDiffusion: Controllable Disentangled Style Transfer via Diffusion Models
    nameList7 = ['Zhizhong Wang', 'Lei Zhao', 'Wei Xing']
    
    # AesUST: Towards Aesthetic-Enhanced Universal Style Transfer
    nameList8: list[str] = ['Zhizhong Wang', 'Zhanjie Zhang', 'Lei Zhao', 'Zhiwen Zuo', 'Ailin Li', 'Wei Xing', 'Dongming Lu']
    
    list_name = 'nameList'
    
    full_name_dict = {}
    
    file_path = './name.txt'
    dir_name = os.path.dirname(file_path) 
    
    # 检查并创建目录（如果不存在）
    if dir_name and not os.path.exists(dir_name):
        os.makedirs(dir_name)
        
    with open(file = './name.txt', mode='w') as f:
        for i in range(8):
            str_i = str(i+1)
            list_name_num  = list_name + str_i
            # print(eval(list_name_num))
            full_name_dict = name_list_create(eval(list_name_num), full_name_dict)
            

        sorted_name_dict =sorted(full_name_dict.items(), key=lambda item: item[1], reverse=True)
            
        f.write(f"{sorted_name_dict}")
    