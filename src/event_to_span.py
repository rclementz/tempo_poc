"""
event_to_span.py 
This module contains functions to create different type of spans
with getting necessary infomation like timestamps, name and attributes
from an event dictionary. 

*updated 12 dec 2022:
 temporary patchset spans's end time now sets as current time 
 instead of using its start time. 
"""


from helper import set_generate_ids,create_trace_id,convert_to_ns,create_span_id,create_context,parent_span_id,md5_span_id
from tracer import set_tracer, custom_id_generator,set_tracer
from opentelemetry import trace 

def get_patchset_st(change_id,patch_nr):
    """
    Retrieves timestamp when a particular patch set 
    was created in a change via gerrit query. 
    :param change_id: string
    :param patch_nr: int
    :return int, start time of patch set 
    """
    from ssh import gerrit_query
    patchsets=gerrit_query(change_id)
    start_time=patchsets[(patch_nr-2)]['createdOn']
    return convert_to_ns(start_time)

def create_change_span(event):
    """
    Create a change span which shows the whole process 
    since a commit made until the change merged. 
    :praram event:dict 
    :return SpanContext(), context of this span 
    """
    project=f"{event['change']['number']}({event['change']['project']})"
    tracer=set_tracer(project,event['change']['number'])
    set_generate_ids(custom_id_generator,create_trace_id(event),create_span_id(event,"change-created"))
    with tracer.start_span(project,start_time=convert_to_ns(event['change']['createdOn'])) as change:
        change.set_attribute("Ref",event['patchSet']['ref'])
        change.set_attribute("Owner",f"{event['change']['owner']['name']} ({event['change']['owner']['username']})")
        change.set_attribute("Subject",event['change']['subject'])
        change.set_attribute("URL",event['change']['url'])
        change.end()
        ctx=change.get_span_context()
     

        return ctx


def complete_change_span(event):
    """
    Complete the change span by sending 
    the actual end time for the span. 
    :param event:dict
    :return SpanContext(), context of this span 
    """
    time=convert_to_ns(event["eventCreatedOn"])
    trace_id=create_trace_id(event)
    project=f"{event['change']['number']}({event['change']['project']})" 

    tracer=set_tracer(project,event['change']['number'])
    set_generate_ids(custom_id_generator,trace_id,create_span_id(event,"change-created"))    
    with tracer.start_span(project,start_time=convert_to_ns(event['change']['createdOn'])) as cc:
        cc.set_attribute("Ref",event['patchSet']['ref'])
        cc.set_attribute("Owner",f"{event['change']['owner']['name']} ({event['change']['owner']['username']})")
        cc.set_attribute("Subject",event['change']['subject'])
        cc.set_attribute("URL",event['change']['url'])
        ctx=cc.get_span_context()
        cc.end(end_time=time)

        return ctx
            
def create_patch_span(event):
    """
    Create a short span when patch set was created. 
    :param event:dict
    :return SpanContext(), context of this span 
    """
    time=convert_to_ns(event["eventCreatedOn"])
    trace_id=create_trace_id(event)
    parent=create_context(trace_id,create_span_id(event,"change-created"))

    tracer=set_tracer(f"pathset {event['patchSet']['number']}",event['change']['number'])    
    
    set_generate_ids(custom_id_generator,trace_id,create_span_id(event,event['type']))
    with tracer.start_span(f"pathset {event['patchSet']['number']}",start_time=time,links=[trace.Link(parent)]) as ps:
        ps.set_attribute("Project",f"{event['change']['project']}") 
        ps.set_attribute("Subject",f"{event['change']['subject']}") 
        ps.set_attribute("Uploader",f"{event['uploader']['name']} ({event['uploader']['username']})")
        ps.set_attribute("URL",f"{event['change']['url']}")
        ps.end()
        ctx=ps.get_span_context()
       
    
    return ctx

def complete_patch_span(event): 
    """
    Create complete a current patchset span 
    when the next patch set was created. 
    :param event:dict
    :return SpanContext(), context of this span 
    """
    patch_nr=event['patchSet']['number']
    st=get_patchset_st(event['change']['id'],patch_nr) 
    et=convert_to_ns(event["eventCreatedOn"])
    ref=event['patchSet']['ref']
    event_type=event['type']

    trace_id=create_trace_id(event)
    if patch_nr >= 10:
        span_id=md5_span_id(f"{ref[:-2]}{patch_nr-1}")
    else:
        span_id=md5_span_id(f"{ref[:-1]}{patch_nr-1}")       
    parent=create_context(trace_id,parent_span_id(event)) #parent=change span
    
    if patch_nr == 1: # This condition avoids creating patchset 0 
        patch_nr_to_complete = 1
    else:
        patch_nr_to_complete = patch_nr-1      
    
    #name and username belong to different categories depends on event type 
    if event_type=="patchset-created":
        person="Uploader"
        name=event['uploader']['name']
        username=event['uploader']['username']

    elif event_type=="change-merged":
        person="Submitter"
        name=event['submitter']['name']
        username=event['submitter']['username']

    elif event_type=="change-abandoned":
        person="Abandoner"
        name=event['abandoner']['name']
        username=event['abandoner']['username']

    tracer=set_tracer(f"pathset {patch_nr_to_complete}",event['change']['number'])    
    set_generate_ids(custom_id_generator,trace_id,span_id)
    with tracer.start_span(f"pathset {patch_nr_to_complete}",start_time=st,links=[trace.Link(parent)]) as ps:
        ps.set_attribute("Project",f"{event['change']['project']}") 
        ps.set_attribute("Subject",f"{event['change']['subject']}") 
        ps.set_attribute("URL",f"{event['change']['url']}") 
        ps.set_attribute(person,f"{name} ({username})")
        ctx=ps.get_span_context()
        ps.end(end_time=et)
    
    return ctx    


