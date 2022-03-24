# 모각코 12일차

def pre_in_to_post(pre_list, in_list):
  if pre_list:
    root = pre_list[0]
    mid = in_list.index(root)
    pre_in_to_post(pre_list[1:mid + 1], in_list[:mid])
    pre_in_to_post(pre_list[mid + 1:], in_list[mid + 1:])
    print(root, end = ' ')

pre_order = [7, 3, 1, 5, 4, 12, 10, 8]
in_order = [1, 3, 12, 4, 5, 7, 8, 10]

print('후위 순회 결과: ', end = '')
pre_in_to_post(pre_order, in_order)