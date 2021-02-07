from queue import Queue

import  matplotlib.pyplot as plt
def swap(a , b):
    return b , a

def arrange_arrival_with_priority(process_id , arrival_time , burst_time , priority):
    length = len(process_id)
    for i in range(length):
        for j in range(length - 1):
            if(priority[j] < priority[j + 1]):
                arrival_time[j] , arrival_time[j + 1] = swap(arrival_time[j] , arrival_time[j + 1])
                burst_time[j] , burst_time[j + 1] = swap(burst_time[j] , burst_time[j + 1])
                priority[j] , priority[j + 1] = swap(priority[j] , priority[j + 1])
                process_id[j] , process_id[j + 1] = swap(process_id[j] , process_id[j + 1])
    
    return process_id , arrival_time , burst_time , priority

def arrange_arrival_with_priority1(process_id , arrival_time , burst_time , priority):
    length = len(process_id)
    for i in range(length):
        for j in range(length - 1):
            if(arrival_time[j] > arrival_time[j + 1]):
                arrival_time[j] , arrival_time[j + 1] = swap(arrival_time[j] , arrival_time[j + 1])
                burst_time[j] , burst_time[j + 1] = swap(burst_time[j] , burst_time[j + 1])
                priority[j] , priority[j + 1] = swap(priority[j] , priority[j + 1])
                process_id[j] , process_id[j + 1] = swap(process_id[j] , process_id[j + 1])
    
    return process_id , arrival_time , burst_time , priority


#For sorting normal
def arrange_arrival(process_id , arrival_time , burst_time):
    length = len(process_id)
    for i in range(length):
        for j in range(length - 1):
            if(arrival_time[j] > arrival_time[j + 1]):
                arrival_time[j] , arrival_time[j + 1] = swap(arrival_time[j] , arrival_time[j + 1])
                burst_time[j] , burst_time[j + 1] = swap(burst_time[j] , burst_time[j + 1])
                priority[j] , priority[j + 1] = swap(priority[j] , priority[j + 1])
                
    return process_id ,  arrival_time , burst_time

#For sorting normal
def arrange_burst(process_id , arrival_time , burst_time):
    length = len(process_id)
    for i in range(length):
        for j in range(length - 1):
            if(burst_time[j] > burst_time[j + 1]):
                arrival_time[j] , arrival_time[j + 1] = swap(arrival_time[j] , arrival_time[j + 1])
                burst_time[j] , burst_time[j + 1] = swap(burst_time[j] , burst_time[j + 1])
                process_id[j] , process_id[j + 1] = swap(process_id[j] , process_id[j + 1])
                
    return process_id ,  arrival_time , burst_time

#ROUND ROBIN
def round_robin(process_id , burst_time , arrival_time , time_quantum):
    curr_time = 0
    length = len(process_id)
    completetion_time = [0]*(length)
    a_queue = Queue(maxsize=length)
    id_queue = Queue(maxsize=length)
    curr_a = 0 
    curr_id = 0
    i = 0
    while(i < length):
        if(i == 0):
            a_queue.put(burst_time[i])
            id_queue.put(process_id[i])
            curr_a = a_queue.get()
            curr_id = id_queue.get()
            curr_time = arrival_time[i]
        else:
            if(curr_time >= arrival_time[i]):
                a_queue.put(burst_time[i])
                id_queue.put(process_id[i])
            else:
                if(time_quantum >= curr_a):
                    curr_time += curr_a
                    curr_a = 0
                    completetion_time[curr_id - 1] = curr_time
                    if(not a_queue.empty()):
                        curr_a = a_queue.get()
                        curr_id = id_queue.get()
                    i -= 1
                else:
                    curr_time += time_quantum
                    curr_a -= time_quantum
                    while(i < length and curr_time >= arrival_time[i]):
                        a_queue.put(burst_time[i])
                        id_queue.put(process_id[i])
                        i += 1
                    i -= 1
                    a_queue.put(curr_a)
                    id_queue.put(curr_id)
                    curr_a = a_queue.get()
                    curr_id = id_queue.get()
        i+=1
    while(not a_queue.empty()):
        if(time_quantum >= curr_a):
            curr_time += curr_a
            completetion_time[curr_id - 1] = curr_time
            if(not a_queue.empty()):
                curr_a = a_queue.get()
                curr_id = id_queue.get()
        else:
            curr_time += time_quantum
            curr_a -= time_quantum
            a_queue.put(curr_a)
            id_queue.put(curr_id)
            curr_a = a_queue.get()
            curr_id = id_queue.get()
    else:
        curr_time += curr_a
        completetion_time[curr_id - 1] = curr_time     
    return completetion_time


