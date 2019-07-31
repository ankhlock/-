def addfenci(s, l):
    import jieba
    str2 = ''
    cut = jieba.cut(s, cut_all=False)
    f = ' '.join(cut)
    s = f
    for i in range(0, len(s)):
        if s[i] != " ":
            str2 += s[i]
        else:
            l.append(str2)
            str2 = ''
    l.append(str2)

def listaddfenci(lis,new_lis):
    l=[]
    for i in range(0,len(lis[1].split('。'))):
        l=[]
        addfenci(lis[1].split('。')[i],l)
        l = Filter_Discontinuation_Word(l)
        new_lis.append(l)

# 整理结构
def Filter_Discontinuation_Word(list_F):
    list_tc = ['','\\','r','n','"', ':', ',', '，', '\u3000', '\n', '\t', '丶', '#', '\ufeff', '《', '》', '、', '／', '：', '（', '）', '△']
    i = 0
    j = 0
    list_G = list_F[:]
    while i < len(list_F):
        j = 0
        while j < len(list_tc):
            if list_F[i] == list_tc[j]:
                list_G.remove(list_F[i])
                break
            else:
                j += 1
        i += 1
    return list_G

def split_word(list_wb,list_cx):
    point=0
    flag=0
    for i in range(0,len(list_wb)-2):
        sign=0
        for j in range(0,len(list_cx)):
            for k in range(i,i+3):
                for f in range(0,len(list_wb[k])):
                    if list_wb[k][f]==list_cx[j]:
                        sign+=1
        if sign>flag:
            flag=sign
            point=i
    for i in range(point,point+3):
        for j in range(0,len(list_wb[i])):
            print(list_wb[i][j],end='')



sy_load = 'D:\\zlw文件\\python\\python练习程序\\考试题\\law_data\\实验文本.txt'
list_sy = open(sy_load, 'r', encoding="GBK").readlines()
open(sy_load,'r',encoding="GBK").close
new_list_sy = []

listaddfenci(list_sy, new_list_sy)


print(list_sy[1].split('。'))
print(new_list_sy)

list_cx=['2015', '年', '9', '月', '10', '日', '被', '庆阳市', '公安局', '西峰', '分局', '刑事拘留']
print('查询:',list_cx)
split_word(new_list_sy,list_cx)
