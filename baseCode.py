from math import exp,sqrt,log
import re
from datetime import date,time,datetime,timedelta
from operator import itemgetter
import numpy as np



x,y=4,5
z=x+y
print('Output #2: four plus five equals {0:d}:'.format(z))
print('*'*40)

a=[1,2,3,4]
b=['first', 'second', 'third', 'fourth']
c=a+b
print('Output #3: {0},{1},{2}'.format(a,b,c))
print('*'*40)

x=9
print('Output #4:{0}'.format(x))
print('Output #5:{0}'.format(3**4))
print('Output #6:{0}'.format(int(8.3)/int(2.7)))
print("Output#7:{0:.3f}".format(8.3/2.7))

print('*'*40)
y=2.5*4.8
print("Output#8:{0:.1f}".format(y))
r=8/float(3)
print("Output#9:{0:.2f}".format(r))
print("Output#10:{0:.4f}".format(8.0/3))
print('*'*40)
print("Output#14:{0:s}".format('I\'menjoyinglearningPython.'))
print("Output#15:{0:s}".format("Thisisalongstring.Withoutthebackslash\
itwouldrunoffofthepageontherightinthetexteditorandbevery\
difficulttoreadandedit.Byusingthebackslashyoucansplitthelong\
stringintosmallerstringsonseparatelinessothatthewholestringiseasy\
toviewinthetexteditor."))
print("Output#16:{0:s}".format('''Youcanusetriplesinglequotesformultilinecommentstrings.'''))

print('*'*40)
string1,string2="Thisisa","shortstring."
sentence=string1+string2
print("Output#18:{0:s}".format(sentence))
print("Output#19:{0:s}{1:s}{2:s}".format("Sheis","very"*4,"beautiful."))
m=len(sentence)
print("Output#20:{0:d}".format(m))
print('*'*40)

string1="My deliverable is due in May"
string1_list1=string1.split()
string1_list2=string1.split(" ",2)
print("Output#21:{0}".format(string1_list1))
print("Output#22:FIRSTPIECE:{0}SECONDPIECE:{1}THIRDPIECE:{2}".format(string1_list2[0],string1_list2[1],string1_list2[2]))
print('*'*40)

string2="Your,deliverable,is,due,in,June"
string2_list=string2.split(',')
print("Output#23:{0}".format(string2_list))
print("Output#24:{0}{1}{2}".format(string2_list[1],string2_list[5],string2_list[1]))
print('*'*40)

string3=" Removeunwantedcharactersfromthisstring.\t\t\n"
print("Output#26:string3:{0:s}".format(string3))
string3_lstrip=string3.lstrip()
print("Output#27:lstrip:{0:s}".format(string3_lstrip))
string3_rstrip=string3.rstrip()
print("Output#28:rstrip:{0:s}".format(string3_rstrip))
string3_strip=string3.strip()
print("Output#29:strip:{0:s}".format(string3_strip))

print('*'*40)
string5="Let's replace the spaces in this sentence witho ther characters."
string5_replace=string5.replace(" ","!@!")
print("Output#32(with!@!):{0:s}".format(string5_replace))
string5_replace=string5.replace(" ",",")
print("Output#33(withcommas):{0:s}".format(string5_replace))

print('*'*40)
string6="Here's WHAT Happens WHEN You Use lower."
print("Output#34:{0:s}".format(string6.lower()))
string7="Here's what Happens when You Use UPPER."
print("Output#35:{0:s}".format(string7.upper()))
string5="here's WHAT Happens WHEN you use Capitalize."
print("Output#36:{0:s}".format(string5.capitalize()))
string5_list=string5.split()
print("Output#37(oneachword):")
for word in string5_list:
    print("{0:s}".format(word.capitalize()))

print('*'*40)
string="The quick brown fox jump sover the lazy dog."
string_list=string.split()
pattern=re.compile(r"The",re.I)
count=0
for word in string_list:
    if pattern.search(word):
        count +=1
        print("Output#38:{0:d}".format(count))

print('*'*40)
string="The quick brown fox jump sover the lazy dog."
string_list=string.split()
pattern=re.compile(r"(?P<match_word>The)",re.I)
print("Output#39:")
for word in string_list:
    if pattern.search(word):
        print("{:s}".format(pattern.search(word).group('match_word')))

print('*'*40)
today=date.today()
print("Output#41:today:{0!s}".format(today))
print("Output#42:{0!s}".format(today.year))
print("Output#43:{0!s}".format(today.month))
print("Output#44:{0!s}".format(today.day))
current_datetime=datetime.today()
print("Output#45:{0!s}".format(current_datetime))