def create_code_review_span(event): 
    """
    Create a span to see whole code review process
    for a reviewer.
    Start time= when patchset created 
    End time= when the comment added
    :param event:dict
    :return SpanContext(), context of this span  
    """
    trace_id=create_trace_id(event)
    parent=create_context(trace_id,parent_span_id(event)) #parent=patch set span 
    author=f"{event['author']['name']}  ({event['author']['username']})"
    keys=event.keys()
    
    tracer=set_tracer(f"pathset {event['patchSet']['number']}",event['change']['number'])       
    set_generate_ids(custom_id_generator,trace_id,create_span_id(event,"code-review"))
    
    if "approvals" in keys: 
        with tracer.start_span(f"code review -{author} ",start_time=convert_to_ns(event['patchSet']['createdOn']),links=[trace.Link(parent)]) as cr:
            cr.set_attribute("Project",event['change']['project'])
            cr.set_attribute("Author",author)
            cr.set_attribute("Verified",f"{event['approvals'][0]['value']}")
            cr.set_attribute("Code Review",f"{event['approvals'][1]['value']}")
            cr.set_attribute("Comment",f"{event['comment']}")
            ctx=cr.get_span_context()
            cr.end(end_time=convert_to_ns(event["eventCreatedOn"]))
    else:     
        with tracer.start_span(f"code review -{author} ",start_time=convert_to_ns(event['patchSet']['createdOn']),links=[trace.Link(parent)]) as cr:
            cr.set_attribute("Project",event['change']['project'])
            cr.set_attribute("Author",author)
            cr.set_attribute("Comment",f"{event['comment']}")
            ctx=cr.get_span_context()
            cr.end(end_time=convert_to_ns(event["eventCreatedOn"]))

    return ctx

def create_comment_span(event,ctx):
    """
    Create a short span when a comment added
    :param event:dict
    :param ctx:SpanContext(), context of the parent span 
    :return SpanContext(), context of this span 
    """ 

    time=convert_to_ns(event["eventCreatedOn"])
    trace_id=create_trace_id(event)
    author=f"{event['author']['name']}  ({event['author']['username']})"
    comment=event['comment']

    tracer=set_tracer(f"pathset {event['patchSet']['number']}",event['change']['number'])       
    set_generate_ids(custom_id_generator,trace_id,create_span_id(event,event['type']))
    with tracer.start_span(comment,start_time=time,links=[trace.Link(ctx)]) as cr: #parent=code review span 
        cr.set_attribute("Project",event['change']['project'])
        cr.set_attribute("Author",author)
        cr.set_attribute("Verified",f"{event['approvals'][0]['value']}")
        cr.set_attribute("Code Review",f"{event['approvals'][1]['value']}")
        cr.set_attribute("Comment",comment)
        ctx=cr.get_span_context()
        cr.end(end_time=time)
    return ctx    
   

def create_merged_or_abandoned_span(event):#
    """
    Create a change merged or abandoned span. 
    Check event type and automatically decide which span to create. 
    :param event:dict
    :return SpanContext(), context of this span 
    """
    time=convert_to_ns(event["eventCreatedOn"])
    trace_id=create_trace_id(event)
    parent=create_context(trace_id,parent_span_id(event)) #parent=patch set span 
    event_type=event['type'] # "change-merged" or "change-abandoned"
    span_name=event_type.replace("c","C")
    span_name= span_name.replace("-", " ")

    if event_type=="change-merged":
        person="Submitter"
        name=event['submitter']['name']
        username=event['submitter']['username']

    elif event_type=="change-abandoned":
        person="Abandoner"
        name=event['abandoner']['name']
        username=event['abandoner']['username']

    tracer=set_tracer(f"pathset {event['patchSet']['number']}",event['change']['number'])       
    set_generate_ids(custom_id_generator,trace_id,create_span_id(event,event_type))
    #Short span for change merged 
    with tracer.start_span(span_name,start_time=time,links=[trace.Link(parent)]) as cm: 
        cm.set_attribute(person,f"{name} ({username})")
        ctx=cm.get_span_context()
        cm.end(end_time=time)                            
    return ctx

def complete_trace(event):
    """
    Sets up proper ends time for the latest patchset span
    and the change span so the trace can be completed.
    The definition of end is when the change is 
    either merged or abandoned.
    :param event:dict
    """
    merge_abandoned=create_merged_or_abandoned_span(event)
    patchset=complete_patch_span(event)
    change=complete_change_span(event)
    return f"Contexts:\nmerged/abandoned:{merge_abandoned}\npatchset:{patchset}\nchange:{change}"
       













