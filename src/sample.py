"""
sample.py
This modules contains sample gerrit event data
to be used in unit tests. 
"""


change_mergeds=[{
    "submitter": {
        "name": "Royaee, Shaghayegh",
        "email": "shaghayegh.royaee@volvocars.com",
        "username": "sroyaee"
    },
    "newRev": "d5c5d0cc6fa0b9bdc453c1b37cfb49c50c860bbf",
    "patchSet": {
        "number": 1,
        "revision": "d5c5d0cc6fa0b9bdc453c1b37cfb49c50c860bbf",
        "parents": [
            "217e79df3e485b0b2db3e3f4aeb0b9f7061411a9"
        ],
        "ref": "refs/changes/37/14737/1",
        "uploader": {
            "name": "Royaee, Shaghayegh",
            "email": "shaghayegh.royaee@volvocars.com",
            "username": "sroyaee"
        },
        "createdOn": 1664806281,
        "author": {
            "name": "Royaee",
            "email": "SROYAEE@volvocars.com",
            "username": ""
        },
        "kind": "REWORK",
        "sizeInsertions": 5,
        "sizeDeletions": 5
    },
    "change": {
        "project": "csir/csir",
        "branch": "master",
        "id": "I40b9a29615b8351540fa8f81df1b782f5ec707c7",
        "number": 14737,
        "subject": "VISP ECU list",
        "owner": {
            "name": "Royaee, Shaghayegh",
            "email": "shaghayegh.royaee@volvocars.com",
            "username": "sroyaee"
        },
        "url": "https://gerrit.volvocars.biz/c/csir/csir/+/14737",
        "commitMessage": "VISP ECU list\n\nChange-Id: I40b9a29615b8351540fa8f81df1b782f5ec707c7\n",
        "createdOn": 1664806281,
        "status": "MERGED"
    },
    "project": "csir/csir",
    "refName": "refs/heads/master",
    "changeKey": {
        "id": "I40b9a29615b8351540fa8f81df1b782f5ec707c7"
    },
    "type": "change-merged",
    "eventCreatedOn": 1664806295
},{
    "submitter": {
        "name": "Belbek, Tughan",
        "email": "tughan.belbek@volvocars.com",
        "username": "tbelbek"
    },
    "newRev": "e2db0e17ab990fbc57d5e9e47d18526d76ce48e2",
    "patchSet": {
        "number": 1,
        "revision": "e2db0e17ab990fbc57d5e9e47d18526d76ce48e2",
        "parents": [
            "978804d70bb1b1e763d139b75dd77b03ed5576bc"
        ],
        "ref": "refs/changes/36/14736/1",
        "uploader": {
            "name": "Belbek, Tughan",
            "email": "tughan.belbek@volvocars.com",
            "username": "tbelbek"
        },
        "createdOn": 1664806207,
        "author": {
            "name": "Belbek, Tughan",
            "email": "tughan.belbek@volvocars.com",
            "username": "tbelbek"
        },
        "kind": "REWORK",
        "sizeInsertions": 4,
        "sizeDeletions": 4
    },
    "change": {
        "project": "swecs/network_and_power_map",
        "branch": "master",
        "id": "I1f8b65f9ff77b0f464dc91d83b53adcc72468c1c",
        "number": 14736,
        "subject": "tc names added",
        "owner": {
            "name": "Belbek, Tughan",
            "email": "tughan.belbek@volvocars.com",
            "username": "tbelbek"
        },
        "url": "https://gerrit.volvocars.biz/c/swecs/network_and_power_map/+/14736",
        "commitMessage": "tc names added\n\nChange-Id: I1f8b65f9ff77b0f464dc91d83b53adcc72468c1c\n",
        "createdOn": 1664806207,
        "status": "MERGED"
    },
    "project": "swecs/network_and_power_map",
    "refName": "refs/heads/master",
    "changeKey": {
        "id": "I1f8b65f9ff77b0f464dc91d83b53adcc72468c1c"
    },
    "type": "change-merged",
    "eventCreatedOn": 1664806221
}]

