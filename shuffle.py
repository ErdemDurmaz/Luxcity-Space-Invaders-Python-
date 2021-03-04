import random

base_list = [23,55,74,744,13,6,3,6223]
def indexer(list):
    indices = []
    for i in range(len(list)):
        if list[i] == 1:
            indices.append(i)
        print(indices)

def randomiser(list):
    for i in range((len(list))):
        return(random.randrange(0,len(list)))

dic = {}
for i in range(len(randomiser(base_list))):
    dic[randomiser(base_list)[i]] = output[i]
    print(dic)
    for randomiser(base_list), item in enumerate(base_list):
        for i in randomiser(base_list):
            base_list[i] = dic[i]
print(base_list)