def priority_non_preemptive(process_id , arrival_time , burst_time , priority):
    crr_time = 0 
    length = len(process_id)
    completion_time = [0]*(length)
    temp_process = []
    temp_arrival = []
    temp_priority = []
    temp_burst = []
    o_of_exec = []
    i = 0
    while(i < length):
        if(i == 0):
            temp_arrival.append(arrival_time[i])
            temp_process.append(process_id[i])
            temp_burst.append(burst_time[i])
            temp_priority.append(priority[i])
            crr_time = arrival_time[i]
        else:
            if(arrival_time[i] <= crr_time):
                temp_arrival.append(arrival_time[i])
                temp_process.append(process_id[i])
                temp_burst.append(burst_time[i])
                temp_priority.append(priority[i])
            else:
                if(len(temp_arrival) == 0):
                    temp_arrival.append(arrival_time[i])
                    temp_process.append(process_id[i])
                    temp_burst.append(burst_time[i])
                    temp_priority.append(priority[i])
                    crr_time = arrival_time[i]
                else:
                    temp_process , temp_arrival , temp_burst , temp_priority = arrange_arrival_with_priority(temp_process , temp_arrival , temp_burst , temp_priority)
                    #executing the first process
                    crr_time += temp_burst[0]
                    completion_time[temp_process[0] - 1] = crr_time
                    if(len(temp_process) > 0):
                        temp_process = temp_process[1:]
                        temp_arrival = temp_arrival[1:]
                        temp_burst = temp_burst[1:]
                        temp_priority = temp_priority[1:]
                    else:
                        temp_process = []
                        temp_arrival = []
                        temp_burst = []
                        temp_priority = []
                i-=1
                        
        i+=1
    while(len(temp_arrival) > 0):
        temp_process , temp_arrival , temp_burst , temp_priority = arrange_arrival_with_priority(temp_process , temp_arrival , temp_burst , temp_priority)
        #executing the first process
        crr_time += temp_burst[0]
        completion_time[temp_process[0] - 1] = crr_time
        if(len(temp_process) > 0):
            temp_process = temp_process[1:]
            temp_arrival = temp_arrival[1:]
            temp_burst = temp_burst[1:]
            temp_priority = temp_priority[1:]
        else:
            temp_process = []
            temp_arrival = []
            temp_burst = []
            temp_priority = []
                    
    return completion_time

#PRIORITY PRE EMPTIVE
def priority_preemptive(process_id , arrival_time , burst_time , priority):
    crr_time = 0
    next_time = 0
    length = len(process_id)
    completion_time = [0]*(length)
    temp_process = []
    temp_arrival = []
    temp_priority = []
    temp_burst = []
    o_of_exec = []
    i = 0
    while(i < length):
        if(i == 0):
            temp_arrival.append(arrival_time[i])
            temp_process.append(process_id[i])
            temp_burst.append(burst_time[i])
            temp_priority.append(priority[i])
            crr_time = arrival_time[i]
            if i < length - 1:
                next_time = arrival_time[i + 1]
        else:
            if(arrival_time[i] <= crr_time):
                temp_arrival.append(arrival_time[i])
                temp_process.append(process_id[i])
                temp_burst.append(burst_time[i])
                temp_priority.append(priority[i])
                if i < length - 1:
                    next_time = arrival_time[i + 1]
            else:
                if(len(temp_process) == 0):
                    temp_arrival.append(arrival_time[i])
                    temp_process.append(process_id[i])
                    temp_burst.append(burst_time[i])
                    temp_priority.append(priority[i])
                    crr_time = arrival_time[i]
                    if i < length - 1:
                        next_time = arrival_time[i + 1]
                else:
                    temp_process , temp_arrival , temp_burst , temp_priority = arrange_arrival_with_priority(temp_process , temp_arrival , temp_burst , temp_priority)
                    if(next_time - crr_time >= temp_burst[0]):
                        #executing the first process
                        crr_time += temp_burst[0]
                        completion_time[temp_process[0] - 1] = crr_time
                        if(len(temp_process) > 0):
                            temp_process = temp_process[1:]
                            temp_arrival = temp_arrival[1:]
                            temp_burst = temp_burst[1:]
                            temp_priority = temp_priority[1:]
                        else:
                            temp_process = []
                            temp_arrival = []
                            temp_burst = []
                            temp_priority = []
                        i-=1
                    else:                    
                        temp_burst[0] = temp_burst[0] - (next_time - crr_time)
                        crr_time = crr_time + (next_time - crr_time)
                        i -= 1
        i += 1
    while(len(temp_arrival) > 0):
        temp_process , temp_arrival , temp_burst , temp_priority = arrange_arrival_with_priority(temp_process , temp_arrival , temp_burst , temp_priority)
        #executing the first process
        crr_time += temp_burst[0]
        completion_time[temp_process[0] - 1] = crr_time
        if(len(temp_process) > 0):
            temp_process = temp_process[1:]
            temp_arrival = temp_arrival[1:]
            temp_burst = temp_burst[1:]
            temp_priority = temp_priority[1:]
        else:
            temp_process = []
            temp_arrival = []
            temp_burst = []
            temp_priority = []
                    
    return completion_time

