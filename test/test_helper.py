import unittest
import sys
sys.path.append('/home/rclement/follow-my-commit/tempo_poc/')

from helper import convert_to_ns,create_trace_id,md5_span_id, create_span_id, parent_span_id,create_context
from sample import change_mergeds, comment_addeds,patchset_createds

"""
.assertEqual(a,b) #a==b
.assertTrue(x) # x is True / .assertFalse(x) # x is False
.assertIs(a,b) #a is b (*means exact same object) 
.assertIsNone(x) # x is None
.assertIn(a,b) # a in b
.assertIsInstance(a,b) # isinstance(a,b)
with self.assertRaises(TypeError): 


"""

class TestHelper(unittest.TestCase): 
    def setUp(self): 
        self.event=patchset_createds[0]
        self.second_event=patchset_createds[1]
        self.third_event=comment_addeds[0]
        self.fourth_event=change_mergeds[0]

    def test_convert_to_ns(self):
        """
        Test if the function converts seconds 
        to nano seconds (add 000000000 to seconds)
        """
        result = convert_to_ns(1664806207)
        self.assertEqual(result,1664806207000000000)

    def test_change_id_value(self):
        change_id= self.event['change']['id'] 
        self.assertEqual(change_id,"I40b9a29615b8351540fa8f81df1b782f5ec707c7")
        
    def test_bstring_value(self): 
        bstring = self.event['change']['id'].encode('ASCII')
        self.assertEqual(bstring, b'I40b9a29615b8351540fa8f81df1b782f5ec707c7')
    
    def test_create_trace_id(self):
        #check if the func gives right trace id as int 
        trace_id=create_trace_id(self.event)
        self.assertEqual(trace_id,161344850801327372871090236364216839313)
    
    def test_ref(self):
         ref= self.event['patchSet']['ref']
         self.assertEqual(ref, "refs/changes/37/14737/1" )
    
    def test_event_type(self):
        event_type=self.event['type'] 
        self.assertEqual(event_type, "patchset-created")      
        
    def test_md5_span_id(self):
        seed = "refs/changes/37/14737/1/patchset-created"
        span_id=md5_span_id(seed)
        self.assertEqual(span_id,2445119322615213086)
    
    def test_patch_number(self):
        patch_nr= self.event['patchSet']['number']
        self.assertEqual(patch_nr, 1)

    def test_create_change_span_id(self):
        event_type="change-created"
        span_id=create_span_id(self.event,event_type)
        self.assertEqual(span_id,3656777699913935109)

    def test_another_change_span_id(self):     
        event_type="change-created"
        span_id=create_span_id(self.second_event,event_type)
        self.assertEqual(span_id,3726526977171287613)

    def test_author_username(self):
        username = self.third_event['author']['username']
        self.assertEqual(username,"sroyaee")

    def test_event_timestamp(self):
        timestamp=self.event['eventCreatedOn']
        self.assertEqual(timestamp,1664806281)

    def test_create_merged_span_id(self):
        #Original string: "refs/changes/37/14737/1/change-merged"
        span_id=create_span_id(self.fourth_event,"change-merged")
        self.assertEqual(span_id,5341229920358995322)

    def test_create_abandoned_span_id(self):
        span_id=create_span_id(self.fourth_event,"change-abandoned")
        self.assertEqual(span_id,4313595830787140576)    

    def test_create_comment_added_span_id(self):
        span_id=create_span_id(self.third_event,"comment-added") 
        self.assertEqual(span_id,912564414786104282)   

    def test_code_review_span_id(self): 
        span_id=create_span_id(self.third_event,"code-review")
        self.assertEqual(span_id,13009815151174474523) 
    
    def test_another_ref(self):
         ref= self.second_event['patchSet']['ref']
         self.assertEqual(ref, "refs/changes/36/14736/11" )
    
    def  test_another_patch_nr(self):
        patch_nr=self.second_event['patchSet']['number']
        self.assertEqual(patch_nr,11)
        
    def test_parent_change_span_id(self):
        span_id=parent_span_id(self.second_event)
        self.assertEqual(span_id,3726526977171287613)   
    
    def test_parent_patchset_span_id(self):
        span_id=parent_span_id(self.third_event)
        self.assertEqual(span_id,2445119322615213086)

    def test_create_context(self):
        trace_id=168635087381289086935107083630587480781
        span_id=2538368262749868298
        result= str(create_context(trace_id,span_id))
        context= "SpanContext(trace_id=0x7eddefbaf0240df763b65c7193690acd, span_id=0x233a187c7254d10a, trace_flags=0x01, trace_state=[], is_remote=True)"
        self.assertEqual(result,context)



# if __name__ == "__main__":
#     unittest.main()#pragma:no cover 

# event=patchset_createds[1]
# print(create_span_id(event,"change-created"))