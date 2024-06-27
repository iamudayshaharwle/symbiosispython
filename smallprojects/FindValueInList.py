
list1 = [23,56,8,723,78,43,2,5]

user_input = int(input('enter: '))

while True:
  if user_input in list1:
    position = list1.index(user_input)
    print(f'{user_input} in list on {position} position')
    break
  else:
    print('not in list')
    break