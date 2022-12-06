# TEMPO POC 
### OVERVIEW 
Tempo poc is poc for code review process visualisation with [Grafana Tempo](https://grafana.com/docs/tempo/latest/).
This programme traces code review processes on gerrit and creates spans by using [opentelemetry](https://opentelemetry.io/docs/instrumentation/python/). All spans created are sent to Grafana Tempo and visualised as traces. Even if spans are created separately, all spans for the same commit will be combined in the same trace. 
You can always make a query and look up a particular trace on Grafana Tempo with trace id (Ex: " c7a3d286766cd5e8e02ca13dedf754a0")


** If you need more clarification of what trace and span are, please check [here](https://grafana.com/docs/tempo/latest/getting-started/traces/)

##### This is the visual sample how it looks when all process get visualised 
![The sample visual](https://user-images.githubusercontent.com/114480431/205316264-90e1306d-a086-4ae3-8a2b-5bd9f7698208.png)

### HOW TO RUN 
```shell
$./run_poc.sh 
```
```run_poc.sh```` builds docker image, sends necessary enviromental valiables and runs the container.

#### The benefit of this poc 
The visualisation of code review process helps us understand how much time we tend to spend to complete each commit and realise bottle neck when the process is not proceeding fast enough as expected

#### Further improvement
- Trigger
    All data from gerrit stream events are retrieved manually, only when main.py is run. 
    To automate this, some triggers need to be set and run the script automatically. 
- Different Tool
    This poc is only covering the process on gerrit, however, it is also addaptable to be used with other tools like GitHub, Gitlab and etc.. 
