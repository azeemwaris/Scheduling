class cstruct:
    arrival_time = 0
    burst_time = 0
    process_name = " "
    turnaround_time = 0
    start_exe_time = 0
    departure_time = 0
    waiting_time = 0
    removed = 0




def main():
    data_array = [cstruct() for i in range(30)]
    ready_array = [cstruct() for i in range(30)]
    executed_array = [cstruct() for i in range(30)]
    total_time = 0
    count = 0
    ready_count = 0
    exe_count = 0
    fin = open("input2.txt",'r')
    fin.readline()
    
    read_line = "empty"

    while read_line != "":
        read_line = fin.readline()

        if read_line != "":
            data = []
            data = read_line.split()
            
            data_array[count].process_name = data[0]
            data_array[count].arrival_time = int(data[1])
            data_array[count].burst_time = int(data[2])
            count += 1


    fin.close()

    while count > 0 :
    
        min_num = data_array[0].arrival_time
        for i in range(count):
            if min_num > data_array[i].arrival_time:
                min_num = data_array[i].arrival_time
        print(min_num)         
        check = 0
        for i in range(count):
            if min_num == data_array[i].arrival_time and data_array[i].arrival_time <= total_time :
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
        #print(count)

        #for i in range(count):
        #   print(data_array[i].process_name)
        print("")
        ready_array.sort(key=lambda cstruct: cstruct.burst_time , reverse=True)

        #for i in range(ready_count):
        #    print(ready_array[i].process_name)


        temp=ready_count-1
        running = ready_array[temp]
        executed_array[exe_count],total_time = run_process(running,total_time)
        exe_count += 1
        del ready_array[ready_count-1]
        ready_count -= 1
        print(ready_array[ready_count-1].process_name)

    ready_array.sort(key=lambda cstruct: cstruct.burst_time , reverse=True)
    while (ready_count > 0):

        temp = ready_count-1
        running = ready_array[temp]
        executed_array[exe_count],total_time = run_process(running,total_time)
        exe_count += 1
        del ready_array[ready_count-1]
        ready_count -= 1
        
       
    print("")
    print("Process name  , Arrival Time , Burst Time ,Start Exec Time, Waiting Time, Turnaround Time ")

    

    for i in range(exe_count):
        print("%10s" % executed_array[i].process_name,'%10d' % executed_array[i].arrival_time,"%10d" % executed_array[i].burst_time,"%10d" % executed_array[i].start_exe_time,"%10d" % executed_array[i].waiting_time,"%10d" % executed_array[i].turnaround_time)

    sumwt=0
    sumtr=0        
    for i in range(exe_count):
        sumwt = executed_array[i].waiting_time + sumwt
        sumtr = executed_array[i].turnaround_time + sumtr

    print("")
    print("Average waiting time is: %f" %(sumwt/exe_count))
    print("Average Turnaround time is: %f" %(sumtr/exe_count))
    print("")

def run_process(running,total_time):

    while running.arrival_time > total_time:
        total_time += 1

    running.start_exe_time = total_time
    running.departure_time = running.start_exe_time + running.burst_time
    total_time = running.departure_time
    running.waiting_time = running.departure_time - running.arrival_time - running.burst_time
    running.turnaround_time = running.departure_time - running.arrival_time

    return running,total_time




main()