print('*'*40)
one_day=timedelta(days=1)
yesterday=today-one_day
print("Output#46:yesterday:{0!s}".format(yesterday))
eight_hours=timedelta(hours=8)
print("Output#47:{0!s}{1!s}".format(eight_hours.days,eight_hours.seconds))

print('*'*40)
date_diff=today-yesterday
print("Output#48:{0!s}".format(date_diff))
print("Output#49:{0!s}".format(str(date_diff).split()[0]))
print("Output#50:{:s}".format(today.strftime('%m/%d/%Y')))
print("Output#51:{:s}".format(today.strftime('%b%d,%Y')))
print("Output#52:{:s}".format(today.strftime('%Y%m%d')))
print("Output#53:{:s}".format(today.strftime('%B%d,%Y')))

print('*'*40)
a_list=[1,2,3]
print("Output#58:{}".format(a_list))
print("Output#59:a_list has {} elements.".format(len(a_list)))
print("Output#60:the maximum value in a_list is {}.".format(max(a_list)))
print("Output#61:the minimum value in a_list is {}.".format(min(a_list)))
another_list=['printer',5,['star','circle',9]]
print("Output#62:{}".format(another_list))
print("Output#63:another_list also has {} elements.".format(len(another_list)))
print("Output#64:5 is in another_list {} time.".format(another_list.count(5)))
#count元素出现的数量

print('*'*40)
print("Output#65:{}".format(a_list[0]))
print("Output#66:{}".format(a_list[1]))
print("Output#67:{}".format(a_list[2]))
print("Output#68:{}".format(a_list[-1]))
print("Output#69:{}".format(a_list[-2]))
print("Output#70:{}".format(a_list[-3]))
print("Output#71:{}".format(another_list[2]))
print("Output#72:{}".format(another_list[-1]))

print('*'*40)
print("Output#73:{}".format(a_list[0:2]))
print("Output#74:{}".format(another_list[:2]))
print("Output#75:{}".format(a_list[1:3]))
print("Output#76:{}".format(another_list[1:]))

print('*'*40)
a_new_list=a_list[:]
print("Output#77:{}".format(a_new_list))

print('*'*40)
a_longer_list=a_list+another_list
print("Output#78:{}".format(a_longer_list))

print('*'*40)
a=2 in a_list
print("Output#79:{}".format(a))
if 2 in a_list:
    print("Output#80:2 is in{}.".format(a_list))
b=6 not in a_list
print("Output#81:{}".format(b))
if 6 not in a_list:
    print("Output#82:6 is not in{}.".format(a_list))

print('*'*40)
a_list.append(4)
a_list.append(5)
a_list.append(6)
print("Output#83:{}".format(a_list))
a_list.remove(5)
print("Output#84:{}".format(a_list))
a_list.pop()
a_list.pop()
print("Output#85:{}".format(a_list))

print('*'*40)
a_list.reverse()
print("Output#86:{}".format(a_list))
a_list.reverse()
print("Output#87:{}".format(a_list))

print('*'*40)
unordered_list=[3,5,1,7,2,8,4,9,0,6]
print("Output#88:{}".format(unordered_list))
list_copy=unordered_list[:]
list_copy.sort()
print("Output#89:{}".format(list_copy))
print("Output#90:{}".format(unordered_list))

print('*'*40)
my_lists=[[1,2,3,4],[4,3,2,1],[2,4,1,3]]
my_lists_sorted_by_index_3=sorted(my_lists,key=lambda index_value:index_value[3])#从第4个元素值进行排序
print("Output#91:{}".format(my_lists_sorted_by_index_3))

print('*'*40)
my_lists=[[123,2,2,444],[22,6,6,444],[354,4,4,678],[236,5,5,678],[578,1,1,290],[461,1,1,290]]
my_lists_sorted_by_index_3_and_0=sorted(my_lists,key=itemgetter(3,0))#先按3进行排序，再按0进行排序
print("Output#92:{}".format(my_lists_sorted_by_index_3_and_0))

print('*'*40)
my_tuple=('x','y','z')
print("Output#93:{}".format(my_tuple))
print("Output#94:my_tuplehas{}elements".format(len(my_tuple)))
print("Output#95:{}".format(my_tuple[1]))
longer_tuple=my_tuple+my_tuple
print("Output#96:{}".format(longer_tuple))

print('*'*40)
one,two,three=my_tuple
print("Output#97:{0}{1}{2}".format(one,two,three))

print('*'*40)
var1='red'
var2='robin'
print("Output#98:{} {}".format(var1,var2))
var1,var2=var2,var1
print("Output#99:{} {}".format(var1,var2))

print('*'*40)
my_list=[1,2,3]
my_tuple=('x','y','z')
print("Output#100:{}".format(tuple(my_list)))
print("Output#101:{}".format(list(my_tuple)))

