'''
@ Author: Solayman Hossain Emon
  ID: 16.01.04.091
  Aust CSE 37th Batch
  
'''

from tabulate import tabulate

x = int(input('How many jobs:::'))

jobs = []
temp_Lst = []
lst = []
z = x

sequence = [None] * z
M1_IN = [None] * z
M1_OUT = [None] * z
M2_IN = [None] * z
M2_OUT = [None] * z

lst_elmnt = -1
frst_elmnt = 0

for y in range(x):
    print('Enter the job name:::')
    element = [input(), int(input('Enter the time for Machine Center1 ::')), int(input('Enter the time for Machine Center2 ::'))] 
    jobs.append(element)

new_list = jobs[:]

print('\n')
print(tabulate(jobs, headers = ['Job', 'Machine Center1', 'Machine Center2']))

k = 1

while k <= z:

    for x in range(len(jobs)):
        list1 = jobs[x][1:]
        temp_Lst.append(list1)

    # find the min list  
    b = [min(p) for p in temp_Lst] 
  
    # find the min element from the list
    min_element = min(b)
    indx = b.index(min_element)

    ck = 0
    cck = 0
    for i in range(len(jobs)):  
        j = 1
        while j <= 2: 
            if(jobs[i][j] == min_element):
                ck = i
                ckk = j
                break
            j = j + 1 
    
    # find the minimum value coming from which machine
    if(ckk == 2):
        sequence[lst_elmnt] = jobs[ck][0]
        lst_elmnt = lst_elmnt - 1
        
    elif(ckk == 1):
        sequence[frst_elmnt] = jobs[ck][0]
        frst_elmnt = frst_elmnt + 1
        
    del jobs[ck]
    del temp_Lst[:]
    k = k + 1            
  
for i in range(len(sequence)):
    for j in range(len(sequence)):
        if(sequence[i] == new_list[j][0]):
            lst.append(new_list[j])
               
print('\n')
print('The Resultant Sequence is :::')
print('\n')
print(sequence) 
print('\n')
print(tabulate(lst, headers = ['Job', 'Machine Center1', 'Machine Center2']))

sm = 0
M1_IN[sm] = 0
k = 1

for i in range(len(lst)):  
    
    if i != 0:
        M1_IN[i] = sm 
    sm = sm + lst[i][1]    
    M1_OUT[i] = sm

smm = M1_OUT[0]
M2_IN[0] = smm

for i in range(len(lst)):  
    
    if i != 0:
        M2_IN[i] = smm 
        if(M2_IN[i] < M1_OUT[i]):
            while(M2_IN[i] != M1_OUT[i]):
                M2_IN[i] = M2_IN[i] + 1
                 
    smm = smm + lst[i][2]
    M2_OUT[i] = lst[i][2] + M2_IN[i]
    
fn = []

for i in range(len(sequence)):
     ls = [sequence[i], M1_IN[i], M1_OUT[i], M2_IN[i], M2_OUT[i]]   
     fn.append(ls)
     
idle = 0
n = -1
for i in range(len(M2_IN) - 1):
    idle = idle + ( M2_IN[n] - M2_OUT[n-1])
    n = n - 1
    
idle = idle + M2_IN[0]  
  
print('\n')
print(tabulate(fn, headers = ['Job_Seq', 'M1_IN', 'M1_OUT','M2_IN', 'M2_OUT']))
print('\n')
print('Total Flow Time(Minimized) :::', M2_OUT[-1])
print('Machine1 Idle Time :::', M2_OUT[-1] - M1_OUT[-1])
print('Machine2 Idle Time :::', idle)

