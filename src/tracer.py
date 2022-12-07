"""
tracer.py 
This modules has a function to set tracer 
to create spans and trace with opentelemetry. 
Grafana tempo is configured as endpoint and 
all created spans are sent there. 
"""
from custom_id import CustomIdGenerator
custom_id_generator=CustomIdGenerator()

def set_tracer(service_name,tracer_name):
    """
    Sets up a tracer to create spans/trace.
    Each service should have an individual tracer
    so this will be set everytime span is created.

    :pram service_name: string, Usually project name 
    :param tracer_name: string, a name to make each tracer unique 
    """
    from base64 import b64encode

    import os
    import sys
    from opentelemetry import trace
    from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
    from opentelemetry.sdk.resources import Resource
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import  BatchSpanProcessor,ConsoleSpanExporter 
   

    resource= Resource(attributes={
        "service.name" : f"{service_name}"
    })

    another_provider=TracerProvider(resource=resource,id_generator=custom_id_generator)
    # get token from env
    token = os.getenv('TEMPO_TOKEN') or sys.exit("Please set the TEMPO_TOKEN environment variable")
    # base64 encode username : token bytes
    userpass = b64encode(b"282303:" + token.encode("ascii"))
    # set headers
    headers = {
        b'authorization': b'Basic ' + userpass
    }
    # create OTLPSpanExporter
    otlp_exporter = OTLPSpanExporter(
        endpoint="https://tempo-eu-west-0.grafana.net",
        headers=headers
    )
  
    span_processor = BatchSpanProcessor(otlp_exporter)
    # Trace set up 
    another_provider.add_span_processor(span_processor)
    another_provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))
    tracer_name = trace.get_tracer(__name__,tracer_provider=another_provider) 

    return tracer_name





