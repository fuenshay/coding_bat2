"""
Author: Shayna Fu
Date: June 17, 2020


Return True if the given string contains an appearance of
"xyz" where the xyz is not directly preceeded by a period (.).
So "xxyz" counts but "x.xyz" does not.


xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True

"""

SOLUTION#1

def xyz_there(str):
  a = str.count(".xyz")
  b = str.count("xyz")
  if a != b:
    return True
  return False

SOLUTION#2  

  for i in range(len(str)):
    if str[i] != "." and str[i+1:i+4] == "xyz":
      return True
    if str[0:3] == "xyz":
      return True
  return False
