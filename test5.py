# exam
import statistics
import math
list1 =[13, 17, 31, 57," ", 41, 83,' ']
list1 = list(set(list1))
list1.remove(' ')
list1 = statistics.mean(list1)
print(list1)
