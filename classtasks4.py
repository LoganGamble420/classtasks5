import numpy as np
import random


print('2.1')
lst = ['logan',21,3.1]
lst2 = [1,2,3,4]
lst3= lst + lst2
print(lst3)
print(lst3[0])
print(lst3[-1])
lst3[5]='gorilla'
print('list.sort(lst3) does not work because different data types are not sortable \n')

print('2.2')
rand_lst = [random.randint(1,6) for iter in range(5)]
print(rand_lst)
rand_lst.reverse()
print(rand_lst)
rand_lst.sort()
print(rand_lst)
rand_lst.pop()
print(rand_lst)
print('The two ways are using -1 to index the last number in the array, or') 
print('leaving it blank because the pop function defaults to the last value')
rand_lst.insert(3, 2.17)
print(rand_lst)

print('\n2.3')
star_id = [12,434,24,3463,437]
mass = [1,0.5,4,6,4,]
print(mass.index(4))
print('index of values less than 1: ' + str(mass.index(min(mass))))
radius = [1,2,0.5,6,4]
print(str(radius.index(min(radius)))+ ' radius.index(min(radius)) is the code i used')
val = radius.index(min(radius)) 
print('star_id is: ' + str(star_id[val]))
print('mass is: ' + str(mass[val]))

print('\n2.4')
name=['l','o','g','a','n']
print(name)
x1=0
x2=10
lstrange=[x*0.5 for x in range(x1,x2+1)]
print(lstrange)
x=[1,-1,3,-5,-6,7]
x3 = [i for i in x if i >= 0]
print(x3)
a = [[1,1,1],[2,2,2],[3,3,3]]
flat_a=[i for sublist in a for i in sublist]
print(flat_a)

print('\n3.1')
print('A big difference between dictionaries and lists is that within dictionaries the order does not matter, which is not the case with lists ')
print('A similarity is that they are both sets of objects')
print('Within a dictionary a key is what can be refrenced by the program and the value is what the dictionary will return when the key is called')
print('You can create an empty dictionary, you can create a dictionary lke this dict = {"key" : Value, ...}, you can also create one like this dictionary = dict( key = Value, ...), finally by creating a list of tuples like this ')
print(' listDict = [("key" : Value, ...)]')
print(' When printing a dictionary it doesnt matter the order it outputs in, because dictionaries do not have a defined order and are accessed by called specific keys that have values attached to them')

print('\n3.2')
d = { "name" : 'Logan', 'stats' : [98,80,88] , 'percentage' : 57.88}
lst = d['stats']
print(lst[1])
d['wins']=['charlotte','houston','LA']
print(d.values())
print(d.keys())
print(d.items())
print(' Values is what the return is when the key is called. the items shows them together.')
lst.append(92) 
d['stats']=lst
print(d)

print('\n3.3')
mov = {'name': 'Interstellar' , 'year': 2014 , 'profit' : 69350000.92, 'cast' : ['Matthew mcconaughey','Anne hatheway', 'Jessica chastain', 'Micheal caine', 'John lithgow']}
print(mov)
print('It did print it in the same order I entered it, Howevere it wouldnt matter because dictionaries do not depend on their order')
lst2 = mov['cast'] 
print(lst2[0])
mov['year'] = 2016
mov = {'name': ['Interstellar','Fantasia'] , 'year': [2014,1940] , 'profit' : [69350000.92,7641000.78], 'cast' : (['Matthew mcconaughey','Anne hatheway', 'Jessica chastain', 'Micheal caine', 'John lithgow'],['Beethoven', 'Stravinsky', 'Schubert', 'Stokowski', 'Matheson'])}
print(mov)

print('\n3.4')
car = {'brand': ['volkswagen ','telsa '], 'model':['super beetle ','x '], 'year':[1978,2020], 'color':[' Checkerboard ',' Yellow ',' Blue ',' Orange '], 'electric':[False,True]}
lstbrand=car['brand']
lstmodel=car['model']
lstyear=car['year']
lstcolor=car['color']
lstelectric=car['electric']
print(lstbrand[1] + lstmodel[1] + str(lstyear[1]) + lstcolor[2] + 'Electric: ' + str(lstelectric[1]))
lstbrand[1]='tesla '
car['brand']=lstbrand
lstmodel.append('y ')
car['model']=lstmodel
print(lstbrand[1] + lstmodel[2] + str(lstyear[1]) + lstcolor[2] + 'Electric: ' + str(lstelectric[1]))

print('\n4.1')
print('1.) Tuples are similar to lists and dictionaries but are ordered and the values arent able to be changed')
print('2.) A tuple is literally defined in the context of coding as a list of values between parantheses "()" ')
print('3.) lists are easy to change and manipulate, tuples are not.')
print('4.) a similarity is that they are both orderly sets of values that can be indexed easily')
print('5.) tuples are faster and it makes your code safer in a way if the data that is not going to change is stored as a tuple.')
print('6.) kinda confused by this question, but i would just use a print function and have the py file be output to a txt file through powershell')
print('7.) this file would be saved in the home directory where python is saved. in my case it is in my user files')
print('8.) It would read in the very first line in the file')
print('9.) using the cd command to change directories and the dir command to get a list of what is within the directories')
print('10.) I save it in the same directory as my python,')
print('11.) a .py, .png, .txt, .jpeg ')
print('12.) there is the functional style which revolves around which is a literal and mathmatical approach to coding. there is the imperative style which focuses on how the actual program itself operates(these are generally shorter codes).There is object-oriented style which makes it very possible for the program to reuse code. finally, there is the procedural style which revolves around step-by-step excecution.')
