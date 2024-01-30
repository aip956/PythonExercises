''' 	my_first_param_function.py 
Implement a while loop to call a function detonation in...X seconds.
Your loop will stop at 0. 10 included, but 0 is not.'''

# function will print("detonation in... "+str(seconds_left)+" seconds.")

timer = 10

def detonation_in(x):
  print("detonation in... ", x, " seconds.")
  
while (timer > 0):
  detonation_in(timer)
  timer -= 1

