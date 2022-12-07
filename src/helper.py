"""
helper.py
This module contains help functions to create a span
with other functions in event_to_span.py 
"""


def convert_to_ns(seconds):
 """
  Convert gerrit's timestamp to nano seconds
  :param seconds: int, timestamp from gerrit with seconds 
  :return int, timestamp with nano secounds 
 """
 ns= int("%s000000000" % seconds)
 return ns 


def create_trace_id(event):
  """
  Hash change id to use as own trace id on id generator.  
  :param event: dict from stream events
  :return int 
  """
  import hashlib
  m=hashlib.md5() 
  bstring=event['change']['id'].encode('ASCII')
  m.update(bstring)
  trace_id=int(m.hexdigest(),16)
  
  return trace_id


def md5_span_id(seed):
 """
 Hash string to use as own span id on id generator. 
 :praram seed: string, usually gerrit ref+ event type + additional info
 :return int 
 """
 import hashlib 
 m=hashlib.md5()
 bstring=seed.encode('ASCII')
 m.update(bstring)
 span_id=(int(m.hexdigest(),16)) % 2**64
  
 return span_id


def create_span_id(event,event_type):
  """
  Create a string to hash for an unique span id.
  Each event type has different element to take. 
  :pram event:dict
  :param event_type:string
  :reutrn span_id: int 
  """
  ref=event['patchSet']['ref']
  patch_nr=event['patchSet']['number']
  
  if event_type == "change-created":
   # refs/changes/12/14612/
     if patch_nr < 10:
       span_id=md5_span_id(ref[:-1])
     elif patch_nr >=10:  
        span_id=md5_span_id(ref[:-2])

  elif event_type=="patchset-created" or event_type=="change-merged" or event_type == "change-abandoned":
  #Ex: refs/changes/12/14612/10/patchset-created or change-merged or change-abandoned 
    span_id=md5_span_id(f"{ref}/{event_type}")
       
  elif event_type=="comment-added": 
  #Ex: refs/changes/12/14612/10/comment-added/rclement/1668262246
    span_id=md5_span_id(f"{ref}/{event_type}/{event['author']['username']}/{event['eventCreatedOn']}") 
     
  elif event_type== "code-review":
   #Ex: refs/changes/12/14612/10/code-review/rclement
    span_id=md5_span_id(f"{ref}/{event_type}/{event['author']['username']}")
  
  return span_id
  
def parent_span_id(event):
  """
  Regenerate span id for a parent span.
  Depends on event type, the parent will be different.
  Patchset spans: parent = current change 
  Code review/merged/abandoned spans: parent = current patchset 
  :param event: dict
  :return parent_span_id: int
  """
  event_type=event['type']
  ref=event['patchSet']['ref']
  #When change span is the parent 
  if event_type == "patchset-created":
    patch_nr=event['patchSet']['number']
    if patch_nr < 10:
      return md5_span_id(ref[:-1])#"refs/changes/37/14737/"
    elif patch_nr >=10:  
      return md5_span_id(ref[:-2])#"refs/changes/37/14737/"
  #When patch set is the parent 
  elif event_type == "comment-added" or event_type == "change-merged" or event_type == "change-abandoned":
      return md5_span_id(f"{ref}/patchset-created")
      #"refs/changes/37/14737/1/patchset-created"

def set_generate_ids(generator,t_id,s_id): #pragma:no cover 
  """
  Set trace id and span id to create a span with 
  using these ids.
  :param generator custom_id_generator
  :param t_id:int, hashed change id 
  :param s_id:int, hased for span id  
  """
  from tracer import custom_id_generator 
  t_type=type(t_id)  
  s_type=type(s_id) 
  
  if t_type is int and s_type is int and generator is custom_id_generator:  
    try:
        generator.set_generate_trace_id(t_id)
        generator.set_generate_span_id(s_id)
    except: 
      print("trace/span ids should be int!")  
    

def create_context(traceid,spanid):
  """
   Convert trace/span id with tempo format
   to Opentelemetry SpanContext format.
   :param traceid:int
   :param spanid:int
   :return ctx:SpanContext(), span context just created
  """ 
  from opentelemetry.trace import SpanContext,TraceFlags

  t=hex(traceid)
  s=hex(spanid)
  ctx= SpanContext(trace_id=int(t,16),span_id=int(s,16),is_remote=True,
    trace_flags=TraceFlags(0x01)) 

  return ctx 