comment_addeds=[
    {
    "author": {
        "name": "Royaee, Shaghayegh",
        "email": "shaghayegh.royaee@volvocars.com",
        "username": "sroyaee"
    },
    "approvals": [
        {
            "type": "Verified",
            "description": "Verified",
            "value": "2",
            "oldValue": "0"
        },
        {
            "type": "Code-Review",
            "description": "Code-Review",
            "value": "2",
            "oldValue": "0"
        }
    ],
    "comment": "Patch Set 1: Verified+2 Code-Review+2",
    "patchSet": {
        "number": 1,
        "revision": "d5c5d0cc6fa0b9bdc453c1b37cfb49c50c860bbf",
        "parents": [
            "217e79df3e485b0b2db3e3f4aeb0b9f7061411a9"
        ],
        "ref": "refs/changes/37/14737/1",
        "uploader": {
            "name": "Royaee, Shaghayegh",
            "email": "shaghayegh.royaee@volvocars.com",
            "username": "sroyaee"
        },
        "createdOn": 1664806281,
        "author": {
            "name": "Royaee",
            "email": "SROYAEE@volvocars.com",
            "username": ""
        },
        "kind": "REWORK",
        "sizeInsertions": 5,
        "sizeDeletions": 5
    },
    "change": {
        "project": "csir/csir",
        "branch": "master",
        "id": "I40b9a29615b8351540fa8f81df1b782f5ec707c7",
        "number": 14737,
        "subject": "VISP ECU list",
        "owner": {
            "name": "Royaee, Shaghayegh",
            "email": "shaghayegh.royaee@volvocars.com",
            "username": "sroyaee"
        },
        "url": "https://gerrit.volvocars.biz/c/csir/csir/+/14737",
        "commitMessage": "VISP ECU list\n\nChange-Id: I40b9a29615b8351540fa8f81df1b782f5ec707c7\n",
        "createdOn": 1664806281,
        "status": "NEW"
    },
    "project": "csir/csir",
    "refName": "refs/heads/master",
    "changeKey": {
        "id": "I40b9a29615b8351540fa8f81df1b782f5ec707c7"
    },
    "type": "comment-added",
    "eventCreatedOn": 1664806292
},{
    "author": {
        "name": "Belbek, Tughan",
        "email": "tughan.belbek@volvocars.com",
        "username": "tbelbek"
    },
    "approvals": [
        {
            "type": "Verified",
            "description": "Verified",
            "value": "2",
            "oldValue": "0"
        },
        {
            "type": "Code-Review",
            "description": "Code-Review",
            "value": "2",
            "oldValue": "0"
        }
    ],
    "comment": "Patch Set 1: Verified+2 Code-Review+2",
    "patchSet": {
        "number": 1,
        "revision": "e2db0e17ab990fbc57d5e9e47d18526d76ce48e2",
        "parents": [
            "978804d70bb1b1e763d139b75dd77b03ed5576bc"
        ],
        "ref": "refs/changes/36/14736/1",
        "uploader": {
            "name": "Belbek, Tughan",
            "email": "tughan.belbek@volvocars.com",
            "username": "tbelbek"
        },
        "createdOn": 1664806207,
        "author": {
            "name": "Belbek, Tughan",
            "email": "tughan.belbek@volvocars.com",
            "username": "tbelbek"
        },
        "kind": "REWORK",
        "sizeInsertions": 4,
        "sizeDeletions": 4
    },
    "change": {
        "project": "swecs/network_and_power_map",
        "branch": "master",
        "id": "I1f8b65f9ff77b0f464dc91d83b53adcc72468c1c",
        "number": 14736,
        "subject": "tc names added",
        "owner": {
            "name": "Belbek, Tughan",
            "email": "tughan.belbek@volvocars.com",
            "username": "tbelbek"
        },
        "url": "https://gerrit.volvocars.biz/c/swecs/network_and_power_map/+/14736",
        "commitMessage": "tc names added\n\nChange-Id: I1f8b65f9ff77b0f464dc91d83b53adcc72468c1c\n",
        "createdOn": 1664806207,
        "status": "NEW"
    },
    "project": "swecs/network_and_power_map",
    "refName": "refs/heads/master",
    "changeKey": {
        "id": "I1f8b65f9ff77b0f464dc91d83b53adcc72468c1c"
    },
    "type": "comment-added",
    "eventCreatedOn": 1664806218
},{
    "author": {
        "name": "BPPCLIMA, BPP (B.)",
        "username": "bppclima"
    },
    "approvals": [
        {
            "type": "Verified",
            "description": "Verified",
            "value": "0"
        },
        {
            "type": "Code-Review",
            "description": "Code-Review",
            "value": "0"
        }
    ],
    "comment": "Patch Set 10:\n\nCheck chain finished with verdict failed: https://victoria.volvocars.biz/product/PSRC7E709E01/If46bf9a6c3250a3fdeecf2299594f0ea61de3328",
    "patchSet": {
        "number": 10,
        "revision": "797df340ade55cc8904d704201cf2a26c5a35dfd",
        "parents": [
            "7a723d71e2238ac5a57dec79be757019f3510f09"
        ],
        "ref": "refs/changes/12/14612/10",
        "uploader": {
            "name": "Berglund, Mattias",
            "email": "mattias.berglund.4@volvocars.com",
            "username": "mbergl17"
        },
        "createdOn": 1664806035,
        "author": {
            "name": "Berglund, Mattias",
            "email": "mattias.berglund.4@volvocars.com",
            "username": "mbergl17"
        },
        "kind": "REWORK",
        "sizeInsertions": 149,
        "sizeDeletions": 5
    },
    "change": {
        "project": "cider/thermal-mgmt-and-climate-verification",
        "branch": "master",
        "id": "If46bf9a6c3250a3fdeecf2299594f0ea61de3328",
        "number": 14612,
        "subject": "ARTCLIMATE-36871: Add snok example test",
        "owner": {
            "name": "Berglund, Mattias",
            "email": "mattias.berglund.4@volvocars.com",
            "username": "mbergl17"
        },
        "url": "https://gerrit.volvocars.biz/c/cider/thermal-mgmt-and-climate-verification/+/14612",
        "commitMessage": "ARTCLIMATE-36871: Add snok example test\n\nChange-Id: If46bf9a6c3250a3fdeecf2299594f0ea61de3328\n",
        "createdOn": 1664790006,
        "status": "NEW",
        "wip": "true"
    },
    "project": "cider/thermal-mgmt-and-climate-verification",
    "refName": "refs/heads/master",
    "changeKey": {
        "id": "If46bf9a6c3250a3fdeecf2299594f0ea61de3328"
    },
    "type": "comment-added",
    "eventCreatedOn": 1664806218
},{
    "author": {
        "name": "BPPCLIMA, BPP (B.)",
        "username": "bppclima"
    },
    "approvals": [
        {
            "type": "Verified",
            "description": "Verified",
            "value": "-1",
            "oldValue": "0"
        },
        {
            "type": "Code-Review",
            "description": "Code-Review",
            "value": "0"
        }
    ],
    "comment": "Patch Set 10: Verified-1",
    "patchSet": {
        "number": 10,
        "revision": "797df340ade55cc8904d704201cf2a26c5a35dfd",
        "parents": [
            "7a723d71e2238ac5a57dec79be757019f3510f09"
        ],
        "ref": "refs/changes/12/14612/10",
        "uploader": {
            "name": "Berglund, Mattias",
            "email": "mattias.berglund.4@volvocars.com",
            "username": "mbergl17"
        },
        "createdOn": 1664806035,
        "author": {
            "name": "Berglund, Mattias",
            "email": "mattias.berglund.4@volvocars.com",
            "username": "mbergl17"
        },
        "kind": "REWORK",
        "sizeInsertions": 149,
        "sizeDeletions": 5
    },
    "change": {
        "project": "cider/thermal-mgmt-and-climate-verification",
        "branch": "master",
        "id": "If46bf9a6c3250a3fdeecf2299594f0ea61de3328",
        "number": 14612,
        "subject": "ARTCLIMATE-36871: Add snok example test",
        "owner": {
            "name": "Berglund, Mattias",
            "email": "mattias.berglund.4@volvocars.com",
            "username": "mbergl17"
        },
        "url": "https://gerrit.volvocars.biz/c/cider/thermal-mgmt-and-climate-verification/+/14612",
        "commitMessage": "ARTCLIMATE-36871: Add snok example test\n\nChange-Id: If46bf9a6c3250a3fdeecf2299594f0ea61de3328\n",
        "createdOn": 1664790006,
        "status": "NEW",
        "wip": "true"
    },
    "project": "cider/thermal-mgmt-and-climate-verification",
    "refName": "refs/heads/master",
    "changeKey": {
        "id": "If46bf9a6c3250a3fdeecf2299594f0ea61de3328"
    },
    "type": "comment-added",
    "eventCreatedOn": 1664806219
}]

