'''
3. Дан список заполненный произвольными целыми числами.
Получите новый список, элементами которого будут только уникальные элементы исходного.
'''

list1=[1,1,3,4,4,6]
list2=[]
for i in list1:
    if list1.count(i)==1:
        list2.append(i)

print(list2)