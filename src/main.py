from ssh import events_streamer
from event_to_span import create_change_span, create_patch_span, complete_patch_span,create_code_review_span,create_comment_span,complete_trace


event_type=["patchset-created","comment-added","change-merged","change-abandoned"]

for i in range(len(event_type)):
   events=events_streamer(event_type[i])
   for event in events:
        if event_type[i] == "patchset-created":
            if event['patchSet']['number'] == 1 : #If it's the first patch
                #Create change span 
                create_change_span(event)
                #Create patch 1 span 
                create_patch_span(event)
                # sent_spans.append(ctx)
            else:
                #Complete previous patch span 
                complete_patch_span(event)
                #Create patch span (find nr in function)
                create_patch_span(event)
            

        elif event_type[i] == "comment-added":
            #Create code review span 
            ctx=create_code_review_span(event)
            #Create comment span 
            create_comment_span(event,ctx)
                

        elif event_type[i] == "change-merged" or event_type[i] == "change-abandoned":
            complete_trace(event)
            

