def string_splosion(str):
  front = "" 
  for x in range(len(str)):
    front = front + str[:x+1]
  return front 
