'''
1. Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.

    Примечание: Списки фруктов создайте вручную в начале файла.

'''


magnit=['яблоки','груши','бананы','апельсины','киви']
lenta=['киви','бананы','фейхоа','фезалис','арбуз']

result=[fruct for fruct in lenta if fruct in magnit]

print (result)