''' my_first_script_with_args.py 
Let's do our first loop statement!

Create a file &percnt;{exercise_name}&percnt;{extension}.

It will print any argument received to the script'''

import sys
#n = len(sys.argv)
for i in range(1, len(sys.argv)):
    print(sys.argv[i])