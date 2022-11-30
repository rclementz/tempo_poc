

# def get_change_name(event):
#   """
#   Get name of the change retrived 
#   through gerrit stream events. 
#   """
#   event_type=event['type']
#   # get patch number 
#   patch_number=event['patchSet']['number']
#   name=event_type.replace('-', f" {patch_number} ")
#   return name 

def convert_to_ns(seconds):
 """
  Convert gerrit's timestamp to nano seconds
 """
 ns= int("%s000000000" % seconds)
 return ns 


def create_trace_id(event):
  """
   Hash change id to use as own trace id on id generator.  
   @param event: dict from stream events
   return int 
  """
  import hashlib
  m=hashlib.md5() 
  bstring=event['change']['id'].encode('ASCII')
  # bstring=event['change']['id'].encode()
  # m.update(b"{event['change']['id']}")
  m.update(bstring)
  trace_id=int(m.hexdigest(),16)
  
  return trace_id


def md5_span_id(seed):
 """
   Hash string to use as own span id on id generator. 
   @praram seed 
   return int 
 """
 import hashlib 
 m=hashlib.md5()# No need to use this 
#  m.update(string.encode())
#  m.update(b'{string}')
 bstring=seed.encode('ASCII')
 m.update(bstring)
 span_id=(int(m.hexdigest(),16)) % 2**64
  
 return span_id


def create_span_id(event,event_type):
  """
  Create a string to hash for an unique span id.
  Each event type has different element to take. 
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
   Patchset spans : 
    parent = current change 
   Code review/merged/abandoned spans :
    parent = current patchset 
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
  @param generator custom_id_generator
  @param t_id int,hashed change id 
  @param s_id int, hased for span id  
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
   @param traceid int
   @param spanid  int
  """ 
  from opentelemetry.trace import SpanContext,TraceFlags

  t=hex(traceid)
  s=hex(spanid)
  ctx= SpanContext(trace_id=int(t,16),span_id=int(s,16),is_remote=True,
    trace_flags=TraceFlags(0x01)) 

  return ctx 


# These functions below will not be used for the real case 
# def trace_id(name):
#   """
#   Temporary trace id maker while creating span manually 
#   """
#   import hashlib
#   m=hashlib.md5()
#   m.update(name.encode())
#   trace_id=int(m.hexdigest(),16)
  
#   return trace_id

# def span_id(name):
#   """
#   Temporary span id maker while creating span manually 
#   """
#   import hashlib 
#   m=hashlib.md5()
#   m.update(name.encode())
#   span_id=(int(m.hexdigest(),16)) % 2**64

#   return span_id

