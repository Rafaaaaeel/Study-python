def findDuplicate(nums):
  tortoise = nums[0] # Recebe o primeiro valor da lista
  hare = nums[0] # Recebe o primeiro valor da lista
  while True: 
    tortoise = nums[tortoise] 
    hare = nums[nums[hare]]
    if tortoise == hare:
      break

    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 == ptr2:
      ptr1 = nums[ptr1]
      ptr2 = nums[ptr2]
      
      break

    return ptr1

print(findDuplicate([5,2,3,5,1]))