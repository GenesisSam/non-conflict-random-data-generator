import csv
import random
import os

# random data
def generate(max_leng=10000):
  i = 0
  d = []

  print("Begin generate random data")
  while i < max_leng:
    ran_var = random.randint(1, max_leng*2)
    if (ran_var not in d):
      print("%d" % (i))
      d.append(ran_var)
      i += 1
  print("End generate random data")
  print("Begin file out")
  get_csv_writer("rnd.csv", d, ",")
  print("Done file out")


def get_csv_writer(filename, rows, delimiter):
  with open(filename, 'w') as csvfile:
    for row in rows:
      try:
        csvfile.write("%d%s" % (row, delimiter))
      except Exception as detail:
        print(type(detail))
        print(detail)

if(__name__ == "__main__"):
  generate(100000)
