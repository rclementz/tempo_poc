"""
trace_id_search.py
This provides the trace id search function.
User can input gerrit change id and it is 
converted to trace id for Grafana Tempo. 
"""

import hashlib

print("****TRACE ID SEARCHER****\nPlease input change id:")

change_id=input()
m=hashlib.md5() 
bstring=change_id.encode('ASCII')
m.update(bstring)
trace_id=m.hexdigest()

print(f"""
The trace id for your change is:

{trace_id}

Copy the id and make a query on Tempo to check the trace.

************************
""")  
   

 
