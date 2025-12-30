import numpy as np
import subprocess
import os
import time
import json

ouputs = 'usr_var_test'
vars = f'./labolsa BVM 10 %x% 10000 10.0 1000 2000.0'.split()


def usr_exploration(min_, max_, step = None, output_data_folder = ouputs, vars = vars, json_name = 'test_data', time_out = 60):
   if not step:
      step = min(10000, (max_ - min_)//10)
      
   # if not os.path.exists()
   
   if not os.path.exists('data/'+output_data_folder):
      if not os.path.exists('data'):
         os.mkdir('data')
      os.mkdir('data/'+output_data_folder)
   
   maping_data = dict()
   
   X = np.arange(min_, max_+step, step)
   for i, x in enumerate(X):
      
      filename = '/' + f'test_{i}_{x}'
      vars[3] = str(x)
      
      # if os.path.exists(test_dir+filename):
      #    continue
      
      subprocess.check_output('make', text=True, cwd='..') 
      
      start = time.perf_counter()
      try:
         result = subprocess.run(
            vars,
            timeout=time_out,
            capture_output=True,
            text=True,
            cwd='..'
         )
         time_lapse = time.perf_counter() - start
         exit_status = 0
            
         
      except subprocess.TimeoutExpired:
         exit_status = -1
         print(f"Process {i} did not converge in time → killed")

      if exit_status == 0:
         log = {
            'x_used' : x,
            'output' : result.stdout,
            'execute_time' : time_lapse,
         }
      else:
         log = {
            'x_used' : str(int(x)),
            'output' : 'timeout_error',
            'execute_time' : None,
         }
      
      maping_data[i] = log
      
      # output = result.stdout
      
      
      
      with open('data/' + output_data_folder+filename, 'w') as file:
         file.write(log['output'])
      
      
   clean_data = {
      str(k): {
         "x_used": int(v["x_used"]),
         "output": str(v["output"]),
         "execute_time": float(v["execute_time"])
      }
      for k, v in maping_data.items()
   }
   
   with open('data/'+output_data_folder+'/'+json_name, 'w', encoding='utf-8') as file:
      json.dump(clean_data, file, indent=3)