print('*'*40)
empty_dict={}
a_dict={'one':1,'two':2,'three':3}
print("Output#102:{}".format(a_dict))
print("Output#103:a_dict has {!s} elements".format(len(a_dict)))
another_dict={'x':'printer','y':5,'z':['star','circle',9]}
print("Output#104:{}".format(another_dict))
print("Output#105:another_dict also has {!s} elements".format(len(another_dict)))

print('*'*40)
a_new_dict=a_dict.copy() #复制一个字典
print("Output#108:{}".format(a_new_dict))
print("Output#109:{}".format(a_new_dict.keys()))
a_dict_keys=a_new_dict.keys()
print("Output#110:{}".format(a_dict_keys))
print("Output#111:{}".format(a_new_dict.values()))
print("Output#112:{}".format(a_new_dict.items()))

print('*'*40)
if 'y' in another_dict:
    print("Output#114:y is a key in another_dict:{}.".format(another_dict.keys()))
    if 'c' not in another_dict:
        print("Output#115:c is not a key in another_dict:{}.".format(another_dict.keys()))
        print("Output#116:{!s}".format(a_dict.get('three')))
        print("Output#117:{!s}".format(a_dict.get('four')))
        print("Output#118:{!s}".format(a_dict.get('four','Not in dict')))

print('*'*40)
print("Output#119:{}".format(a_dict))
dict_copy=a_dict.copy()
ordered_dict1=sorted(dict_copy.items(),key=lambda item:item[0])
print("Output#120(order by keys):{}".format(ordered_dict1))
ordered_dict2=sorted(dict_copy.items(),key=lambda item:item[1])
print("Output#121(order by values):{}".format(ordered_dict2))
ordered_dict3=sorted(dict_copy.items(),key=lambda x:x[1],reverse=True)#降序
print("Output#122(order by values,descending):{}".format(ordered_dict3))
ordered_dict4=sorted(dict_copy.items(),key=lambda x:x[1],reverse=False)#升序
print("Output#123(order by values,ascending):{}".format(ordered_dict4))
ordered_dict3=sorted(dict_copy.items(),key=lambda item:item[0],reverse=True)#降序
print("Output#122(order by values,descending):{}".format(ordered_dict3))
ordered_dict4=sorted(dict_copy.items(),key=lambda item:item[0],reverse=False)#升序
print("Output#123(order by values,ascending):{}".format(ordered_dict4))

print('*'*40)
x=5
if x>4 or x!=9:
    print("Output#124:{!s}".format(x))
if x>6:
    print("Output#125:x is greater than six")
elif x>4 and x==5:
    print("Output#125:{}".format(x))
else:
    print("Output#125:x is not greater than 4")

print('*'*40)
y=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
z=['Annie','Betty','Claire','Daphne','Ellie','Franchesca','Greta','Holly','Isabel','Jenny']
print("Output#126:")
for month in y:
    print("{!s}".format(month))

print("Output#127:(index value:name in list)")
for i in range(len(z)):
    print("{0!s}:{1:s}".format(i,z[i]))

print("Output#128:(access elements in y with z's index values)")
for j in range(len(z)):
    if y[j].startswith('J'): #首字J
        print("{!s}".format(y[j]))

print("Output#129:")
for key,value in another_dict.items():
    print("{0:s},{1}".format(key,value))

print('*'*40)
my_data=[[1,2,3],[4,5,6],[7,8,9]]
rows_to_keep=[row for row in my_data if row[1]>5]
print("Output#130(list comprehension):{}".format(rows_to_keep))

print('*'*40)
my_data=[(1,2,3),(4,5,6),(7,8,9),(10,11,12),(7,8,9)]
set_of_tuples1={x for x in my_data}
print("Output#131(set comprehension):{}".format(set_of_tuples1))
set_of_tuples2=set(my_data)#精减元组
print("Output#132(set function):{}".format(set_of_tuples2))

print('*'*40)
my_dictionary={'customer1':7,'customer2':9,'customer3':11}
my_results={key:value for key,value in my_dictionary.items() if value>9}
print("Output#133(dictionary comprehension):{}".format(my_results))

print('*'*40)
print("Output#134:")
x=0
while x<11:
    print("{!s}".format(x))
    x += 1

print('*'*40)
def getMean(numericValues):
    #print(len(numericValues))
    return sum(numericValues) / len(numericValues) if len(numericValues) > 0 else float('nan')
my_list=[2,2,4,4,6,6,8,8]
print("Output#135(mean):{!s}".format(getMean(my_list)))

print('*'*40)
print(np.mean(my_list))