patchset_createds=[{
    "uploader": {
        "name": "Royaee, Shaghayegh",
        "email": "shaghayegh.royaee@volvocars.com",
        "username": "sroyaee"
    },
    "patchSet": {
        "number": 1,
        "revision": "d5c5d0cc6fa0b9bdc453c1b37cfb49c50c860bbf",
        "parents": [
            "217e79df3e485b0b2db3e3f4aeb0b9f7061411a9"
        ],
        "ref": "refs/changes/37/14737/1",
        "uploader": {
            "name": "Royaee, Shaghayegh",
            "email": "shaghayegh.royaee@volvocars.com",
            "username": "sroyaee"
        },
        "createdOn": 1664806281,
        "author": {
            "name": "Royaee",
            "email": "SROYAEE@volvocars.com",
            "username": "sroyaee"
        },
        "kind": "REWORK",
        "sizeInsertions": 5,
        "sizeDeletions": 5
    },
    "change": {
        "project": "csir/csir",
        "branch": "master",
        "id": "I40b9a29615b8351540fa8f81df1b782f5ec707c7",
        "number": 14737,
        "subject": "VISP ECU list",
        "owner": {
            "name": "Royaee, Shaghayegh",
            "email": "shaghayegh.royaee@volvocars.com",
            "username": "sroyaee"
        },
        "url": "https://gerrit.volvocars.biz/c/csir/csir/+/14737",
        "commitMessage": "VISP ECU list\n\nChange-Id: I40b9a29615b8351540fa8f81df1b782f5ec707c7\n",
        "createdOn": 1664806281,
        "status": "NEW"
    },
    "project": "csir/csir",
    "refName": "refs/heads/master",
    "changeKey": {
        "id": "I40b9a29615b8351540fa8f81df1b782f5ec707c7"
    },
    "type": "patchset-created",
    "eventCreatedOn": 1664806281
},{
    "uploader": {
        "name": "Belbek, Tughan",
        "email": "tughan.belbek@volvocars.com",
        "username": "tbelbek"
    },
    "patchSet": {
        "number": 11,
        "revision": "e2db0e17ab990fbc57d5e9e47d18526d76ce48e2",
        "parents": [
            "978804d70bb1b1e763d139b75dd77b03ed5576bc"
        ],
        "ref": "refs/changes/36/14736/11",
        "uploader": {
            "name": "Belbek, Tughan",
            "email": "tughan.belbek@volvocars.com",
            "username": "tbelbek"
        },
        "createdOn": 1664806207,
        "author": {
            "name": "Belbek, Tughan",
            "email": "tughan.belbek@volvocars.com",
            "username": "tbelbek"
        },
        "kind": "REWORK",
        "sizeInsertions": 4,
        "sizeDeletions": 4
    },
    "change": {
        "project": "swecs/network_and_power_map",
        "branch": "master",
        "id": "I1f8b65f9ff77b0f464dc91d83b53adcc72468c1c",
        "number": 14736,
        "subject": "tc names added",
        "owner": {
            "name": "Belbek, Tughan",
            "email": "tughan.belbek@volvocars.com",
            "username": "tbelbek"
        },
        "url": "https://gerrit.volvocars.biz/c/swecs/network_and_power_map/+/14736",
        "commitMessage": "tc names added\n\nChange-Id: I1f8b65f9ff77b0f464dc91d83b53adcc72468c1c\n",
        "createdOn": 1664806207,
        "status": "NEW"
    },
    "project": "swecs/network_and_power_map",
    "refName": "refs/heads/master",
    "changeKey": {
        "id": "I1f8b65f9ff77b0f464dc91d83b53adcc72468c1c"
    },
    "type": "patchset-created",
    "eventCreatedOn": 1664806207
}]

