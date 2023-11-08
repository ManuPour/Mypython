list =[4, 12, 7, 2, 3, 6 ,1 , 8, 5, 13, 16, 19]
target = 12

def summa12(list, target):
    found = False
    for i in range(len(list)-1):
      for j in range(i+1, len(list)):
          if list[i]+ list[j] == target:
              print(list[i], list[j])
              found = True
    return found
print(summa12(list, target))
