"""
custom_id.py
IdGenerator is abstract class in opentelemetry.sdk.trace.id_generator.
From there, create CustomIdGenerator which allow us to 
genrate our own trace id and span id. 

Original idea comes from here:
https://github.com/open-telemetry/opentelemetry-python/issues/2366
However, codes are modified to make them functional. 
"""


from opentelemetry.sdk.trace.id_generator import IdGenerator

class CustomIdGenerator(IdGenerator):
  
    def __init__(self):
        super().__init__()
        self.custom_trace_id = None
        self.custom_span_id = None
        
    #Trace_id: A unique 16-byte array to identify the trace that a span is associated with
    #Ex: 7bba9f33312b3dbb8b2c2c62bb7abe2d
    def set_generate_trace_id(self,t_id):
      """
       Set custome trace id which will be 
       used in func generate_trace_id.
       :param t_cd:int
      """
      self.custom_trace_id = t_id
      
    def generate_trace_id(self)->int:  
       trace_id=self.custom_trace_id
       return trace_id
    
    # Span_id: Hex-encoded 8-byte array to identify the current span
    #Ex:086e83747d0e381e
    def set_generate_span_id(self,s_id):
      """
       Set custome span id which will be 
       used in func generate_trace_id 
       :param s_id:int 
      """
      self.custom_span_id = s_id
     
    def generate_span_id(self)->int:
       span_id=self.custom_span_id
       return span_id 

