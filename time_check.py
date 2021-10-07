import random 
import copy 
import time 

def time_check_1(): 
    time_sort = [['2**', 'selection_sort', 'insertion_sort', 'merge_sort', 'shell_sort']] 
    sorting_types = [selection_sort, insertion_sort, merge_sort, shell_sort] 
    for i in range(7,16): 
        n = 2 ** i
        a = [random.randint(0, n) for j in range(n)]
        sort_time_for_a = [i] 
        for s in sorting_types: 
            average_time = 0 
            for k in range(0, 5): 
                m = copy.deepcopy(a) 
                start_time = time.time() 
                s(m) 
                time_of_sort = time.time() - start_time 
                average_time += time_of_sort 
            average_time = average_time / 5 
            sort_time_for_a.append(average_time) 
        time_sort.append(sort_time_for_a) 
    for l in time_sort: 
        print(l)

def time_check_2():
    time_sort = [['2**', 'selection_sort', 'insertion_sort', 'merge_sort', 'shell_sort']] 
    sorting_types = [selection_sort, insertion_sort, merge_sort, shell_sort] 
    for i in range(7,16): 
        n = 2 ** i 
        a = [j for j in range(n)]
        sort_time_for_a = [i] 
        for s in sorting_types: 
            k = copy.deepcopy(a) 
            start_time = time.time() 
            s(k) 
            time_of_sort = time.time() - start_time 
            sort_time_for_a.append(time_of_sort) 
        time_sort.append(sort_time_for_a) 
    for l in time_sort: 
        print(l)

def time_check_3():
    time_sort = [['2**', 'selection_sort', 'insertion_sort', 'merge_sort', 'shell_sort']] 
    sorting_types = [selection_sort, insertion_sort, merge_sort, shell_sort] 
    for i in range(7,16): 
        n = 2 ** i 
        a = [j for j in range(n)]
        a.reverse()
        sort_time_for_a = [i] 
        for s in sorting_types: 
            k = copy.deepcopy(a) 
            start_time = time.time() 
            s(k) 
            time_of_sort = time.time() - start_time 
            sort_time_for_a.append(time_of_sort) 
        time_sort.append(sort_time_for_a) 
    for l in time_sort: 
        print(l)

def time_check_4():
    time_sort = [['2**', 'selection_sort', 'insertion_sort', 'merge_sort', 'shell_sort']] 
    sorting_types = [selection_sort, insertion_sort, merge_sort, shell_sort] 
    for i in range(7,8): 
        n = 2 ** i 
        a = [random.randint(1, 3) for j in range(n)]
        sort_time_for_a = [i] 
        for s in sorting_types: 
            average_time = 0 
            for k in range(0, 3): 
                k = copy.deepcopy(a)
                random.shuffle(k) 
                start_time = time.time() 
                s(k) 
                time_of_sort = time.time() - start_time 
                average_time += time_of_sort 
            average_time = average_time / 3 
            sort_time_for_a.append(average_time) 
        time_sort.append(sort_time_for_a) 
    for l in time_sort: 
        print(l)

 
 
def selection_sort(a): 
    for i in range(len(a) - 1): 
        for j in range(i + 1, len(a)): 
            if a[j] < a[i]: 
                a[j], a[i] = a[i], a[j] 
 
 
def insertion_sort(a): 
    for i in range(1, len(a)): 
        key = a[i] 
        j = i - 1 
        while j >= 0 and key < a[j]: 
            a[j + 1] = a[j] 
            j -= 1 
        a[j + 1] = key 
 
 
def merge_sort(a): 
    if len(a) > 1: 
        mid = len(a)//2 
        l = a[:mid] 
        r = a[mid:] 
 
        merge_sort(l) 
        merge_sort(r) 
 
        i = j = k = 0 
        while i < len(l) and j < len(r): 
            if l[i] < r[j]: 
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
 
 
def shell_sort(a): 
    last_index = len(a) - 1 
    step = len(a)//2 
    while step > 0: 
        for i in range(step, last_index + 1, 1): 
            j = i 
            delta = j - step 
            while delta >= 0 and a[delta] > a[j]: 
                a[delta], a[j] = a[j], a[delta] 
                j = delta 
                delta = j - step 
        step //= 2 
 
 
if __name__ == '__main__':
    print('Exp. 1')
    time_check_1()
    print('Exp. 2')
    time_check_2()
    print('Exp. 3')
    time_check_3()
    print('Exp. 4')
    time_check_4()
