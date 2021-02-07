class Queue:
    def __init__(self , maxsize):
        self.first = 0 
        self.last = 0
        self.maxsize = maxsize
        self.arr = [None]*(maxsize + 1)
    
    def empty(self):
        if(self.first == self.last):
            return 1
        else:
            return 0
    
    def isFull(self):
        if((self.last + 1)%(self.maxsize + 1) == self.first):
            return 1
        else:
            return 0
    
    def put(self , num):
        if(not self.isFull()):
            self.last = (self.last + 1)%(self.maxsize + 1)
            self.arr[self.last] = num
    
    def get(self):
        if(not self.empty()):
            self.first = (self.first + 1)%(self.maxsize + 1)
            return self.arr[self.first]

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
        print("curr_a = ",curr_a)
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
                    print("curr_time before = ",curr_time)
                    curr_time += curr_a
                    print("curr_time after = ",curr_time)
                    curr_a = 0
                    completetion_time[curr_id - 1] = curr_time
                    if(not a_queue.empty()):
                        curr_a = a_queue.get()
                        curr_id = id_queue.get()
                    i -= 1
                else:
                    print("curr_time before = ",curr_time)
                    curr_time += time_quantum
                    print("curr_time after = ",curr_time)
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
        print(curr_a , curr_id)
        i+=1
    print("curr_time = ",curr_time)
    while(not a_queue.empty()):
        if(time_quantum >= curr_a):
            print("curr_time before = ",curr_time)
            curr_time += curr_a
            print("curr_time after = ",curr_time)
            completetion_time[curr_id - 1] = curr_time
            if(not a_queue.empty()):
                curr_a = a_queue.get()
                curr_id = id_queue.get()
        else:
            print("curr_time before = ",curr_time)
            curr_time += time_quantum
            print("curr_time after = ",curr_time)
            curr_a -= time_quantum
            a_queue.put(curr_a)
            id_queue.put(curr_id)
            curr_a = a_queue.get()
            curr_id = id_queue.get()
        print(curr_a)
    else:
        curr_time += curr_a
        completetion_time[curr_id - 1] = curr_time     
    return completetion_time

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
        
def plot_completion_time(process_id , completion_time):
    plt.plot(completion_time , process_id)
    plt.scatter(completion_time , process_id , color="red")
    plt.xlabel("completetion_time")
    plt.ylabel("Process Id")
    plt.title("Completion time plot")
    plt.show()    

if __name__ == "__main__":
    #as i am using heap processes having same arrival time can be reordered by algo
    process_id = [1 ,2 , 3 , 4 , 5 , 6]
    arrival_time = [5 , 4 , 3 , 1 , 2 , 6]
    burst_time = [5 , 6 , 7 , 9 , 2 , 3]
    process_id , arrival_time , burst_time = arrange_arrival(process_id , arrival_time , burst_time)
    print(process_id , burst_time , arrival_time)
    completion_time = round_robin(process_id , burst_time , arrival_time , 3)
    arrival_time ,process_id , burst_time = arrange_arrival(arrival_time ,process_id , burst_time)
    print(completion_time)
    print(process_id , burst_time , arrival_time)
      #calculating turnaround time
    turnaround_time = cal_turnaround_time(arrival_time , completion_time)

    #calculating waiting time
    waiting_time = cal_waiting_time(turnaround_time , burst_time)
    
    #calculating average waiting time
    avg_waiting_time = cal_avg_waiting_tinme(waiting_time)
    
    print(completion_time , turnaround_time , waiting_time , avg_waiting_time)
    
    plot_completion_time(process_id, completion_time)
