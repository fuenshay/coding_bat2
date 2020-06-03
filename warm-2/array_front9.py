def array_front9(nums):
  for x in nums[:4]:
    if x == 9:
      return True
      break
  return False
