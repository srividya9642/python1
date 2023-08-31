#write into csv.file
import csv
f=open('emp.csv','w')
cp=csv.writer(f)
for i in range(10):
    eid=input("enter employee id:")
    ename=input("enter employee name:")
    esal=input("enter employee salary:")

    
f=open('emp.json'())
print(f.name)
print(f.mode)
print(f.writable())
print(f.readable())
print(f.closed)