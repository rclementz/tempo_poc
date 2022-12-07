# TEMPO POC 
![The sample visual](https://user-images.githubusercontent.com/114480431/205316264-90e1306d-a086-4ae3-8a2b-5bd9f7698208.png)
### OVERVIEW 
Tempo poc is poc for code review process visualisation with [Grafana Tempo](https://grafana.com/docs/tempo/latest/).

This programme traces code review processes on gerrit and creates **spans** by using [opentelemetry](https://opentelemetry.io/docs/instrumentation/python/). 
All spans are created based on the data which is retrieved from [gerrit stream events*](https://gerrit.volvocars.biz/Documentation/cmd-stream-events.html), then sent to Grafana Tempo and visualised as traces. 
Even if spans are created separately, all spans for the same commit will be combined in the same trace. You can always make a query and look up a particular trace on Grafana Tempo with trace id (Ex: c7a3d286766cd5e8e02ca13dedf754a0)

***gerrit stream-events**: 
    provides JSON data of events/activity currently occuring on the gerrit server via SSH connection. Events can be categorised into 17 different types but this poc filters and use only the ones from [patchset created](https://gerrit.volvocars.biz/Documentation/cmd-stream-events.html#_patchset_created), [comment added](https://gerrit.volvocars.biz/Documentation/cmd-stream-events.html#_comment_added), [change merged](https://gerrit.volvocars.biz/Documentation/cmd-stream-events.html#_change_merged) and [change abandoned](https://gerrit.volvocars.biz/Documentation/cmd-stream-events.html#_change_abandoned). You can find sample json data in `/src/sample.py`. 

**Still not clear what are trace and span?
    If you need more clarification, please check [here](https://grafana.com/docs/tempo/latest/getting-started/traces/)

### HOW TO RUN 
```shell
 $ docker-compose up --build -d 
```
After running this command, please wait for a while since it takes a while to retrieve data and create spans if some activities are found in stream events. 
Then you can run below and see logs 
```shell
$ docker-compose logs 
```
![]


### Further improvement
- Trigger
    All data from gerrit stream events are retrieved manually, only when main.py is run. 
    To automate this, some triggers need to be set and run the script automatically. 
- Different Tool
    This poc is only covering the process on gerrit, however, it is also addaptable to be used with other tools like GitHub, Gitlab and etc.. 
