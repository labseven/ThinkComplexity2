m = 2**32
a = 1664525
c = 1013904223

n=100000000000

seed = 4

rng = seed

while(True):
  rng = ((a * rng) + c) % m
  print(rng)
