from PIL.ImageChops import difference
from numpy.testing.print_coercion_tables import print_new_cast_table

my_set = {1,2,3}
print(my_set)

set_ = set([4,5,6,6])
print(set_)

set1 = {1,2,3}
set2 = {3,4,5}


union_result_method = set1.union(set2)
union_result_operator = set1 | set2

print('Union of set1 and set2 using method:',union_result_method)
print('Union of set1 and set2 using method:',union_result_operator)


#inetsection

intersection_method = set1.intersection(set2)
intersection_operator = set1 & set2
print('intersection of set1 and set2 using intersection method:'  ,intersection_method)
print('intersection of set1 and set2 using intersection operator:'  ,intersection_operator)

#difference
difference_method = set1.difference(set2) # 1,2
difference_operator = set1 - set2
print('Differnce of set1 and set2 using Difference method:'  ,difference_method)
print('Differnce of set1 and set2 using Difference operator:'  ,difference_operator)

#symetric_differnce
symmetric_method = set1.symmetric_difference(set2)
symmetric_operator = set1 ^ set2
print('using this symmetric method thing of set 1 and set 2',symmetric_method)
print('using this symmetric operator thing of set 1 and set 2',symmetric_operator)

my_set= {1,2,3}
my_set.remove(3)
print(my_set)

my_set.add(5)
print(my_set)

my_set.discard(7)
print(my_set)



