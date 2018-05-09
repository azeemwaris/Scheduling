class cstruct:
        arrival_time = -1
        burst_time = 0
        process_name = " "
        turnaround_time = 0
        start_exe_time = 0
        departure_time = 0
        waiting_time = 0
        input = 0
        remaining_quantum = 0
        remaining_burst_time = 0
        start = 0
        removed = 0


data_array = []
ready_array = []
executed_array = []
waiting_array = []
total_time = 0
count = 0
ready_count = 0
exe_count = 0
wait_count = 0
time_slice = 0
input_after = 0
in_out_time = 0

def main():
    global data_array
    global ready_array
    global executed_array
    global waiting_array
    global total_time
    global count
    global ready_count
    global exe_count
    global wait_count
    global time_slice
    global input_after
    global in_out_time
    global d_count
    
    input_array = [cstruct() for i in range(30)]

    fin = open("input3.txt",'r')

    read_line = "empty"
    read_line = fin.readline()
    
    data = []
    data = read_line.split()
    time_slice = int(data[1])
    
    read_line = fin.readline()
    data = read_line.split()
    input_after = int(data[1])
    
    read_line = fin.readline()
    data = read_line.split()
    in_out_time = int(data[1])
    
    read_line = fin.readline()
    
    while read_line != "":
        read_line = fin.readline()

        if read_line != "":
            
            data = read_line.split()
            
            input_array[count].process_name = data[0]
            input_array[count].arrival_time = int(data[1])
            input_array[count].burst_time = int(data[2])
            input_array[count].remaining_burst_time = int(data[2])
            if data[3] == 'yes':
                input_array[count].input = 1
            else:
                input_array[count].input = 0

            count += 1


    fin.close()

    n = 0
    while n < count:
        data_array.append(input_array[n])
        n += 1
    data_array.sort(key = lambda c: c.arrival_time)
    total_time=data_array[0].arrival_time
    d_count=count
    #for i in range(count):
    #    print("%10s" % data_array[i].process_name,'%10d' % data_array[i].arrival_time,"%10d" % data_array[i].burst_time,"%10r" % (data_array[i].input==1),"%10d" % data_array[i].start_exe_time,"%10d" % data_array[i].waiting_time,"%10d" % data_array[i].turnaround_time)



    print("Process name  , Arrival Time , Burst Time  ,      input  ,Start Exec Time, Waiting Time, Turnaround Time ")
    
    copy_to_ready()
    while  ready_count>0:
       
        if ready_count != 0:
            running = ready_array[0]
            if running.input == 0:
                running = run_process_without_input(running)
           
                if running.removed == 1:
                    executed_array.append(running)
                    exe_count += 1
                    del ready_array[0]
                    ready_count -= 1

                else:
                    ready_array.append(running)
                    del ready_array[0]

            else:
                running,data_array,waiting_array,total_time = run_process_with_input(running,data_array,waiting_array,total_time,time_slice)

        if ready_count == 0 and d_count>0:
            f = 0
            while (data_array[f].arrival_time < total_time):
                f+=1
            total_time = data_array[f].arrival_time
            copy_to_ready()
            
    
        
    #print("")
    #print("Process name  , Arrival Time , Burst Time  ,      input  ,Start Exec Time, Waiting Time, Turnaround Time ")

    

    #for i in range(exe_count):
        #print("%10s" % executed_array[i].process_name,'%10d' % executed_array[i].arrival_time,"%10d" % executed_array[i].burst_time,"%10r" % (executed_array[i].input==0),"%10d" % executed_array[i].start_exe_time,"%10d" % executed_array[i].waiting_time,"%10d" % executed_array[i].turnaround_time)

    sumwt=0
    sumtr=0        
    for i in range(exe_count):
        sumwt = executed_array[i].waiting_time + sumwt
        sumtr = executed_array[i].turnaround_time + sumtr

    print("")
    print("Average waiting time is: %f" %(sumwt/exe_count))
    print("Average Turnaround time is: %f" %(sumtr/exe_count))
    print("")

def run_process_without_input(running):

    global data_array
    global ready_array
    global executed_array
    global waiting_array
    global total_time
    global count
    global ready_count
    global exe_count
    global wait_count
    global time_slice
    global input_after
    global in_out_time

    #while (running.arrival_time > total_time):
        #total_time += 1

    #running.remaining_quantam_time = time_slice
    if running.start == 0:
        running.start_exe_time = total_time
        running.start = 1

    for i in range(time_slice):
        running.remaining_burst_time -= 1        
        total_time += 1
        copy_to_ready()
        if running.remaining_burst_time <= 0:
            running.departure_time = total_time
            running.waiting_time = running.departure_time - running.arrival_time - running.burst_time
            running.turnaround_time = running.departure_time - running.arrival_time
            print("%10s" % running.process_name,'%10d' % running.arrival_time,"%10d" % running.burst_time,"%10r" % (running.input==1),"%10d" % running.start_exe_time,"%10d" % running.waiting_time,"%10d" % running.turnaround_time)
            running.removed = 1
            return running
    return running

d_count=0

def copy_to_ready():

    global data_array
    global ready_array
    global executed_array
    global waiting_array
    global total_time
    global count
    global ready_count
    global exe_count
    global wait_count
    global time_slice
    global input_after
    global in_out_time
    global d_count
   
    i = 0
    while(i<count):
        if  data_array[i].arrival_time == total_time :
            ready_array.append(data_array[i])
            #del data_array[i]
            d_count-=1
            ready_count+=1
        i+=1 

            #data_array[i].removed = 1
            #check = 1
    
   # min_num = data_array[0].arrival_time
   # if ready_count != 0:
    #    for i in range(count):
     #       if min_num == data_array[i].arrival_time:
      #          ready_array.append(data_array[i])
       #         temp += 1
        #        data_array[i].removed = 1
                    
    return

def run_process_with_input(running):

    while (running.arrival_time > total_time):
        total_time += 1

main()



