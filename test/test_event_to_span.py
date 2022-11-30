import unittest
import sys
sys.path.append('/home/rclement/follow-my-commit/tempo_poc/')

from event_to_span import get_patchset_st,create_change_span,complete_change_span,create_patch_span,complete_patch_span
from sample import patchset_createds,comment_addeds,change_mergeds

class TestEventToSpan (unittest.TestCase):
    def setUp(self):
        self.change_id="Ia1ed8917012cc22cae80d8da3c8d46270b8a4607"
        self.patch_nr= 3
        self.event= patchset_createds[0]
        self.second_event= patchset_createds[1]
        self.third_event=comment_addeds[0]
        self.fourth_event = change_mergeds[0]
        self.name="Royaee, Shaghayegh"
        self.username="sroyaee"
        self.attribute="Royaee, Shaghayegh (sroyaee)"
     
    def test_get_patchset_st(self):
        st=1668094038000000000
        result=get_patchset_st(self.change_id,self.patch_nr)
        self.assertEqual(result,st)
    
    def test_project_name(self):
        project= "csir/csir"
        result=self.event['change']['project']    
        self.assertEqual(project,result)
    
    def test_change_nr(self):
        change_nr= 14737
        result= self.event['change']['number']
        self.assertEqual(change_nr,result)

    def test_span_name(self):
        project= "14737(csir/csir)"
        result = project=f"{self.event['change']['number']}({self.event['change']['project']})"
        self.assertEqual(project,result) 
    
    def test_change_timestamp(self):
        timestamp=1664806281
        result = self.event['change']['createdOn']
        self.assertEqual(timestamp,result)         
    
    def test_change_ref(self):
        ref="refs/changes/37/14737/1"
        result=self.event['patchSet']['ref']
        self.assertEqual(ref,result)   

    def test_owner_name(self):
        result= self.event['change']['owner']['name'] 
        self.assertEqual(self.name,result) 
    
    def test_owner_username(self):
        result= self.event['change']['owner']['username']
        self.assertEqual(self.username,result) 
    
    def test_owner_attribute(self):   
        result= f"{self.event['change']['owner']['name']} ({self.event['change']['owner']['username']})"
        self.assertEqual(self.attribute,result)

    def test_change_subject(self):
        sub= "VISP ECU list"
        result=self.event['change']['subject']
        self.assertEqual(sub,result) 

    def test_create_change_span(self):
        ctx="SpanContext(trace_id=0x7961e350e4e6d59ae9070aa7d7b3ac91, span_id=0x32bf7bf191f0a905, trace_flags=0x01, trace_state=[], is_remote=False)"
        result=str(create_change_span(self.event))
        self.assertEqual(ctx,result)

    def test_event_created_time(self):
        time=1664806281
        result=self.event["eventCreatedOn"]    
        self.assertEqual(time,result)
    
    def test_complete_change_span(self):
        ctx="SpanContext(trace_id=0x7961e350e4e6d59ae9070aa7d7b3ac91, span_id=0x32bf7bf191f0a905, trace_flags=0x01, trace_state=[], is_remote=False)"
        result=str(complete_change_span(self.fourth_event))
        self.assertEqual(ctx,result)

    def test_patch_nr(self):
        patch_nr= 1
        result=self.event['patchSet']['number']
        self.assertEqual(patch_nr,result)
    
    def test_change_id(self):
        result=self.event['change']['id']
        change_id="I40b9a29615b8351540fa8f81df1b782f5ec707c7"
        self.assertEqual(change_id,result)
    
    def test_event_type(self):
        event_type="patchset-created"
        result=self.event['type']
        self.assertEqual(event_type,result)
    
    def test_patch_kind(self):
        kind="REWORK"   
        result=self.event['patchSet']['kind']
        self.assertEqual(kind,result)
    
    def test_uploader_name(self):
        result=self.event['uploader']['name']
        self.assertEqual(self.name,result)
    
    def test_uploader_username(self):
        result=self.event['uploader']['username']   
        self.assertEqual(self.username,result)
    
    def test_uploader_attribute(self):
        result=f"{self.event['uploader']['name']} ({self.event['uploader']['username']})"
        self.assertEqual(self.attribute,result)

    def test_create_patch_span(self):
        ctx="SpanContext(trace_id=0x7961e350e4e6d59ae9070aa7d7b3ac91, span_id=0x21eecf11b1ec6c1e, trace_flags=0x01, trace_state=[], is_remote=False)"
        result=str(create_patch_span(self.event))
        self.assertEqual(ctx,result)
    
    def test_another_patch_nr(self):
        patch_nr=11
        result=self.second_event['patchSet']['number']
        self.assertEqual(patch_nr,result)

    def test_submitter_name(self):
        result= self.fourth_event['submitter']['name']
        self.assertEqual(self.name,result)

    def test_submitter_username(self):
        result=self.fourth_event['submitter']['username']
        self.assertEqual(self.username, result)

    def test_author_name(self):
        result=self.third_event['author']['name']
        self.assertEqual(self.name,result)

    def test_author_username(self):
        result=self.third_event['author']['username']
        self.assertEqual(self.username,result)

    def test_v_approval_value(self):
        value="2"
        result= self.third_event['approvals'][0]['value'] 
        self.assertEqual(value,result)

    def test_cr_approval_value(self):
        value="2"
        result= self.third_event['approvals'][1]['value']  
        self.assertEqual(value,result)     
    
    def test_comment_value(self):
        value="Patch Set 1: Verified+2 Code-Review+2"
        result=self.third_event['comment']
        self.assertEqual(value,result)
    
    def test_attribute_url(self):
        url="https://gerrit.volvocars.biz/c/csir/csir/+/14737"
        result=self.event['change']['url']
        self.assertEqual(result,url)
