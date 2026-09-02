import time

current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 

def speed_calc_decorator(function):
    def calculate():
        new_time = time.time()
        function()
        new_time_2 = time.time()
        diff = new_time_2 - new_time
        print(f"Time it took is {diff}")
    return calculate
    
@speed_calc_decorator
def fast_function():
  for i in range(1000):
    i * i
        
@speed_calc_decorator
def slow_function():
  for i in range(10000):
    i * i

fast_function()
slow_function()
