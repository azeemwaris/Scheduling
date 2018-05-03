class cstruct:
    arrival_time = 0
    burst_time = 0
    process_name = " "
    turnaround_time = 0
    start_exe_time = 0
    departure_time = 0
    waiting_time = 0




def main():
    data_array = [cstruct() for i in range(30)]
    total_time = 0
    count = 0
    fin = open("input1.txt",'r')
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

    data_array.sort(key=lambda cstruct: cstruct.arrival_time , reverse=True)
    

    print("")
    print("Process name  , Arrival Time , Burst Time ,Start Exec Time, Waiting Time, Turnaround Time ")

    loop = count-1
    while loop >= 0:
        running = data_array[loop]
        data_array[loop],total_time = run_process(running,total_time)
        loop -= 1

    for i in range(count):
        print("%10s" % data_array[i].process_name,'%10d' % data_array[i].arrival_time,"%10d" % data_array[i].burst_time,"%10d" % data_array[i].start_exe_time,"%10d" % data_array[i].waiting_time,"%10d" % data_array[i].turnaround_time)

    sumwt=0
    sumtr=0        
    for i in range(count):
        sumwt = data_array[i].waiting_time + sumwt
        sumtr = data_array[i].turnaround_time + sumtr

    print("")
    print("Average waiting time is: %f" %(sumwt/count))
    print("Average Turnaround time is: %f" %(sumtr/count))
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