#FCFS
def FCFS(processes , burst_time , arrival_time):
    n = len(processes)
    completion_time = [0]*n
    curr_time = 0
    for i in range(n):
        #Checking whether the process has yet arrived or not
        #If not arrived , then increasing the current time to make the process arrive
        if(curr_time < arrival_time[i]):
            curr_time = arrival_time[i] 
        #now calculating the completion time
        curr_time = curr_time + burst_time[i]
        completion_time[processes[i] - 1] = curr_time
    return completion_time


#SJF PRE EMPTIVE
def SJF_preemptive(process_id , arrival_time , burst_time):
    crr_time = 0
    next_time = 0
    length = len(process_id)
    completion_time = [0]*(length)
    temp_process = []
    temp_arrival = []
    temp_burst = []
    o_of_exec = []
    i = 0
    while(i < length):
        if(i == 0):
            temp_arrival.append(arrival_time[i])
            temp_process.append(process_id[i])
            temp_burst.append(burst_time[i])
            crr_time = arrival_time[i]
            if i < length - 1:
                next_time = arrival_time[i + 1]
        else:
            if(arrival_time[i] <= crr_time):
                temp_arrival.append(arrival_time[i])
                temp_process.append(process_id[i])
                temp_burst.append(burst_time[i])
                if i < length - 1:
                    next_time = arrival_time[i + 1]
            else:
                if(len(temp_process) == 0):
                    temp_arrival.append(arrival_time[i])
                    temp_process.append(process_id[i])
                    temp_burst.append(burst_time[i])
                    crr_time = arrival_time[i]
                    if i < length - 1:
                        next_time = arrival_time[i + 1]
                else:
                    temp_process , temp_arrival , temp_burst = arrange_burst(temp_process , temp_arrival , temp_burst)
                    if(next_time - crr_time >= temp_burst[0]):
                        #executing the first process
                        crr_time += temp_burst[0]
                        completion_time[temp_process[0] - 1] = crr_time
                        if(len(temp_process) > 0):
                            temp_process = temp_process[1:]
                            temp_arrival = temp_arrival[1:]
                            temp_burst = temp_burst[1:]
                        else:
                            temp_process = []
                            temp_arrival = []
                            temp_burst = []
                        i-=1
                    else:                    
                        temp_burst[0] = temp_burst[0] - (next_time - crr_time)
                        crr_time = crr_time + (next_time - crr_time)
                        i -= 1
        i += 1
    while(len(temp_arrival) > 0):
        temp_process , temp_arrival , temp_burst = arrange_burst(temp_process , temp_arrival , temp_burst)
        #executing the first process
        crr_time += temp_burst[0]
        completion_time[temp_process[0] - 1] = crr_time
        if(len(temp_process) > 0):
            temp_process = temp_process[1:]
            temp_arrival = temp_arrival[1:]
            temp_burst = temp_burst[1:]
        else:
            temp_process = []
            temp_arrival = []
            temp_burst = []
                    
    return completion_time

#SJF NON PRE EMPTIVE
def SJF_non_preemptive(process_id , arrival_time , burst_time):
    crr_time = 0 
    length = len(process_id)
    completion_time = [0]*(length)
    temp_process = []
    temp_arrival = []
    temp_burst = []
    o_of_exec = []
    i = 0
    while(i < length):
        if(i == 0):
            temp_arrival.append(arrival_time[i])
            temp_process.append(process_id[i])
            temp_burst.append(burst_time[i])
            crr_time = arrival_time[i]
        else:
            if(arrival_time[i] <= crr_time):
                temp_arrival.append(arrival_time[i])
                temp_process.append(process_id[i])
                temp_burst.append(burst_time[i])
            else:
                if(len(temp_arrival) == 0):
                    temp_arrival.append(arrival_time[i])
                    temp_process.append(process_id[i])
                    temp_burst.append(burst_time[i])
                    crr_time = arrival_time[i]
                else:
                    temp_process , temp_arrival , temp_burst = arrange_burst(temp_process , temp_arrival , temp_burst)
                    print(temp_process , temp_arrival , temp_burst)
                    #executing the first process
                    crr_time += temp_burst[0]
                    completion_time[temp_process[0] - 1] = crr_time
                    if(len(temp_process) > 0):
                        temp_process = temp_process[1:]
                        temp_arrival = temp_arrival[1:]
                        temp_burst = temp_burst[1:]
                    else:
                        temp_process = []
                        temp_arrival = []
                        temp_burst = []
                i-=1
                        
        i+=1
    while(len(temp_arrival) > 0):
        temp_process , temp_arrival , temp_burst = arrange_burst(temp_process , temp_arrival , temp_burst)
        print(temp_process , temp_arrival , temp_burst)
        #executing the first process
        crr_time += temp_burst[0]
        completion_time[temp_process[0] - 1] = crr_time
        if(len(temp_process) > 0):
            temp_process = temp_process[1:]
            temp_arrival = temp_arrival[1:]
            temp_burst = temp_burst[1:]
        else:
            temp_process = []
            temp_arrival = []
            temp_burst = []
                    
    return completion_time




