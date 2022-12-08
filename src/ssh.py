"""
ssh.py 
This module handles SSH client to access gerrit to get stream-events 
and gerrit query. Event type is specified as a parameter and events 
will be saved and returned as list. 

***updated: 05 dec 2022
    No need to provide config anymore since host is in known_hosts file. 
**updated: 29 nov 2022
    path to key file name will be found by using getcwd()
*updated: 18 oct 2022 
    Func name: events_getter -> events_streamer 
    Using list instead of queue to save events 
     because queue objects disappear from the queue once retrived.
    (can't return and use them in a different file) 
"""

import paramiko
import os 
import json 

def events_streamer(event_type): 
    """
    events_streamer connects gerrit via SSH
    and stream ongoing code review events. 
    :pram event_type: string, event type on gerrit 
    :return a list of each event retrieved 

    Event types used in this poc are "patchset-created",
    "comment-added","change-merged","change-abandoned"
    """
    client=paramiko.SSHClient()    
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.load_system_host_keys()
    path=os.getcwd()
    path=path.replace("tempo_poc","")
    
    client.connect( 'gerrit-ssh.volvocars.biz',
                    username='csei-jenkins',
                    port=22,
                    key_filename=f'{path}.ssh/id_rsa' 
                    )             
    stdin, stdout, stderr = client.exec_command(f"gerrit stream-events -s {event_type}")  
    stdin.close() 
    
    events=[]
    for line in stdout:
        print(f"Retrieving gerrit stream events (type: {event_type}) :\n")
        event=json.loads(line)
        events.append(event)
        client.close()
        print('Retrieved and creating span(s)')
    
    if len(events) == 0:
        print(f"** Nothing retrieved from {event_type}")
        
    return events  # Stream events saved in a list 


def gerrit_query(change_id):
    """
    gerrit_query makes a query on gerrit 
    and retrieve the patch set infomation 
    in the particular change.
    :param change_id: string, change id in gerrit  
    :return a list of patchsets in the change
    """
    client=paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
    client.load_system_host_keys()
    path=os.getcwd()
    path=path.replace("tempo_poc","")

    client.connect( 'gerrit-ssh.volvocars.biz',
                    username='csei-jenkins',
                    port=22,
                    key_filename=f'{path}.ssh/id_rsa' 
                    )             
    stdin, stdout, stderr = client.exec_command(f'gerrit query --format=JSON --patch-sets change:{change_id}')
    stdin.close()  

    patchsets=[]
    for line in stdout:
        patchset=json.loads(line)
        patchsets.append(patchset)
   
    print(f"Retriving patch set info on gerrit query for change id: {change_id}")
    client.close()
    print('Completed and the connection closed.')
    
    patchsets=patchsets[0].get('patchSets')
     
    return patchsets


