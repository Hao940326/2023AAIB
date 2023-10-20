s = 'abcdabcaba'
d ={}
for c in s:
  if c in d:
    d[c] += 1
  else:
    d[c] = 1 
  print("現在的字:",c,"字典是:",d)