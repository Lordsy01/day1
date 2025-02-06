def find_all_pairs(arr, target):
    n=len(arr)
    pairs=[]
    numbs_indices={}
    numbs_map={}
    
    if n==0:
        return pairs
    for i, numbs in enumerate(arr):
        numbs_indices[numbs]=numbs_indices.get(numbs, []) + [i]
    for i in range(n):
        for j in range(i+1, n):
            pairs.append((arr[i],arr[j]))
            numbs_map.get(numbs, []) +[index]
    return pairs, numbs_indices

    # for index, numbs in enumerate(arr):
    #     complement=target-numbs
    #     if complement in numbs_map:
    #         for prev_index in numbs_map[complement]:
    #      result.append((prev_index, index))
    
    # return result

numbs=[2, 8, 5, 9,3]   
target_sum= input("what is your target sum?")
print( target_sum)
print(len(target))
all_pairs=find_all_pairs(numbs)
print(all_pairs)
empty_array=[]
empty_pairs=find_all_pairs(empty_array)
print(empty_pairs)
one_element_array=[1]
one_element_pair=find_all_pairs(one_element_array)
print(one_element_pair)