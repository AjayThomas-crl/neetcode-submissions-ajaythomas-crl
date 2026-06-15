class Node:
    def __init__(self, key,value):
        self.val=value
        self.key=key
        self.next=self.prev=None
class LRUCache:

    def __init__(self, capacity: int):
        self.m={}
        self.cap=capacity

        self.left,self.right=Node(0,0),Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left

    def remove(self,node):
        prev,nxt=node.prev,node.next
        prev.next=nxt
        nxt.prev=prev
    def insert(self,node):
        t=self.right.prev
        self.right.prev=node
        node.next=self.right
        t.next=node
        node.prev=t

    def get(self, key: int) -> int:
        return self.m.get(key).val if self.m.get(key) else -1

    def put(self, key: int, value: int) -> None:
        if(key in self.m):
            self.remove(self.m[key])
        n=Node(key,value)
        self.m[key]=n
        self.insert(n)

        if(len(self.m)>self.cap):
            del self.m[self.left.next.key]
            self.remove(self.left.next)
        
        return None


