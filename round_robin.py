class cstruct:
    arrival_time = -1
    burst_time = 0
    removed = 0
    process_name = " "
    turnaround_time = 0
    start_exe_time = 0
    departure_time = 0
    waiting_time = 0
    input = 0
    remaining_quantum = 0
    remaining_burst_time = 0




def main():
    data_array = [cstruct() for i in range(30)]
    ready_array = [cstruct() for i in range(30)]
    executed_array = [cstruct() for i in range(30)]
    waiting_array =  [cstruct() for i in range(30)]
    total_time = 0
    count = 0
    ready_count = 0
    exe_count = 0
    wait_count = 0
    time_slice = 0
    input_after = 0
    in_out_time = 0
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
            
            data_array[count].process_name = data[0]
            data_array[count].arrival_time = int(data[1])
            data_array[count].burst_time = int(data[2])
            data_array[count].remaining_burst_time = int(data[2])
            if data[3] == 'yes':
                data_array[count].input = 1
            count += 1


    fin.close()
    data_array,count,ready_array,ready_count,total_time = copy_to_ready(data_array,count,ready_array,ready_count,total_time)
    while count > 0 :
    
    

        running = ready_array[0]

        if running.input == 0:

            running,data_array,executed_array,total_time = run_process_without_input(running,data_array,executed_array,total_time,time_slice)

            if running.removed == 1:
                data_array,count,ready_array,ready_count,total_time = copy_to_ready(data_array,count,ready_array,ready_count,total_time)
                executed_array[exe_count]=running
                exe_count += 1
                del ready_array[0]
                ready_count -= 1

            else:
                data_array,count,ready_array,ready_count,total_time = copy_to_ready(data_array,count,ready_array,ready_count,total_time)
                ready_array[ready_count-1] = running
                del ready_array[0]
            
        else:
             running,data_array,waiting_array,total_time = run_process_with_input(running,data_array,waiting_array,total_time,time_slice)

    
        
    print("")
    print("Process name  , Arrival Time , Burst Time  ,      input  ,Start Exec Time, Waiting Time, Turnaround Time ")

    

    for i in range(exe_count):
        print("%10s" % executed_array[i].process_name,'%10d' % executed_array[i].arrival_time,"%10d" % executed_array[i].burst_time,"%10r" % (executed_array[i].input==0),"%10d" % executed_array[i].start_exe_time,"%10d" % executed_array[i].waiting_time,"%10d" % executed_array[i].turnaround_time)

    sumwt=0
    sumtr=0        
    for i in range(exe_count):
        sumwt = executed_array[i].waiting_time + sumwt
        sumtr = executed_array[i].turnaround_time + sumtr

    print("")
    print("Average waiting time is: %f" %(sumwt/exe_count))
    print("Average Turnaround time is: %f" %(sumtr/exe_count))
    print("")

def run_process_without_input(running,data_array,executed_array,total_time,time_slice):

    while (running.arrival_time > total_time):
        total_time += 1

    for i in range(time_slice):
        if running.remaining_burst_time == 0:
            running.start_exe_time = total_time
            running.departure_time = running.start_exe_time + running.burst_time
            total_time = running.departure_time
            running.waiting_time = running.departure_time - running.arrival_time - running.burst_time
            running.turnaround_time = running.departure_time - running.arrival_time
            running.removed = 1
            return running,data_array,executed_array,total_time
        running.remaining_burst_time -= 1        
        total_time += 1

    return running,data_array,executed_array,total_time





def copy_to_ready(data_array,count,ready_array,ready_count,total_time):

    min_num = data_array[0].arrival_time
    for i in range(count):
        if min_num > data_array[i].arrival_time:
            min_num = data_array[i].arrival_time

           
    check = 0
    for i in range(count):
        if  data_array[i].arrival_time <= total_time :
            ready_array[ready_count] = data_array[i]
            ready_count += 1
            data_array[i].removed = 1
            check = 1
                

    if ready_count == 0 or check == 0:
        for i in range(count):
            if min_num == data_array[i].arrival_time :
                ready_array[ready_count] = data_array[i]
                ready_count += 1
                data_array[i].removed = 1
                    
    tempc = count
    for i in range(tempc):
        if data_array[i].removed == 1:
            del data_array[i]
            count -= 1

    return data_array,count,ready_array,ready_count,total_time

def run_process_with_input(running,data_array,waiting_array,total_time,time_slice):

    while (running.arrival_time > total_time):
        total_time += 1

    



main()



