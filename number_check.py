import random 
import copy 
import time

comparison_var = [0, 0, 0, 0]

def number_check_1():
    global comparison_var
    compresions = [['2**', 'selection_sort', 'insertion_sort', 'merge_sort', 'shell_sort']] 
    sorting_types = [selection_sort, insertion_sort, merge_sort, shell_sort]
    for i in range(7, 16): 
        n = 2 ** i
        a = [random.randint(0, n) for j in range(n)]
        compresions_for_a = [i] 
        for s in range(len(sorting_types)):  
            for k in range(0, 5): 
                k = copy.deepcopy(a)
                sorting_types[s](k)
            average_number_compresions = comparison_var[s] / 5 
            compresions_for_a.append(average_number_compresions)
            comparison_var[s] = 0
        compresions.append(compresions_for_a) 
    for l in compresions: 
        print(l)

def number_check_2():
    global comparison_var
    compresions = [['2**', 'selection_sort', 'insertion_sort', 'merge_sort', 'shell_sort']] 
    sorting_types = [selection_sort, insertion_sort, merge_sort, shell_sort]
    for i in range(7, 16): 
        n = 2 ** i
        a = [j for j in range(n)]
        compresions_for_a = [i] 
        for s in range(len(sorting_types)): 
            k = copy.deepcopy(a) 
            sorting_types[s](k)
            compresions_for_a.append(comparison_var[s])
            comparison_var[s] = 0
        compresions.append(compresions_for_a) 
    for l in compresions: 
        print(l)

def number_check_3():
    global comparison_var
    compresions = [['2**', 'selection_sort', 'insertion_sort', 'merge_sort', 'shell_sort']] 
    sorting_types = [selection_sort, insertion_sort, merge_sort, shell_sort]
    for i in range(7, 16): 
        n = 2 ** i
        a = [j for j in range(n)]
        a.reverse()
        compresions_for_a = [i] 
        for s in range(len(sorting_types)):  
            k = copy.deepcopy(a) 
            sorting_types[s](k)
            compresions_for_a.append(comparison_var[s])
            comparison_var[s] = 0
        compresions.append(compresions_for_a) 
    for l in compresions: 
        print(l)

def number_check_4():
    global comparison_var
    compresions = [['2**', 'selection_sort', 'insertion_sort', 'merge_sort', 'shell_sort']] 
    sorting_types = [selection_sort, insertion_sort, merge_sort, shell_sort]
    for i in range(7, 16): 
        n = 2 ** i
        a = [random.randint(1, 3) for j in range(n)]
        compresions_for_a = [i] 
        for s in range(len(sorting_types)):  
            for k in range(0, 3): 
                k = copy.deepcopy(a)
                random.shuffle(k)
                sorting_types[s](k)
            average_number_compresions = comparison_var[s] / 3
            compresions_for_a.append(average_number_compresions)
            comparison_var[s] = 0
        compresions.append(compresions_for_a) 
    for l in compresions: 
        print(l)

 
 
def selection_sort(a):
    for i in range(len(a) - 1): 
        for j in range(i + 1, len(a)): 
             if less_election_sort(a[j],a[i]): 
                a[j], a[i] = a[i], a[j]

def less_election_sort(x, y):
    global comparison_var
    comparison_var[0] += 1 
    return x < y
 
 
def insertion_sort(a): 
    global comparison_var
    for i in range(1, len(a)): 
        key = a[i] 
        j = i - 1
        while j >= 0 and less_election_sort_1(key,a[j]):
            a[j + 1] = a[j] 
            j -= 1
        a[j + 1] = key

def less_election_sort_1(x, y):
    global comparison_var
    comparison_var[1] += 1 
    return x < y
 
 
def merge_sort(a):
    global comparison_var 
    if len(a) > 1: 
        mid = len(a)//2 
        l = a[:mid] 
        r = a[mid:] 
 
        merge_sort(l) 
        merge_sort(r) 
 
        i = j = k = 0 
        while i < len(l) and j < len(r):
            if less_election_sort_2(l[i], r[j]):
                a[k] = l[i] 
                i += 1 
            else: 
                a[k] = r[j] 
                j += 1 
            k += 1 
 
        while i < len(l): 
            a[k] = l[i] 
            i += 1 
            k += 1 
 
        while j < len(r): 
            a[k] = r[j] 
            j += 1 
            k += 1 
 
def less_election_sort_2(x, y):
    global comparison_var
    comparison_var[2] += 1 
    return x < y 
 
def shell_sort(a):
    global comparison_var
    last_index = len(a) - 1 
    step = len(a)//2 
    while step > 0: 
        for i in range(step, last_index + 1, 1): 
            j = i 
            delta = j - step
            while delta >= 0 and more_election_sort(a[delta], a[j]):
                a[delta], a[j] = a[j], a[delta] 
                j = delta 
                delta = j - step
        step //= 2 
 

def more_election_sort(x, y):
    comparison_var[3] += 1
    return x > y
 
if __name__ == '__main__':
    print('Exp. 1')
    number_check_1()
    print('Exp. 2')
    number_check_2()
    print('Exp. 3')
    number_check_3()
    print('Exp. 4')
    number_check_4()
