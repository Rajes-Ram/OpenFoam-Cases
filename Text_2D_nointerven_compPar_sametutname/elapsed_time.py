import time
import os

 ## Check if the file elapsed_time exists.
 ## If it doesn't, it is the beginning of execution of the code;
 ## If it do, it is the end of execution, the elapsed time wil be calculated.

check_file = os.path.exists("elapsed_time")

if check_file == False:
    ## time in seconds since The Epoch, January 1st, 1970
    current_time = time.time()

    get_time_file = open('elapsed_time', 'w')
    get_time_file.write(str(current_time))
    get_time_file.close()

else:
    initial_time_file = open('elapsed_time', 'r')
    lines = initial_time_file.readlines() ## read file
    initial_time = lines[0].split()
    initial_time = float(initial_time[0])
    initial_time_file.close()

    current_time = time.time()
    
    get_time_file = open('elapsed_time', 'w')
    get_time_file.write(str(current_time - initial_time))
    get_time_file.close()
