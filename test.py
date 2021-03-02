to_modify = [23,55,74,744,13,6,3,6223]
def indexer(list):
    indices = []
    for i in range(len(list)):
        if list[i] == 1:
          indices.append(i)
          print(indices)
indexer(to_modify)
