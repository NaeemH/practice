#!/usr/bin/env python3

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
    self.headval = None

def traverse(self):
    node = self # start from first node
    while node!=None:
        print(node.val) # Access whole node value
        node = node.next # Move on to next node

traverse(head)

