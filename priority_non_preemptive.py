import  matplotlib.pyplot as plt
def swap(a , b):
    return b , a

def arrange_arrival_with_priority(process_id , arrival_time , burst_time , priority):
    #Making a max heap
    a = []
    a.append(-1) 
    n = len(process_id)
    for i in range(n):
        a.append(arrival_time[i]) 
        j = i + 1 
        while(j > 1):
            if(a[j] > a[j//2]):
                a[j] , a[j//2] = swap(a[j] , a[j//2])
                
                burst_time[j - 1] , burst_time[j//2 - 1] = swap(burst_time[j - 1] , burst_time[j//2 - 1])
    
                process_id[j - 1] , process_id[j//2 - 1] = swap(process_id[j - 1] , process_id[j//2 - 1])
                
                priority[j - 1] , priority[j//2 - 1] = swap(priority[j - 1] , priority[j//2 - 1])
        
                j = j//2
            
            else:
                break
            
    #Doing Heap Sort
    len_a = len(a)
    for i in range(n):
        larg = a[1]
        j = len_a - 1
        a[1] , a[j] = swap(a[1] , a[j])        

        burst_time[0] , burst_time[j - 1] = swap(burst_time[0] , burst_time[j - 1])

        process_id[0] , process_id[j - 1] = swap(process_id[0] , process_id[j - 1])
        
        priority[0] , priority[j - 1] = swap(priority[0] , priority[j - 1])
        
        len_a = len_a - 1
        j = 1
        while(2*j <= len_a - 1):
            ind = 0
            if(2*j == len_a - 1):
                ind = 2*j
            else:
                if(a[2*j] > a[2*j + 1]):
                    ind = 2*j
                else:
                    ind = 2*j + 1
            if(a[j] < a[ind]):
                a[ind] , a[j] = swap(a[ind] , a[j])        

                burst_time[ind - 1 ] , burst_time[j - 1] = swap(burst_time[ind -1] , burst_time[j - 1])

                process_id[ind - 1] , process_id[j - 1] = swap(process_id[ind - 1] , process_id[j - 1])
                
                priority[ind - 1] , priority[j - 1] = swap(priority[ind - 1] , priority[j - 1])
            else:
                break
            
    for i in range(len(process_id)):
        arrival_time[i] = a[i + 1] ;
        
    return process_id , arrival_time , burst_time , priority


def priority_non_preemptive(process_id , arrival_time , burst_time , prioritiy):
    crr_time = 0
    length = len(process_id)
    completion_time = [0]*(length)
    id_a = [-1]*(length + 1)
    pr = [-1]*(length + 1)
    a = [-1]*(length + 1)
    len_a = 1
    i = 0
    while(i < length):
        if(i == 0):
            crr_time = arrival_time[i]
            a[len_a] = burst_time[i]
            pr[len_a] = prioritiy[i]
            id_a[len_a] = process_id[i]
            len_a += 1
        else:
            if(arrival_time[i] <= crr_time):
                a[len_a] = burst_time[i]
                pr[len_a] = prioritiy[i]
                id_a[len_a] = process_id[i]
                j = len_a
                len_a += 1
                #arranging in max heap
                while(j > 1):
                    if(pr[j] > pr[j//2]):
                        pr[j] , pr[j//2] = swap(pr[j] , pr[j//2])
                        a[j] , a[j//2] = swap(a[j] , a[j//2])
                        id_a[j] , id_a[j//2] = swap(id_a[j] , id_a[j // 2])
                        j = j//2
                    else:
                        break
            else:
                if(len_a == 1):
                    crr_time = arrival_time[i]
                    a[len_a] = burst_time[i]
                    pr[len_a] = prioritiy[i]
                    id_a[len_a] = process_id[i]
                    len_a += 1
                else:
                    #removing from heap
                    crr_time += a[1]
                    completion_time[id_a[1] - 1] = crr_time
                    len_a = len_a - 1
                    j = len_a
                    pr[1] , pr[j] = swap(pr[1] , pr[j]) 
                    a[1] , a[j] = swap(a[1] , a[j])        
                    id_a[1] , id_a[j] = swap(id_a[1] , id_a[j])        
                    j = 1
                    while(2*j <= len_a - 1):
                        ind = 0
                        if(2*j == len_a - 1):
                            ind = 2*j
                        else:
                            if(pr[2*j] > pr[2*j + 1]):
                                ind = 2*j
                            else:
                                ind = 2*j + 1
                        if(pr[j] < pr[ind]):
                            pr[ind] , pr[j] = swap(pr[ind] , pr[j]) 
                            a[ind] , a[j] = swap(a[ind] , a[j])        
                            id_a[ind] , id_a[j] = swap(id_a[ind] , id_a[j])
                        else:
                            break
                    i = i - 1
        i += 1
    while(len_a > 1):
        crr_time += a[1]
        completion_time[id_a[1] - 1] = crr_time
        len_a = len_a - 1
        j = len_a
        pr[1] , pr[j] = swap(pr[1] , pr[j]) 
        a[1] , a[j] = swap(a[1] , a[j])        
        id_a[1] , id_a[j] = swap(id_a[1] , id_a[j])        
        j = 1        
        while(2*j <= len_a - 1):
            ind = 0
            if(2*j == len_a - 1):
                ind = 2*j
            else:
                if(pr[2*j] > pr[2*j + 1]):
                    ind = 2*j
                else:
                    ind = 2*j + 1
            if(pr[j] < pr[ind]):
                pr[ind] , pr[j] = swap(pr[ind] , pr[j]) 
                a[ind] , a[j] = swap(a[ind] , a[j])        
                id_a[ind] , id_a[j] = swap(id_a[ind] , id_a[j])
            else:
                break
            
    return completion_time

def cal_turnaround_time(arrival_time , completion_time):
    n = len(completion_time)
    turnaround_time = []
    for i in range(n):
        turnaround_time.append(completion_time[i] - arrival_time[i])
    return turnaround_time

def cal_waiting_time(turmaround_time , burst_time):
    n = len(turnaround_time)
    waiting_time = []
    for i in range(n):
        waiting_time.append(turmaround_time[i] - burst_time[i])
    return waiting_time

def cal_avg_waiting_tinme(waiting_time):
    sum = 0
    for i in range(len(waiting_time)):
        sum += waiting_time[i]
    return sum/len(waiting_time)
        
def plot_completion_time(processes , completion_time):
    plt.plot(completion_time , processes)
    plt.scatter(completion_time , processes , color="red")
    plt.xlabel("completetion_time")
    plt.ylabel("Process Id")
    plt.title("Completion time plot")
    plt.show()    

if __name__ == "__main__":
    process_id = [1 ,2 , 3 , 4 , 5 , 6 , 7]
    arrival_time = [0 , 1 , 2 , 3 , 4 , 5 , 6]
    burst_time = [4 , 2 , 3 , 5 , 1 , 4 , 6]
    priority = [2 , 4 , 6 , 10 , 8 , 12 , 9]
    #arranging w.r.t. arrival time
    process_id , arrival_time , burst_time , priority = arrange_arrival_with_priority(process_id , arrival_time , burst_time , priority)

    completion_time = priority_non_preemptive(process_id , arrival_time , burst_time , priority)
    
    #arranging w.r.t process id
    arrival_time ,process_id , burst_time , priority = arrange_arrival_with_priority(arrival_time , process_id , burst_time , priority)
    
    print(process_id , burst_time , arrival_time , completion_time)
    #calculating turnaround time
    turnaround_time = cal_turnaround_time(arrival_time , completion_time)
    print(turnaround_time)

    #calculating waiting time
    waiting_time = cal_waiting_time(turnaround_time , burst_time)
    print(waiting_time)
    #calculating average waiting time
    avg_waiting_time = cal_avg_waiting_tinme(waiting_time)
    
    print(completion_time , turnaround_time , waiting_time , avg_waiting_time)
    
    plot_completion_time(process_id, completion_time)