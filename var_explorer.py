# import matplotlib.pyplot as plt
import numpy as np
import subprocess
import os
import time
import json

# var, min_, max_, step  = input('Insterte el nombre de variabe, el valor minimo, el valor maximo y el step separado por un espacio:').split()
# min_, max_, step = map(int, [min_, max_, step])

min_, max_, step = 10000, 200000, 10000
X = np.arange(min_, max_+step, step)
n_test = len(X)

# x_fake = 10000

test_dir = 'usr_var_test'
exit_status_dir = 'exit_status'

if not os.path.exists(test_dir):
   os.mkdir(test_dir)
   
if not os.path.exists(exit_status_dir):
   os.mkdir(exit_status_dir)


maping_data = dict()
for i, x in enumerate(X):
   
   filename = '/' + f'test_{i}_{x}'
   
   # if os.path.exists(test_dir+filename):
   #    continue
   
   subprocess.check_output('make', text=True)
   
   start = time.perf_counter()
   try:
      result = subprocess.run(
         f'./labolsa BVM 10 100 {x} 10.0 1000 2000.0'.split(),
         timeout=60,
         capture_output=True,
         text=True
      )
      time_lapse = time.perf_counter() - start
      exit_status = 0
         
      
   except subprocess.TimeoutExpired:
      exit_status = -1
      print("Process did not converge in time → killed")

   if exit_status == 0:
      log = {
         'x_used' : x,
         # 'output' : result.stdout,
         'execute_time' : time_lapse,
      }
   else:
      log = {
         'x_used' : str(int(x)),
         # 'output' : 'timeout',
         'execute_time' : -1,
      }
   
   maping_data[i] = log
   
   output = result.stdout
   
   with open(test_dir+filename, 'w') as file:
      file.write(output)

clean_data = {
   str(k): {
      "x_used": int(v["x_used"]),
      "execute_time": float(v["execute_time"])
   }
   for k, v in maping_data.items()
}
print(maping_data)
with open(exit_status_dir+'/'+'test_data.json', 'w', encoding='utf-8') as file:
   json.dump(clean_data, file, indent=3)