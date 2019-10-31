def sencSplitter(words):
  senc = words
  splitted = senc.split()
  inv = []
  x = len(splitted) - 1
  while x >= 0:
      inv.append(splitted[x]) 
      x = x-1
  result=" ".join(inv)
  return result
