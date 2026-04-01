# Learning from https://youtu.be/mziIj4M_uwk

def topten():
  n = 1

  while n <= 10:
    sq = n * n
    yield sq
    n += 1

values = topten()

for i in values:
  print(i)

#Why ? (Real life reson)
# Maybe for fetching data one at a time instead of loading everything into memory.