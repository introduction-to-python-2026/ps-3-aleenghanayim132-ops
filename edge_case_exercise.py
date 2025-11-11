def move(my_list, direction):
  index_of_one = my_list.index(1)
  if direction == 'right':
    if my_list[index_of_one + 1] < len(my_list):
      my_list[index_of_one] = 0
      my_list[index_of_one + 1] = 1
      return my_list
  if direction == 'left':
    if my_list[index_of_one - 1] >= 0:
      my_list[index_of_one] = 0
      my_list[index_of_one - 1] = 1
      return my_list
  return my_list
