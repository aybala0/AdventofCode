

pagenos = {}
with open('/Users/student/cs/advent_of_code/day5/pagedene.txt') as file:
  for line in file:
    key, val = line.strip().split('|')
    key = int(key)
    val = int(val)
    if key not in pagenos.keys():
      pagenos[key] = []
      pagenos[key].append(val)
    else:
      pagenos[key].append(val)

updates = []
with open('/Users/student/cs/advent_of_code/day5/updatedene.txt') as file2:
  for line2 in file2:
    updates.append([int(x) for x in line2.strip().split(',')])



def iscorrectly_ordered(update):
  seen = set()
  for page in update:
      seen.add(page)
      if page in pagenos:
        for i in pagenos[page]:
          if i in seen:
            return False
  return True

class Linkedlist:
    def __init__(self, val, prev=None, next=None) -> None:
        self.val = val
        self.prev = prev
        self.next = next

    def attach(self, val):
        newnode = Linkedlist(val, self, None)
        self.next = newnode

    @staticmethod
    def list_to_linked(arr):
        if not arr:
            return None
        newnode = Linkedlist(arr[0], None, None)
        save = newnode
        for elem in arr[1:]:
            newnode.attach(elem)
            newnode = newnode.next

        return save
    
    def linked_to_arr(self):
      result = []
      while(self):
        result.append(self.val)
        self = self.next
      return result


    def add_to_left_of(self, node):
      #take node out of its current place by reconnecting the other ends
      if node.prev:
        node.prev.next = node.next
      if node.next:
        node.next.prev = node.prev

      #add it to the left of self
      node.next = self
      if self.prev:
        node.prev = self.prev
        self.prev.next = node
        self.prev = node
      else:
         self.prev = node
         node.prev = None


    def printlist(self):
        traverser = self
        while traverser is not None:
            print(traverser.val, end=" -> ")
            traverser = traverser.next
        print("None")


arr = [3, 4, 5, 8, 3, 2]
linked_list = Linkedlist.list_to_linked(arr)


def fix_order(update):
  linked_list = Linkedlist.list_to_linked(update)
  traverser = linked_list.next
  while traverser is not None:
    head = linked_list
    while head.val != traverser.val:
      #print(f"head: {head.val}")
      if traverser.val in pagenos:
        if head.val in pagenos[traverser.val]:
          #print(f"self:{traverser.val} and node: {head.val}")
          traverser.add_to_left_of(head)
          
      head = head.next
    traverser = traverser.next
  return linked_list.linked_to_arr()
         

sum = 0
for update in updates:
  if not iscorrectly_ordered(update):
    new = fix_order(update)
    print(update, new)
    sum += new[int(len(new)/2)]

print(sum)
