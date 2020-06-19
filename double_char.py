"""
Author: Shayna Fu
Date: June 17, 2020


Given a string, return a string where for every char in the original, there are two chars.


double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'

"""

SOLUTION:

  result = ''
  for char in str:
    result += char * 2
  return result 
