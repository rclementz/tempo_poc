"""
ssh.py 
This is SSH client to access gerrit to get stream-events. 
Event type is specified as a parameter and events will be saved 
and returned as list. 

updated: 29 nov 2022

updated: 18 oct 2022 
*Func name: events_getter -> events_streamer 
 Using list instead of queue to save events 
 because queue objects disappear from the queue once retrived.
 (can't return and use them in a different file) 
"""

import paramiko
import os 
import json 

def events_streamer(event_type): 
    client=paramiko.SSHClient()    
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.load_system_host_keys()
    path=os.getcwd()
    path=path.replace("tempo_poc","")

    config= paramiko.SSHConfig.from_file(open(f'{path}.ssh/config'))
    host= config.lookup('gerrit-ssh.volvocars.biz')

    client.connect( 'gerrit-ssh.volvocars.biz',
                    username='csei-jenkins',
                    port=22,
                    key_filename=f'{path}.ssh/csei-jenkins-private-key' 
                    )             
    stdin, stdout, stderr = client.exec_command(f"gerrit stream-events -s {event_type}")
    # stdin, stdout, stderr = client.exec_command("gerrit stream-events")
     
    stdin.close() # This is to get rid of "AttributeError: 'NoneType' object has no attribute 'time'"
    
    events=[]
 
    for line in stdout:
        print(f"Retrieving gerrit stream events (type: {event_type}) :\n")
        event=json.loads(line)
        events.append(event)
        print(event) # Delete this line on demo ??
        client.close()
        print('**Completed**')
    
    if len(events) == 0:
        print(f"** Nothing retrieved from {event_type} **")
        
    return events  # Stream events saved in a list  


def gerrit_query(change_id):
    client=paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
    client.load_system_host_keys()
    path=os.getcwd()
    path=path.replace("tempo_poc","")


    config= paramiko.SSHConfig.from_file(open(f'{path}.ssh/config'))
    host= config.lookup('gerrit-ssh.volvocars.biz')

    client.connect( 'gerrit-ssh.volvocars.biz',
                    username='csei-jenkins',
                    port=22,
                    key_filename=f'{path}.ssh/csei-jenkins-private-key' 
                    )             
    stdin, stdout, stderr = client.exec_command(f'gerrit query --format=JSON --patch-sets change:{change_id}')

    stdin.close() # This is to get rid of "AttributeError: 'NoneType' object has no attribute 'time'"
    
    patchsets=[]
    for line in stdout:
        patchset=json.loads(line)
        patchsets.append(patchset)
   
    print(f"Retriving patch set info on gerrit query for change id: {change_id}")
    client.close()
    print('Completed and the connection closed.')
    
    return patchsets



#Here is the old ver. with queue just in case.. 
# import queue 
# queue=queue.Queue()

# def events_getter(event_type): 
#     client=paramiko.SSHClient()
#     client.load_system_host_keys()
#     # Which policy we actually should choose? : Autoadd, RejectPolicy, WarningPolicy 
#     #client.set_missing_host_key_policy()

#     config= paramiko.SSHConfig.from_file(open('/home/rclement/.ssh/config'))
#     host= config.lookup('gerrit-ssh.volvocars.biz')

#     client.connect('gerrit-ssh.volvocars.biz',
#                     username='csei-jenkins',
#                     port=22,
#                     key_filename='/home/rclement/.ssh/csei-jenkins-private-key' 
#                     )             
#     stdin, stdout, stderr = client.exec_command(f"gerrit stream-events -s {event_type}")
#     # stdin, stdout, stderr = client.exec_command("gerrit stream-events")
     
#     stdin.close() # This is to get rid of "AttributeError: 'NoneType' object has no attribute 'time'"
    
#     for line in stdout: 
#         queue.put(json.loads(line))
    
#     # events=queue.get()
#     events=queue
#     print(events)
            
#     print(f"Start retriving stream events {event_type} :\n")
#     print ('****adding to the queue*****')
#     client.close()
#     print('\nCompleted and the connection closed.')
    
#     return events  # Stream events saved as queue for now 
