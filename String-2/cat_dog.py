"""
Author: Shayna Fu
Date: June 17, 2020


Return True if the string "cat" and "dog" appear the same number of times in the given string.


cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True

"""
SOLUTION:

def cat_dog(str):
 count_cat = 0
 count_dog = 0
 for i in range(len(str)-2):
  if str[i:i+3] == 'dog':
   count_cat += 1
  if str[i:i+3] == 'cat':
   count_dog += 1
 return count_cat == count_dog
