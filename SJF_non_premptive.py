import  matplotlib.pyplot as plt
def swap(a , b):
    return b , a

def arrange_arrival(process_id , arrival_time , burst_time):
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
            else:
                break
            
    for i in range(len(process_id)):
        arrival_time[i] = a[i + 1] ;
        
    return process_id ,  arrival_time , burst_time 
        
def SJF_non_premptive(process_id , arrival_time , burst_time):
    o_of_ex = []
    length = len(process_id)
    temp = [-1]*(length + 1)
    crr_time = 0
    crr = 1
    len_a = 1
    completion_time = []
    a = [-1]*(length +  1)

    i = 0 
    while(i < length):
        if(i == 0):
            crr_time = arrival_time[i]
            a[len_a] = burst_time[i]
            temp[len_a] = process_id[i]
            len_a += 1
        else:
            if(arrival_time[i] <= crr_time):
                a[len_a] = burst_time[i]
                temp[len_a] = process_id[i]
                j = len_a
                len_a += 1
                #arranging in min heap
                while(j > 1):
                    if(a[j] < a[j//2]):
                        a[j] , a[j//2] = swap(a[j] , a[j//2])
                        temp[j] , temp[j//2] = swap(temp[j] , temp[j // 2])
                        j = j//2
                    else:
                        break
            else:
                if(len_a == 1):
                    crr_time = arrival_time[i]
                    a[len_a] = burst_time[i]
                    temp[len_a] = process_id[i]
                    len_a += 1
                else:
                    #removing from heap
                    o_of_ex.append(temp[1])
                    crr_time += a[1]
                    completion_time.append(crr_time)
                    len_a = len_a - 1
                    j = len_a
                    a[1] , a[j] = swap(a[1] , a[j])        
                    temp[1] , temp[j] = swap(temp[1] , temp[j])        
                    j = 1
                    while(2*j <= len_a - 1):
                        ind = 0
                        if(2*j == len_a - 1):
                            ind = 2*j
                        else:
                            if(a[2*j] < a[2*j + 1]):
                                ind = 2*j
                            else:
                                ind = 2*j + 1
                        if(a[j] > a[ind]):
                            a[ind] , a[j] = swap(a[ind] , a[j])        
                            temp[ind] , temp[j] = swap(temp[ind] , temp[j])
                        else:
                            break
                    i = i - 1
        i += 1           
    while(len_a > 1):
        o_of_ex.append(temp[1])
        crr_time += a[1]
        completion_time.append(crr_time)
        len_a = len_a - 1
        j = len_a
        a[1] , a[j] = swap(a[1] , a[j])        
        temp[1] , temp[j] = swap(temp[1] , temp[j])
        j = 1        
        while(2*j <= len_a - 1):
            ind = 0
            if(2*j == len_a - 1):
                ind = 2*j
            else:
                if(a[2*j] < a[2*j + 1]):
                    ind = 2*j
                else:
                    ind = 2*j + 1
            if(a[j] > a[ind]):
                a[ind] , a[j] = swap(a[ind] , a[j])        
                temp[ind] , temp[j] = swap(temp[ind] , temp[j])
            else:
                break
    
    temp_arr = [0]*length
    temp_bur = [0]*length
    temp_id = [0]*length
    hash_id = [0]*(length + 1)
    
    print(o_of_ex)
    for i in range(length):
        hash_id[o_of_ex[i]] = i
    
    
    for i in range(length):
        pos = hash_id[process_id[i]]
        temp_arr[pos] = arrival_time[i]
        temp_bur[pos] = burst_time[i]
        temp_id[pos] = process_id[i]
    
    process_id = temp_id
    burst_time = temp_bur
    arrival_time = temp_arr
    
    return completion_time , process_id , burst_time , arrival_time  

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
    process_id = [1 ,2 , 3, 4 ]
    arrival_time = [0 ,0 , 0 , 0]
    burst_time = [21 , 3 , 6 , 2]
    process_id , arrival_time , burst_time = arrange_arrival(process_id , arrival_time , burst_time)
    print(process_id , burst_time , arrival_time)
    completion_time ,process_id , burst_time , arrival_time = SJF_non_premptive(process_id , arrival_time , burst_time)
    print(process_id , burst_time , arrival_time)
     #calculating turnaround time
    turnaround_time = cal_turnaround_time(arrival_time , completion_time)

    #calculating waiting time
    waiting_time = cal_waiting_time(turnaround_time , burst_time)
    
    #calculating average waiting time
    avg_waiting_time = cal_avg_waiting_tinme(waiting_time)
    
    print(completion_time , turnaround_time , waiting_time , avg_waiting_time)
    
    plot_completion_time(process_id, completion_time)