def cal_turnaround_time(arrival_time , completion_time):
    n = len(completion_time)
    turnaround_time = []
    for i in range(n):
        turnaround_time.append(completion_time[i] - arrival_time[i])
    return turnaround_time

def cal_waiting_time(turnaround_time , burst_time):
    n = len(turnaround_time)
    waiting_time = []
    for i in range(n):
        waiting_time.append(turnaround_time[i] - burst_time[i])
    return waiting_time

def cal_avg_waiting_time(waiting_time):
    sum = 0
    for i in range(len(waiting_time)):
        sum += waiting_time[i]
    return sum/len(waiting_time)
        
def cal_avg_turnaround_time(turnaround_time):
    sum = 0
    for i in range(len(turnaround_time)):
        sum += turnaround_time[i]
    return sum/len(turnaround_time)

def plot_completion_time(processes , completion_time):
    plt.plot(processes , completion_time ,color = "blue" , label = "completion time")
    sum = 0 
    for i in range(len(completion_time)):
        sum += completion_time[i]
    
    plt.plot(processes , [len(processes)*1.0/sum]*len(processes) , color = "green" , label = "avg throughput")
    plt.scatter(processes ,completion_time , color="red")
    plt.ylabel("completetion time")
    plt.xlabel("Process Id")
    plt.title("Completion time plot")
    plt.legend()
    plt.show()

def plot_waiting_time(process , waiting_time , avg_waiting_time):
    plt.plot(process , waiting_time ,color = "blue" , label = "waiting time")
    plt.plot(process , [avg_waiting_time]*len(process) , color = "green" , label = "avg waiting time")
    plt.scatter(process ,waiting_time , color="red")
    plt.ylabel("Waiting time")
    plt.xlabel("Process Id")
    plt.title("Waiting time plot")
    plt.legend()
    plt.show()

def plot_turnaround_time(process , turnaround_time , avg_turnaround_time):
    plt.plot(process , turnaround_time ,color = "blue" , label = "job elapsed time")
    plt.plot(process , [avg_turnaround_time]*len(process) , color = "green" , label = "avg job elapsed time")
    plt.scatter(process ,turnaround_time , color="red")
    plt.ylabel("Job elpased time")
    plt.xlabel("Process Id")
    plt.title("Job elapsed time plot")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    process_id = [1 ,2 , 3 , 4 , 5 , 6]
    arrival_time = [0 ,1 , 2 ,3 , 4 , 5]
    burst_time = [7 , 5 , 3 , 1 , 2 , 1]
    # #arranging w.r.t. arrival time
    # process_id , arrival_time , burst_time , priority = arrange_arrival_with_priority1(process_id , arrival_time , burst_time , priority)
    
    process_id ,  arrival_time , burst_time = arrange_arrival(process_id ,  arrival_time , burst_time )
    
    completion_time = SJF_preemptive(process_id , arrival_time , burst_time)
    
    arrival_time , process_id , burst_time = arrange_arrival(arrival_time , process_id , burst_time )

    print("Process Id")
    print(process_id)

    print("arrival time")
    print(arrival_time)
    
    print("burst time")
    print(burst_time)
    
    print("Completion time")
    print(completion_time)
    
    plot_completion_time(process_id, completion_time)
    
    # arrival_time  , process_id , burst_time = arrange_arrival(arrival_time ,  process_id , burst_time )
    # # #arranging w.r.t process id
    # # arrival_time ,process_id , burst_time , priority = arrange_arrival_with_priority(arrival_time , process_id , burst_time , priority)
    
    # print(process_id , burst_time , arrival_time , completion_time)
    # #calculating turnaround time
    # turnaround_time = cal_turnaround_time(arrival_time , completion_time)
    # print(turnaround_time)

    # #calculating waiting time
    # waiting_time = cal_waiting_time(turnaround_time , burst_time)
    # print(waiting_time)
    # #calculating average waiting time
    # avg_waiting_time = cal_avg_waiting_tinme(waiting_time)
    
    # print(completion_time , turnaround_time , waiting_time , avg_waiting_time)
    
    # plot_completion_time(process_id, completion_time)