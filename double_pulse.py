import sys   

file = 'data.csv'
data = 'data_out.csv'
range1=range(100,200)
range2=range(300,500)
    
i=0
with open(file,'r') as file_to_read,open(data, 'w') as file_to_write:
    while True:
        lines = file_to_read.readline()
        if not lines:
            break
        if i==0:
            file_to_write.writelines("TIME,ARB\n")
            i=1
            continue
        i=i+1
        lines=lines.rstrip("\n")
        #print (lines)
        if i in range1 or i in range2:
            file_to_write.writelines(lines+" 1\n")
        else:
            file_to_write.writelines(lines+" 0\n")
print ("finish")
        
            
