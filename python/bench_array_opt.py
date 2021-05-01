
### benchmark the performance for operating a (x, y) matrix with different methods

import time
import numpy as np
import random
import copy

def init_neseted_list(x, y, v):
  nlist = [[v]*x for i in range(y)]
  # print(nlist)
  return nlist

def init_np_array(x, y, v):
  return np.full((x, y), v)


def test_init_nested_list(benchmark):
  # benchmark.group = "Initialization"
  init_v = random.randrange(255)
  benchmark(init_neseted_list, 1000, 1000, init_v)

def test_init_np_array(benchmark):
  # benchmark.group = "Initialization"
  init_v = random.randrange(255)
  benchmark(init_np_array, 1000, 1000, init_v)


########################### iteration ###########################


def iterate_nested_list(nlist, v):
  for i in range(len(nlist)):
    for j in range(len(nlist[i])):
      nlist[i][j] = v

def iterate_np_array(a, v):
  for i in range(len(a)):
    for j in range(len(a[i])):
      a[i][j] = v

def test_iterate_nested_list(benchmark):
  # benchmark.group = "Iteration"
  test_list = init_neseted_list(1000, 1000, 0)
  v = random.randrange(255)
  benchmark(iterate_nested_list, nlist=test_list, v=v)


def test_iterate_np_array(benchmark):
  # benchmark.group = "Iteration"
  np_arry = init_np_array(1000, 1000, 0)
  v = random.randrange(255)
  benchmark(iterate_nested_list, np_arry, v)

########################### copy ###########################

def copy_nested_list_dp(l):
  new_l = copy.deepcopy(l)
  return new_l

def copy_nested_list_it(l):
  new_l = []
  for row in l:
    n_row = []
    for column in row:
      n_row.append(column)
    new_l.append(n_row)
  # print(new_l)
  return new_l

def copy_nested_list_lc(l):
  new_l = [ [c for c in row] for row in l]
  # print(new_l)
  return new_l

def copy_nested_list_slice(l):
  new_l = [ row[:] for row in l]
  # print(new_l)
  return new_l

def copy_np_array(a):
  new_a = copy.deepcopy(a)
  return new_a


def test_copy_nested_list(benchmark):
  # benchmark.group = "Copy"
  v = random.randrange(255)
  test_list = init_neseted_list(1000, 1000, v)
  benchmark(copy_nested_list_dp, test_list)

def test_copy_nested_list_it(benchmark):
  # benchmark.group = "Copy"
  v = random.randrange(255)
  test_list = init_neseted_list(1000, 1000, v)
  benchmark(copy_nested_list_it, test_list)

def test_copy_nested_list_lc(benchmark):
  # benchmark.group = "Copy"
  v = random.randrange(255)
  test_list = init_neseted_list(1000, 1000, v)
  benchmark(copy_nested_list_lc, test_list)

def test_copy_nested_list_slice(benchmark):
  # benchmark.group = "Copy"
  v = random.randrange(255)
  test_list = init_neseted_list(1000, 1000, v)
  benchmark(copy_nested_list_slice, test_list)


def test_copy_np_array(benchmark):
  # benchmark.group = "Copy"
  v = random.randrange(255)
  test_arr = init_np_array(1000, 1000, v)
  benchmark(copy_np_array, test_arr)

########################### to array of string ###########################
def to_string_nested_list_it(l):
  str_list = []
  for row in l:
    str_row = ""
    for v in row:
      str_row+=("%d "%v)
    str_list.append(str_row)
  # print(str_list)
  return str_list

def to_string_nested_list_lc(l):
  str_list = [" ".join("%d"%(item) for item in row) for row in l  ]
  #print(str_list)
  return str_list

def to_string_np_array_it(a):
  str_list = []
  for row in a:
    str_row =""
    for v in row:
      str_row+=("%d "%v)
    str_list.append(str_row)
  # print(str_list)
  return str_list

def to_string_np_array_lc(a):
  str_list = [" ".join(["%d"%(item) for item in row]) for row in a  ]
  # print(str_list)
  return str_list

# def to_string_np_array_lc_2(a):
#   str_list = [" ".join("%d"%(item) for item in row) for row in a  ]
#   # print(str_list)
#   return str_list

def to_string_np_array_2str(a):
  # for row in a:
  #   str_row = np.array2string(row, separator=" ")
  #   print(str_row.strip("[]"))

  str_list = [ np.array2string(row, separator=" ").strip("[]") for row in a ]
  # str_list_2 = [np.array2string(row, separator=" ") for row in a]
  # print(str_list)
  return str_list
  # print(str_list)
  # return str_list

def to_string_np_array_lc_2(a):
  print(a.tolist())
  # str_list = []
  # for row in a:
  #   arrstr = np.char.mod('%d', a)
  #   str_list_2 = [np.array2string(row, separator=" ") for row in a]
  # # print(str_list)
  # return str_list

def test_tostr_nested_list_it(benchmark):
  # benchmark.group = "To String"
  v = random.randrange(255)
  test_list = init_neseted_list(1000, 1000, v)
  benchmark(to_string_nested_list_it, test_list)

def test_tostr_nested_list_lc(benchmark):
  # benchmark.group = "To String"
  v = random.randrange(255)
  test_list = init_neseted_list(1000, 1000, v)
  benchmark(to_string_nested_list_lc, test_list)

def test_tostr_nested_np_array_it(benchmark):
  # benchmark.group = "To String"
  v = random.randrange(255)
  test_arr = init_np_array(1000, 1000, v)
  benchmark(to_string_np_array_it, test_arr)

def test_tostr_nested_np_array_lc(benchmark):
  # benchmark.group = "To String"
  v = random.randrange(255)
  test_arr = init_np_array(1000, 1000, v)
  benchmark(to_string_np_array_lc, test_arr)

def test_tostr_nested_np_array_2str(benchmark):
  # benchmark.group = "To String"
  v = random.randrange(255)
  test_arr = init_np_array(1000, 1000, v)
  benchmark(to_string_np_array_2str, test_arr)

#### geneal ####
def g_nested_list():
  v = random.randrange(255)
  test_list = init_neseted_list(1000, 1000, v)
  v1= random.randrange(255)
  iterate_nested_list(test_list, v1)
  copied_list =   copy_nested_list_slice(test_list)
  str_list = to_string_nested_list_lc(copied_list)
  # print(str_list)
  return str_list

def g_np_array():
  v = random.randrange(255)
  test_arr = init_np_array(1000, 1000, v)
  v1= random.randrange(255)
  iterate_np_array(test_arr, v1)
  copied_arr = copy_np_array(test_arr)
  str_list = to_string_np_array_lc(copied_arr)
  # print(str_list)
  return str_list

def test_g_nested_list(benchmark):
  benchmark.group = "General"
  benchmark(g_nested_list)

def test_g_np_array(benchmark):
  benchmark.group = "General"
  benchmark(g_np_array)



if __name__ == "__main__":
  l = init_neseted_list(10, 10, 4)
  print(copy_nested_list_slice(l))
  # arr = init_np_array(10, 10, 4)
  # print(to_string_np_array_2str(arr))
  # to_string_nested_list_it(arr)
  # g_nested_list()
  # g_np_array()
