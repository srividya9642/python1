#dump()
#write python object to json file
import json
f=open('emp.json','w')
emp_dict={'id':101,
          'name':'rahul',
          'avail':True,
          'loc':None
          }
json.dump(emp_dict,f)
          
f.close()       