from tkinter import *
from tkinter import font
import  matplotlib.pyplot as plt
from tkinter import messagebox


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

def swap(a , b):
    return b , a


#FOR arranging the priority
def arrange_all(process_id , arrival_time , burst_time , priority , completion_time):
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
                
                completion_time[j - 1] , completion_time[j//2 - 1] = swap(completion_time[j - 1] , completion_time[j//2 - 1])
        
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
        
        completion_time[0] , completion_time[j - 1] = swap(completion_time[0] , completion_time[j - 1])
        
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
                
                completion_time[ind - 1] , completion_time[j - 1] = swap(completion_time[ind - 1] , completion_time[j - 1])
            else:
                break
            
    for i in range(len(process_id)):
        arrival_time[i] = a[i + 1] ;
        
    return process_id , arrival_time , burst_time , priority , completion_time


#FOR arranging the priority
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


#For sorting normal
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


#PRIORITY NON PRE EMPTIVE
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


#PRIORITY PRE EMPTIVE
def priority_preemptive(process_id , arrival_time , burst_time , prioritiy):
    crr_time = 0
    next_time = 0
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
            if i < length - 1:
                next_time = arrival_time[i + 1]
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
                if i < length - 1:
                    next_time = arrival_time[i + 1]
            else:
                if(len_a == 1):
                    crr_time = arrival_time[i]
                    a[len_a] = burst_time[i]
                    pr[len_a] = prioritiy[i]
                    id_a[len_a] = process_id[i]
                    len_a += 1
                    if i < length - 1:
                        next_time = arrival_time[i + 1]
                else:
                    #removing from heap
                    if(next_time - crr_time >= a[1]):
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
                    else:                    
                        a[1] = a[1] - (next_time - crr_time)
                        crr_time = crr_time + (next_time - crr_time)
                        i -= 1
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


#SJF PREEMPTIVE
def SJF_preemptive(process_id , burst_time , arrival_time):
    curr_time = 0
    next_time = 0
    len_a = 1
    length = len(process_id)
    a = [-1]*(length + 1)
    id_a = [-1]*(length + 1)
    completion_time = [0]*(length)
    completed_id = []
    i = 0
    while(i < length):
        if(i == 0):
            a[len_a] = burst_time[i]
            id_a[len_a] = process_id[i]
            len_a += 1
            curr_time = arrival_time[i]
            if i < length - 1:
                next_time = arrival_time[i + 1]
        else:
            if(arrival_time[i] <= curr_time):
                a[len_a] = burst_time[i]
                id_a[len_a] = process_id[i]
                j = len_a
                len_a += 1
                #arranging in min heap
                while(j > 1):
                    if(a[j] < a[j//2]):
                        a[j] , a[j//2] = swap(a[j] , a[j//2])
                        id_a[j] , id_a[j//2] = swap(id_a[j] , id_a[j // 2])
                        j = j//2
                    else:
                        break
                if i < length - 1:
                    next_time = arrival_time[i + 1]
            else:
                if(len_a == 1):
                    a[len_a] = burst_time[i]
                    id_a[len_a] = process_id[i]
                    len_a += 1
                    curr_time = arrival_time[i]
                    if i < length - 1:
                        next_time = arrival_time[i + 1]
                else:
                    if(next_time - curr_time >= a[1]):
                        completion_time[id_a[1] - 1] += curr_time + a[1]
                        completed_id.append(id_a[1])
                        curr_time += a[1]
                        #removing from heap
                        len_a = len_a - 1
                        j = len_a
                        a[1] , a[j] = swap(a[1] , a[j])        
                        id_a[1] , id_a[j] = swap(id_a[1] , id_a[j])        
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
                                id_a[ind] , id_a[j] = swap(id_a[ind] , id_a[j])
                            else:
                                break
                        i = i - 1
                    else:                    
                        a[1] = a[1] - (next_time - curr_time)
                        curr_time = curr_time + (next_time - curr_time)
                        i -= 1     
        i += 1
        
    while(len_a > 1):
        completed_id.append(id_a[1])
        curr_time += a[1]
        completion_time[id_a[1] - 1] += curr_time
        len_a = len_a - 1
        j = len_a
        a[1] , a[j] = swap(a[1] , a[j])        
        id_a[1] , id_a[j] = swap(id_a[1] , id_a[j])
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
                id_a[ind] , id_a[j] = swap(id_a[ind] , id_a[j])
            else:
                break
    
    # print(completion_time , completed_id) ;
    # temp_completion = completion_time.copy()
    # for i in range(length):
    #     completion_time[i] = temp_completion[process_id[i] - 1]
    return completion_time

#SJF NON PRE EMPTIVE
def SJF_non_premptive(process_id , arrival_time , burst_time):
    length = len(process_id)
    crr_time = 0
    len_a = 1
    a = [-1]*(length +  1)
    id_a = [-1]*(length + 1)
    completion_time = [0]*(length)
    completed_id = []

    i = 0 
    while(i < length):
        if(i == 0):
            crr_time = arrival_time[i]
            a[len_a] = burst_time[i]
            id_a[len_a] = process_id[i]
            len_a += 1
        else:
            if(arrival_time[i] <= crr_time):
                a[len_a] = burst_time[i]
                id_a[len_a] = process_id[i]
                j = len_a
                len_a += 1
                #arranging in min heap
                while(j > 1):
                    if(a[j] < a[j//2]):
                        a[j] , a[j//2] = swap(a[j] , a[j//2])
                        id_a[j] , id_a[j//2] = swap(id_a[j] , id_a[j // 2])
                        j = j//2
                    else:
                        break
            else:
                if(len_a == 1):
                    crr_time = arrival_time[i]
                    a[len_a] = burst_time[i]
                    id_a[len_a] = process_id[i]
                    len_a += 1
                else:
                    #removing from heap
                    completion_time[id_a[1] - 1] += crr_time + a[1]
                    completed_id.append(id_a[1])
                    crr_time += a[1]
                    len_a = len_a - 1
                    j = len_a
                    a[1] , a[j] = swap(a[1] , a[j])        
                    id_a[1] , id_a[j] = swap(id_a[1] , id_a[j])
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
                            id_a[ind] , id_a[j] = swap(id_a[ind] , id_a[j])
                        else:
                            break
                    i = i - 1
        i += 1           
    while(len_a > 1):
        completed_id.append(id_a[1])
        crr_time += a[1]
        completion_time[id_a[1] - 1] += crr_time
        len_a = len_a - 1
        j = len_a
        a[1] , a[j] = swap(a[1] , a[j])        
        id_a[1] , id_a[j] = swap(id_a[1] , id_a[j])
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
    
def perform(type , new_win):
    temp_arrival = new_win_arrival_time_entry.get()
    temp_burst = new_win_burst_time_entry.get()
    temp_priority = ""
    priority_temp = []
    time_quantum = 0
    if(type == "PP" or type == "PNP"):
        temp_priority = new_win_priority_entry.get() 
        priority_temp = temp_priority.split(",")
    elif(type == "RR"):
        time_quantum = int(new_win_time_quantum_entry.get())

    arrival_time_temp = temp_arrival.split(",")
    burst_time_temp = temp_burst.split(",")
    if( len(arrival_time_temp) == len(burst_time_temp)):
        length = len(arrival_time_temp)
        process_id = [0]*length
        arrival_time = [0]*length
        burst_time = [0]*length
        priority = [0]*length
        for i in range(length):
            process_id[i] = i + 1
            arrival_time[i] = eval(arrival_time_temp[i])
            burst_time[i] = eval(burst_time_temp[i])
        if(type == "FCFS"):
            new_win.destroy()
            process_id ,  arrival_time , burst_time = arrange_arrival(process_id ,  arrival_time , burst_time ) 
            completion_time = FCFS(process_id , burst_time , arrival_time)
            arrival_time  , process_id , burst_time = arrange_arrival(arrival_time ,  process_id , burst_time)
            #now sorting in order to make it as it was entered in the algo
            process_id , arrival_time , burst_time , completion_time = arrange_arrival_with_priority(process_id , arrival_time , burst_time , completion_time)
            turnaround_time = cal_turnaround_time(arrival_time , completion_time)
            waiting_time = cal_waiting_time(turnaround_time , burst_time)
            avg_waiting_time = cal_avg_waiting_time(waiting_time)
            avg_turnaround_time = cal_avg_turnaround_time(turnaround_time)
            lat_win = Toplevel()
            lat_win.configure(background = '#FFF9A6')
            process_id_label = Label(lat_win  , bg = "#FFF9A6", text = "Process id : "+str(process_id)[1:-1] , font = font.Font(size = 13) , padx = 100)
            arrival_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Arrival time : "+str(arrival_time)[1:-1] ,font = font.Font(size = 13) , padx = 100)
            burst_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Burst time : "+str(burst_time)[1:-1] , font = font.Font(size = 13) , padx = 100)
            completion_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Completion time : "+str(completion_time)[1:-1] , font = font.Font(size = 13) , padx = 100)
            turnaround_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Turnaround time: "+str(turnaround_time)[1:-1] , font = font.Font(size = 13) , padx = 100)
            waiting_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Waiting time : "+str(waiting_time)[1:-1] , font = font.Font(size = 13) , padx = 100)
            avg_waiting_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Average waiting time : "+str(avg_waiting_time) , font = font.Font(size = 13) , padx = 100)
            comp_button = Button(lat_win , text = "Plot completion time graph" ,bg = "#FF5733" , fg = "white",font = font.Font(size = 13), command = lambda: plot_completion_time(process_id , completion_time))
            wait_button = Button(lat_win , text = "Plot waiting time graph" ,bg = "#FF5733" , fg = "white",font = font.Font(size = 13), command = lambda : plot_waiting_time(process_id , waiting_time , avg_waiting_time))
            job_button = Button(lat_win , text = "Plot job elapsed time graph" ,bg = "#FF5733" , fg = "white",font = font.Font(size = 13), command = lambda:plot_turnaround_time(process_id , turnaround_time , avg_turnaround_time))
            process_id_label.grid(row = 0 , column = 0 , pady = 10)
            arrival_time_label.grid(row = 1 , column = 0 , pady = 10)
            burst_time_label.grid(row = 2 , column = 0 , pady = 5)
            completion_time_label.grid(row = 3 , column = 0 , pady = 5)
            turnaround_time_label.grid(row = 4 , column = 0 , pady = 5)
            waiting_time_label.grid(row = 5 , column = 0 , pady = 5)
            avg_waiting_time_label.grid(row = 6 , column = 0 , pady = 5 , padx = 20)
            comp_button.grid(row = 7 , column = 0 , pady = 10)
            wait_button.grid(row = 8 , column = 0 , pady = 10)
            job_button.grid(row = 9 , column = 0 , pady = 10)
        elif(type == "SJFP"):
            new_win.destroy()
            process_id ,  arrival_time , burst_time = arrange_arrival(process_id ,  arrival_time , burst_time ) 
            completion_time = SJF_preemptive(process_id , burst_time , arrival_time)
            arrival_time  , process_id , burst_time = arrange_arrival(arrival_time ,  process_id , burst_time)
            #now sorting in order to make it as it was entered in the algo
            process_id , arrival_time , burst_time , completion_time = arrange_arrival_with_priority(process_id , arrival_time , burst_time , completion_time)
            turnaround_time = cal_turnaround_time(arrival_time , completion_time)
            waiting_time = cal_waiting_time(turnaround_time , burst_time)
            avg_waiting_time = cal_avg_waiting_time(waiting_time)
            avg_turnaround_time = cal_avg_turnaround_time(turnaround_time)
            lat_win = Toplevel()
            lat_win.configure(background = '#FFF9A6')
            process_id_label = Label(lat_win  , bg = "#FFF9A6", text = "Process id : "+str(process_id)[1:-1], font = font.Font(size = 13) , padx = 100)
            arrival_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Arrival time : "+str(arrival_time)[1:-1], font = font.Font(size = 13) , padx = 100)
            burst_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Burst time : "+str(burst_time)[1:-1], font = font.Font(size = 13) , padx = 100)
            completion_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Completion time : "+str(completion_time)[1:-1], font = font.Font(size = 13) , padx = 100)
            turnaround_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Turnaround time: "+str(turnaround_time)[1:-1], font = font.Font(size = 13) , padx = 100)
            waiting_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Waiting time : "+str(waiting_time)[1:-1], font = font.Font(size = 13) , padx = 100)
            avg_waiting_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Average waiting time : "+str(avg_waiting_time) , font = font.Font(size = 13) , padx = 100)
            comp_button = Button(lat_win , text = "Plot completion time graph",bg = "#FF5733" , fg = "white",font = font.Font(size = 13) , command = lambda: plot_completion_time(process_id , completion_time))
            wait_button = Button(lat_win , text = "Plot waiting time graph" ,bg = "#FF5733" , fg = "white",font = font.Font(size = 13), command = lambda : plot_waiting_time(process_id , waiting_time , avg_waiting_time))
            job_button = Button(lat_win , text = "Plot job elapsed time graph" ,bg = "#FF5733" , fg = "white",font = font.Font(size = 13), command = lambda:plot_turnaround_time(process_id , turnaround_time , avg_turnaround_time))

            process_id_label.grid(row = 0 , column = 0 , pady = 10)
            arrival_time_label.grid(row = 1 , column = 0 , pady = 10)
            burst_time_label.grid(row = 2 , column = 0 , pady = 5)
            completion_time_label.grid(row = 3 , column = 0 , pady = 5)
            turnaround_time_label.grid(row = 4 , column = 0 , pady = 5)
            waiting_time_label.grid(row = 5 , column = 0 , pady = 5)
            avg_waiting_time_label.grid(row = 6 , column = 0 , pady = 5 , padx = 20)
            comp_button.grid(row = 7 , column = 0 , pady = 10)
            wait_button.grid(row = 8 , column = 0 , pady = 10)
            job_button.grid(row = 9 , column = 0 , pady = 10)
        elif(type == "SJFNP"):
            new_win.destroy()
            process_id ,  arrival_time , burst_time = arrange_arrival(process_id ,  arrival_time , burst_time ) 
            completion_time = SJF_non_premptive(process_id , arrival_time , burst_time)
            arrival_time  , process_id , burst_time = arrange_arrival(arrival_time ,  process_id , burst_time)
            #now sorting in order to make it as it was entered in the algo
            process_id , arrival_time , burst_time , completion_time = arrange_arrival_with_priority(process_id , arrival_time , burst_time , completion_time)
            turnaround_time = cal_turnaround_time(arrival_time , completion_time)
            waiting_time = cal_waiting_time(turnaround_time , burst_time)
            avg_waiting_time = cal_avg_waiting_time(waiting_time)
            avg_turnaround_time = cal_avg_turnaround_time(turnaround_time)
            lat_win = Toplevel()
            lat_win.configure(background = '#FFF9A6')
            process_id_label = Label(lat_win  , bg = "#FFF9A6", text = "Process id : "+str(process_id)[1:-1], font = font.Font(size = 13) , padx = 100)
            arrival_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Arrival time : "+str(arrival_time)[1:-1], font = font.Font(size = 13) , padx = 100)
            burst_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Burst time : "+str(burst_time)[1:-1], font = font.Font(size = 13) , padx = 100)
            completion_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Completion time : "+str(completion_time)[1:-1], font = font.Font(size = 13) , padx = 100)
            turnaround_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Turnaround time: "+str(turnaround_time)[1:-1], font = font.Font(size = 13) , padx = 100)
            waiting_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Waiting time : "+str(waiting_time)[1:-1], font = font.Font(size = 13) , padx = 100)
            avg_waiting_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Average waiting time : "+str(avg_waiting_time), font = font.Font(size = 13) , padx = 100)
            comp_button = Button(lat_win , text = "Plot completion time graph" ,bg = "#FF5733" , fg = "white",font = font.Font(size = 13), command = lambda: plot_completion_time(process_id , completion_time))
            wait_button = Button(lat_win , text = "Plot waiting time graph" ,bg = "#FF5733" , fg = "white",font = font.Font(size = 13), command = lambda : plot_waiting_time(process_id , waiting_time , avg_waiting_time))
            job_button = Button(lat_win , text = "Plot job elapsed time graph" ,bg = "#FF5733" , fg = "white",font = font.Font(size = 13), command = lambda:plot_turnaround_time(process_id , turnaround_time , avg_turnaround_time))

            process_id_label.grid(row = 0 , column = 0 , pady = 10)
            arrival_time_label.grid(row = 1 , column = 0 , pady = 10)
            burst_time_label.grid(row = 2 , column = 0 , pady = 5)
            completion_time_label.grid(row = 3 , column = 0 , pady = 5)
            turnaround_time_label.grid(row = 4 , column = 0 , pady = 5)
            waiting_time_label.grid(row = 5 , column = 0 , pady = 5)
            avg_waiting_time_label.grid(row = 6 , column = 0 , pady = 5 , padx = 20)
            comp_button.grid(row = 7 , column = 0 , pady = 10)
            wait_button.grid(row = 8 , column = 0 , pady = 10)
            job_button.grid(row = 9 , column = 0 , pady = 10)
        elif(type == "RR"):
            new_win.destroy()
            process_id ,  arrival_time , burst_time = arrange_arrival(process_id ,  arrival_time , burst_time ) 
            completion_time = round_robin(process_id , burst_time , arrival_time , time_quantum)
            arrival_time  , process_id , burst_time = arrange_arrival(arrival_time ,  process_id , burst_time)
            #now sorting in order to make it as it was entered in the algo
            process_id , arrival_time , burst_time , completion_time = arrange_arrival_with_priority(process_id , arrival_time , burst_time , completion_time)
            turnaround_time = cal_turnaround_time(arrival_time , completion_time)
            waiting_time = cal_waiting_time(turnaround_time , burst_time)
            avg_waiting_time = cal_avg_waiting_time(waiting_time)
            avg_turnaround_time = cal_avg_turnaround_time(turnaround_time)
            lat_win = Toplevel()
            lat_win.configure(background = '#FFF9A6')
            process_id_label = Label(lat_win  , bg = "#FFF9A6", text = "Process id : "+str(process_id)[1:-1],font = font.Font(size = 13) , padx = 100)
            arrival_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Arrival time : "+str(arrival_time)[1:-1],font = font.Font(size = 13) , padx = 100)
            burst_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Burst time : "+str(burst_time)[1:-1],font = font.Font(size = 13) , padx = 100)
            time_quantum_label = Label(lat_win  , bg = "#FFF9A6", text = "Time Quantum : "+str(time_quantum),font = font.Font(size = 13) , padx = 100)
            completion_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Completion time : "+str(completion_time)[1:-1],font = font.Font(size = 13) , padx = 100)
            turnaround_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Turnaround time: "+str(turnaround_time)[1:-1],font = font.Font(size = 13) , padx = 100)
            waiting_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Waiting time : "+str(waiting_time)[1:-1],font = font.Font(size = 13) , padx = 100)
            avg_waiting_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Average waiting time : "+str(avg_waiting_time),font = font.Font(size = 13))
            comp_button = Button(lat_win , text = "Plot completion time graph" ,bg = "#FF5733" , fg = "white",font = font.Font(size = 13), command = lambda: plot_completion_time(process_id , completion_time))
            wait_button = Button(lat_win , text = "Plot waiting time graph" ,bg = "#FF5733" , fg = "white",font = font.Font(size = 13), command = lambda : plot_waiting_time(process_id , waiting_time , avg_waiting_time))
            job_button = Button(lat_win , text = "Plot job elapsed time graph" ,bg = "#FF5733" , fg = "white",font = font.Font(size = 13), command = lambda:plot_turnaround_time(process_id , turnaround_time , avg_turnaround_time))

            process_id_label.grid(row = 0 , column = 0 , pady = 10)
            arrival_time_label.grid(row = 1 , column = 0 , pady = 10)
            burst_time_label.grid(row = 2 , column = 0 , pady = 5)
            time_quantum_label.grid(row = 3 , column = 0 ,pady = 5)
            completion_time_label.grid(row = 4 , column = 0 , pady = 5)
            turnaround_time_label.grid(row = 5 , column = 0 , pady = 5)
            waiting_time_label.grid(row = 6 , column = 0 , pady = 5)
            avg_waiting_time_label.grid(row = 7 , column = 0 , pady = 5 , padx = 20)
            comp_button.grid(row = 8 , column = 0 , pady = 10)
            wait_button.grid(row = 9 , column = 0 , pady = 10)
            job_button.grid(row = 10 , column = 0 , pady = 10)
        elif(type == "PNP"):
            if(len(arrival_time_temp) == len(burst_time_temp) and len(burst_time_temp) == len(priority_temp)):
                new_win.destroy()
                for i in range(length):
                    priority[i] = eval(priority_temp[i])
                process_id , arrival_time , burst_time , priority = arrange_arrival_with_priority(process_id , arrival_time , burst_time , priority)
                completion_time = priority_non_preemptive(process_id , arrival_time , burst_time , priority)
                arrival_time ,process_id , burst_time , priority = arrange_arrival_with_priority(arrival_time , process_id , burst_time , priority)
                process_id , arrival_time , burst_time , priority , completion_time = arrange_all(process_id , arrival_time , burst_time , priority , completion_time)
                turnaround_time = cal_turnaround_time(arrival_time , completion_time)
                waiting_time = cal_waiting_time(turnaround_time , burst_time)
                avg_waiting_time = cal_avg_waiting_time(waiting_time)
                avg_turnaround_time = cal_avg_turnaround_time(turnaround_time)
                lat_win = Toplevel()
                lat_win.configure(background = '#FFF9A6')
                process_id_label = Label(lat_win  , bg = "#FFF9A6", text = "Process id : "+str(process_id)[1:-1], font = font.Font(size = 13) , padx = 100)
                arrival_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Arrival time : "+str(arrival_time)[1:-1], font = font.Font(size = 13) , padx = 100)
                burst_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Burst time : "+str(burst_time)[1:-1], font = font.Font(size = 13) , padx = 100)
                priority_label = Label(lat_win  , bg = "#FFF9A6", text = "Priority : "+str(priority)[1:-1], font = font.Font(size = 13) , padx = 100)
                completion_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Completion time : "+str(completion_time)[1:-1], font = font.Font(size = 13) , padx = 100)
                turnaround_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Turnaround time: "+str(turnaround_time)[1:-1], font = font.Font(size = 13) , padx = 100)
                waiting_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Waiting time : "+str(waiting_time)[1:-1], font = font.Font(size = 13) , padx = 100)
                avg_waiting_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Average waiting time : "+str(avg_waiting_time), font = font.Font(size = 13) , padx = 100)
                comp_button = Button(lat_win , text = "Plot completion time graph" ,bg = "#FF5733" , fg = "white",font = font.Font(size = 13), command = lambda: plot_completion_time(process_id , completion_time))
                wait_button = Button(lat_win , text = "Plot waiting time graph" ,bg = "#FF5733" , fg = "white",font = font.Font(size = 13), command = lambda : plot_waiting_time(process_id , waiting_time , avg_waiting_time))
                job_button = Button(lat_win , text = "Plot job elapsed time graph" ,bg = "#FF5733" , fg = "white",font = font.Font(size = 13), command = lambda:plot_turnaround_time(process_id , turnaround_time , avg_turnaround_time))

                process_id_label.grid(row = 0 , column = 0 , pady = 10)
                arrival_time_label.grid(row = 1 , column = 0 , pady = 10)
                burst_time_label.grid(row = 2 , column = 0 , pady = 5)
                priority_label.grid(row = 3 , column = 0 , pady = 5)
                completion_time_label.grid(row = 4 , column = 0 , pady = 5)
                turnaround_time_label.grid(row = 5 , column = 0 , pady = 5)
                waiting_time_label.grid(row = 6 , column = 0 , pady = 5)
                avg_waiting_time_label.grid(row = 7 , column = 0 , pady = 5 , padx = 20)
                comp_button.grid(row = 8 , column = 0 , pady = 10)
                wait_button.grid(row = 9 , column = 0 , pady = 10)
                job_button.grid(row = 10 , column = 0 , pady = 10)
            else:
                messagebox.showerror("Error" , "Please make sure that number of values in priority , arrival time and burst time are same")
        elif(type == "PP"):
            if(len(arrival_time_temp) == len(burst_time_temp) and len(burst_time_temp) == len(priority_temp)):
                new_win.destroy()
                for i in range(length):
                    priority[i] = eval(priority_temp[i])
                process_id , arrival_time , burst_time , priority = arrange_arrival_with_priority(process_id , arrival_time , burst_time , priority)
                completion_time = priority_preemptive(process_id , arrival_time , burst_time , priority)
                arrival_time ,process_id , burst_time , priority = arrange_arrival_with_priority(arrival_time , process_id , burst_time , priority)
                process_id , arrival_time , burst_time , priority , completion_time = arrange_all(process_id , arrival_time , burst_time , priority , completion_time)
                turnaround_time = cal_turnaround_time(arrival_time , completion_time)
                waiting_time = cal_waiting_time(turnaround_time , burst_time)
                avg_waiting_time = cal_avg_waiting_time(waiting_time)
                avg_turnaround_time = cal_avg_turnaround_time(turnaround_time)
                lat_win = Toplevel()
                lat_win.configure(background = '#FFF9A6')
                process_id_label = Label(lat_win  , bg = "#FFF9A6", text = "Process id : "+str(process_id)[1:-1], font = font.Font(size = 13) , padx = 100)
                arrival_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Arrival time : "+str(arrival_time)[1:-1], font = font.Font(size = 13), padx = 100)
                burst_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Burst time : "+str(burst_time)[1:-1], font = font.Font(size = 13), padx = 100)
                priority_label = Label(lat_win  , bg = "#FFF9A6", text = "Priority : "+str(priority)[1:-1], font = font.Font(size = 13), padx = 100)
                completion_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Completion time : "+str(completion_time)[1:-1], font = font.Font(size = 13), padx = 100)
                turnaround_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Turnaround time: "+str(turnaround_time)[1:-1], font = font.Font(size = 13), padx = 100)
                waiting_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Waiting time : "+str(waiting_time)[1:-1], font = font.Font(size = 13), padx = 100)
                avg_waiting_time_label = Label(lat_win  , bg = "#FFF9A6", text = "Average waiting time : "+str(avg_waiting_time), font = font.Font(size = 13), padx = 100)
                comp_button = Button(lat_win , text = "Plot completion time graph" ,bg = "#FF5733" , fg = "white",font = font.Font(size = 13), command = lambda: plot_completion_time(process_id , completion_time))
                wait_button = Button(lat_win , text = "Plot waiting time graph" ,bg = "#FF5733" , fg = "white",font = font.Font(size = 13), command = lambda : plot_waiting_time(process_id , waiting_time , avg_waiting_time))
                job_button = Button(lat_win , text = "Plot job elapsed time graph" ,bg = "#FF5733" , fg = "white",font = font.Font(size = 13), command = lambda:plot_turnaround_time(process_id , turnaround_time , avg_turnaround_time))

                process_id_label.grid(row = 0 , column = 0 , pady = 10)
                arrival_time_label.grid(row = 1 , column = 0 , pady = 10)
                burst_time_label.grid(row = 2 , column = 0 , pady = 5)
                priority_label.grid(row = 3 , column = 0 , pady = 5)
                completion_time_label.grid(row = 4 , column = 0 , pady = 5)
                turnaround_time_label.grid(row = 5 , column = 0 , pady = 5)
                waiting_time_label.grid(row = 6 , column = 0 , pady = 5)
                avg_waiting_time_label.grid(row = 7 , column = 0 , pady = 5 , padx = 20)
                comp_button.grid(row = 8 , column = 0 , pady = 10)
                wait_button.grid(row = 9 , column = 0 , pady = 10)
                job_button.grid(row = 10 , column = 0 , pady = 10)
            else:
                messagebox.showerror("Error" , "Please make sure that number of values in priority , arrival time and burst time are same")

    else:
        messagebox.showerror("Error" , "Please make sure that number of values in arrival time and burst time are same")

def set_lists_new(type):
    new_win = Toplevel()
    title = ""
    if(type == "FCFS"):
        title = "FCFS"
    elif(type == "SJFP"):
        title = "SJF Preemptive"
    elif(type == "SJFNP"):
        title = "SJF Non-Preemptive"
    elif(type == "PP"):
        title = "Priority Preemptive"
    elif(type == "PNP"):
        title = "Priority Non Preemptive"
    elif(type == "RR"):
        title = "Round Robin"
    new_win.title(title)
    new_win.configure(background = "#FFF9A6")
    new_win_info_label = Label(new_win ,bg = "#FFF9A6", text = "Values must be seperated by commas\neg:- 1,2,3,4,5,6,7,8" , font = font.Font(size = 12))
    new_win_info_label.grid(row = 0 , column = 0 , columnspan = 2 , padx = 30 , pady = 10)
    new_win_process_id_label = Label(new_win , text = "Process ids " , font = font.Font(size = 13))
    # global new_win_process_id_entry
    # new_win_process_id_entry = Entry(new_win , width = 50 ,font = font.Font(size = 12))
    # new_win_process_id_label.grid(row = 1 , column = 0)
    # new_win_process_id_entry.grid(row = 1 , column = 1)
    
    global new_win_arrival_time_entry
    new_win_arrival_time_label = Label(new_win ,bg = "#FFF9A6", text = "Arrival time " , font = font.Font(size = 13))
    new_win_arrival_time_entry = Entry(new_win, width = 50,font = font.Font(size = 12))
    new_win_arrival_time_label.grid(row = 2 , column = 0)
    new_win_arrival_time_entry.grid(row = 2 , column = 1)
    
    global new_win_burst_time_entry
    new_win_burst_time_label = Label(new_win ,bg = "#FFF9A6", text = "Burst time " , font = font.Font(size = 13))
    new_win_burst_time_entry = Entry(new_win, width = 50,font = font.Font(size = 12))
    new_win_burst_time_label.grid(row = 3 , column = 0)
    new_win_burst_time_entry.grid(row = 3 , column = 1)
    
    if(type == "PP" or type == "PNP"):
        global new_win_priority_entry
        new_win_priority_label = Label(new_win ,bg = "#FFF9A6", text = "Priority " , font = font.Font(size = 13))
        new_win_priority_entry = Entry(new_win, width = 50,font = font.Font(size = 12))
        new_win_priority_label.grid(row = 4 , column = 0)
        new_win_priority_entry.grid(row = 4 , column = 1)
        submit_button = Button(new_win , text = "Next" ,font = font.Font(size = 12) ,  bg = "#FF5733" , fg = "white", command = lambda:perform(type , new_win))
        submit_button.grid(row = 5 , column = 0 , columnspan = 2 , pady = 10)
    
    elif(type == "RR"):
        global new_win_time_quantum_entry
        new_win_time_quantum_label = Label(new_win ,bg = "#FFF9A6", text = "Time Quantum " , font = font.Font(size = 13))
        new_win_time_quantum_entry = Entry(new_win, width = 50,font = font.Font(size = 12))
        new_win_time_quantum_label.grid(row = 4 , column = 0)
        new_win_time_quantum_entry.grid(row = 4 , column = 1)
        submit_button = Button(new_win , text = "Next" ,font = font.Font(size = 12) ,  bg = "#FF5733" , fg = "white", command = lambda:perform(type , new_win))
        submit_button.grid(row = 5 , column = 0 , columnspan = 2 , pady = 10)
    
    else:
        submit_button = Button(new_win , text = "Next" ,font = font.Font(size = 12) ,  bg = "#FF5733" , fg = "white", command = lambda:perform(type , new_win))
        submit_button.grid(row = 4 , column = 0 , columnspan = 2 , pady = 10)
    
    
    
def set_name():
    global name 
    name = name_entry.get()
    name_label.destroy()
    name_entry.destroy()
    name_submit.destroy()
    new_name_label = Label(root , text = "Welcome "+name , font = font.Font(size = 18) ,  bg = '#FFF9A6')
    new_name_label.grid(row = 0 , column = 0 , padx = 20 , pady = 10)
    info_label = Label(root , text = "What do you want to choose?" , font = font.Font(size = 13) ,  bg = '#FFF9A6')
    info_label.grid(row = 1 , column = 0 , padx = 30 , pady = 10)
    fcfs_button = Button(root , text = "FCFS" , command =lambda:set_lists_new("FCFS") , font = font.Font(size = 12) ,  bg = "#FF5733" , fg = "white")
    fcfs_button.grid(row = 2 , column = 0 , pady = 10)
    fcfs_button = Button(root , text = "SJF(non-preemptive)" , command =lambda:set_lists_new("SJFNP") , font = font.Font(size = 12) ,  bg = "#FF5733" , fg = "white")
    fcfs_button.grid(row = 3 , column = 0 , pady = 10)
    fcfs_button = Button(root , text = "SJF(preemptive)" , command =lambda:set_lists_new("SJFP") , font = font.Font(size = 12) , bg = "#FF5733" , fg = "white")
    fcfs_button.grid(row = 4 , column = 0 , pady = 10)
    fcfs_button = Button(root , text = "Priority(non-preemptive)" , command =lambda:set_lists_new("PNP") , font = font.Font(size = 12) ,  bg = "#FF5733" , fg = "white")
    fcfs_button.grid(row = 5 , column = 0 , pady = 10)
    fcfs_button = Button(root , text = "Priority(preemptive)" , command =lambda:set_lists_new("PP") , font = font.Font(size = 12) ,  bg = "#FF5733" , fg = "white")
    fcfs_button.grid(row = 6 , column = 0 , pady = 10)
    fcfs_button = Button(root , text = "Round Robin" , command =lambda:set_lists_new("RR") , font = font.Font(size = 12) ,  bg = "#FF5733" , fg = "white")
    fcfs_button.grid(row = 7 , column = 0 , pady = 10)
    
if __name__ == "__main__":
    root = Tk()
    root.title("Simulator")
    root.configure(background = '#FFF9A6')
    name_label = Label(root , text = "Please enter your name " , font = font.Font(size = 12) , bg = '#FFF9A6')
    name_entry = Entry(root , width = 30 , font = font.Font(size = 11))
    name_submit = Button(root , text = "NEXT" , command = set_name , font = font.Font(size = 12) , bg = "#FF5733" , fg = "white")
    
    name_label.grid(row = 0 , column = 0 , pady = 20)
    name_entry.grid(row = 0 , column = 1 , pady = 20)
    name_submit.grid(row = 1 , column = 0 , columnspan = 2 , pady = 10)
    
 
    root.mainloop()