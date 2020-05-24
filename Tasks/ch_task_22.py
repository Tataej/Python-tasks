##22. Number of Lists in a List
##Return the total number of lists inside a given list.
##Examples
##num_of_sublists([[1, 2, 3]]) ➞ 1
## 
##num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3]]) ➞ 3
## 
##num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]) ➞ 4
## 
##num_of_sublists([1, 2, 3]) ➞ 0


def num_of_sublists(x):
    if type(x) == list:
        count = 0
        for elements in x:
            if type(elements) == list:
                count += 1
        print('num_of_sublists(',x,') --> %d' %(count))
        return(count)


num_of_sublists([[1, 2, 3]]) 
 
num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
 
num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]])
 
num_of_sublists([1, 2, 3])
