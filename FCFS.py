import matplotlib.pyplot as plt

def FCFS(processes , burst_time , arrival_time):
    n = len(processes)
    completion_time = []
    curr_time = 0
    for i in range(n):
        #Checking whether the process has yet arrived or not
        #If not arrived , then increasing the current time to make the process arrive
        if(curr_time < arrival_time[i]):
            curr_time = arrival_time[i] 
        #now calculating the completion time
        curr_time = curr_time + burst_time[i]
        completion_time.append(curr_time)
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
    #process Ids
    processes = [1 , 2 , 3 , 4]
    n = len(processes)
    
    #burst time
    burst_time = [5 , 3 , 8 , 6]
    
    #arrival time
    arrival_time = [0 , 1 , 2 , 3]
    
    #calculating completion time
    completion_time = FCFS(processes , burst_time , arrival_time)
    
    #calculating turnaround time
    turnaround_time = cal_turnaround_time(arrival_time , completion_time)

    #calculating waiting time
    waiting_time = cal_waiting_time(turnaround_time , burst_time)
    
    #calculating average waiting time
    avg_waiting_time = cal_avg_waiting_tinme(waiting_time)
    
    print(completion_time , turnaround_time , waiting_time , avg_waiting_time)
    
    plot_completion_time(processes, completion_time)