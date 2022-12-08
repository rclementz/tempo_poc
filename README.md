# TEMPO POC 
![The sample visual](https://user-images.githubusercontent.com/114480431/205316264-90e1306d-a086-4ae3-8a2b-5bd9f7698208.png)
## OVERVIEW 
Tempo poc is poc for code review process visualisation with [Grafana Tempo](https://grafana.com/docs/tempo/latest/).

This programme traces code review processes on gerrit and creates **spans** by using [opentelemetry](https://opentelemetry.io/docs/instrumentation/python/). 

All spans are created based on the data which is retrieved from [gerrit stream events*](https://gerrit.volvocars.biz/Documentation/cmd-stream-events.html), then sent to Grafana Tempo and visualised as traces. 
Even if spans are created separately, all spans for the same commit will be combined in the same trace. You can always make a query and look up a particular trace on Grafana Tempo with trace id (Ex: `c7a3d286766cd5e8e02ca13dedf754a0`)

>**gerrit stream-events**: 
>
>provides JSON data of events/activity currently occuring on the gerrit server via SSH connection. Events can be categorised into 17 different types but this poc >filters and use only the ones from [patchset created](https://gerrit.volvocars.biz/Documentation/cmd-stream-events.html#_patchset_created), [comment added](https://gerrit.volvocars.biz/Documentation/cmd-stream-events.html#_comment_added), [change merged](https://gerrit.volvocars.biz/Documentation/cmd-stream-events.html#_change_merged) and [change abandoned](https://gerrit.volvocars.biz/Documentation/cmd-stream-events.html#_change_abandoned). You can always find sample >json data in `/src/sample.py`. 

## SPAN AND TRACE 
![span_trace_explanation](https://user-images.githubusercontent.com/114480431/206401083-ceab2702-4bdb-4015-933d-512b0954be25.png)

[Here](https://grafana.com/docs/tempo/latest/getting-started/traces/) is the definition of span and trace from Grafana Tempo but we can expalin these for this poc as below. 

>**Span**: shows the duration of an individual work/action. 
For example, a patchset 1 span starts when it is created and ends when the next patchset is created.

>**Trace**: the collection of spans which belong to the same code review process (the same change) 


## HOW TO RUN 
```shell
 $ docker-compose up --build -d 
```
After running this command, please wait for a while since it takes a while to retrieve data and create spans if some activities are found in stream events. 
Then you can run below and see logs 
```shell
$ docker-compose logs 
```
## HOW TO SEE LOGS 
### Spans are created
If spans are created, these lines will be shown in logs. 
```
Retrieved and creating span(s)
Calling end() on an ended span.
Calling end() on an ended span.
```

Under this line, there's also the detail of created span with JSON format:
```
{
    "name":"12345(repo/name)"
    "content":{
        "trace_id": "0x1ab2c3edf45ff67d8e9c012b34567ab8",
        "span_id": "0x123a45b67890c12d",
        "trace_state":"[]"
     },
     "kind":"SpanKind.INNTERNAL",
     "parent_id":null,
     "start_time": "2022-12-07T00:00:01.000000Z",
     "end_time": "2022-12-07T00:01:01.000000Z",
     "status": {
        "status_code":"UNSET"
      },
      "attributes":{
        "Ref":"refs/changes/88/12345/1",
        "Owner":"Owner Name (ownerusername)",
        "Subject": "Subject for the commit",
        "URL": "https://gerrit.volvocars.biz/c/xxxxx/yyyy"
      },
      "events":[],
      "links":[
        {
            "context":{
                "trace_id": "0x1ab2c3edf45fg67h8i9j012k34567lm8",
                "span_id": "0x9ab87c65d43e21f09a8",
                "trace_state":"[]"
                },
                "attributes":{}
             }
      ],
      "resource": {
        "attributes": {
            "attributes":{
                "service.name": 12345(repo/name)
                },
                "schema_url": ""
                }
       }
}             
```
>***attributes**: usually contains reference of the change(**ref**) and the name of person who commited (this can be **owner**,**uploader**,**submitter** or >**author**)and other elements differ depends on the type of spans(**change**,**patchset**,**comment**,**code review**)
       
>***links**: if the span is related to another span as parent and child spans, parent span's context(trace id and span id) will be shown here. 

### Nothing retrieved     
These messages are shown when nothing available on gerrit stream events.  
```
**Nothing retrieved from patchset-created
**Nothing retrieved from comment-added
**Nothing retrieved from change-merged
**Nothing retrieved from change-abandoned
```

## FIND YOUR TRACE 
Trace id is generated based on gerrit Change id. 
If you'd like to check a trace of your change, get your trace id and make a query on Grafana Tempo. 
### Trace id search
```
$python3 trace_id_search.py 
```
Run `trace_id_search.py`, input your change id and then it gives you the trace id. 

### Tempo Query 
![tempo_query](https://user-images.githubusercontent.com/114480431/206408849-48651444-5194-45ca-931a-7d2d715a96c1.png)
Once you get the trace id, only thing to do is making a query. 
Enjoy tracing! 


    
## Further improvements
These are issues/idea to develop this poc further.
- **Adapting irregular flow**:
Since gerrit stream events is not covering patchset deleted, we can't follow that activity even when it happens. Deleted patchset stays on the trace. 
- **Organising dashboard**
This poc is covering all gerrit activities under CSEI and create spans and traces of everything happening. That makes a bit difficult for you to find a particular trace without using tempo query. It'd be great if we can set up dashboards for different categories(ex:each change or each team etc)to access and see traces much more easily.   

