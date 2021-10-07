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
