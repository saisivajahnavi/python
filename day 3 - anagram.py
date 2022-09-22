from collections import defaultdict
test_list=["12345"]
print("the original list:"+str(test_list))
temp=defaultdict(list)
for ele in test_list:
    temp[str(sorted(ele))].append(ele)
res=list(temp.values())
print("the grouped anagrams:"+str(res))
