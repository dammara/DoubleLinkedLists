# Markhus Dammar
# 3/3/2020
# This is the driver for DLL

from ClassDL import ListNode, DoubleLinkedList
import time

myList = DoubleLinkedList()
print("Here's the empty list.")
print(myList)
time.sleep(1)

print("Now, let's fill up the list.")
myList.push_head(3)
time.sleep(1)
print(myList)
myList.push_head(5)
time.sleep(1)
print(myList)
myList.push_head(12)
time.sleep(1)
print(myList)
myList.push_end(8)
time.sleep(1)
print(myList)
myList.push_end(0)
time.sleep(1)
print(myList)

print("""I'm going to add two more numbers, one to the head,
and one to the end""")
time.sleep(1)
myList.push_head(18)
print(myList)
time.sleep(1)
myList.push_end(44)
print(myList)

time.sleep(1)

print("Let's try removing the head of the list.")
time.sleep(1)
myList.pop_head()
print(myList)
time.sleep(1)

print("Cool. Lastly, let's pop the end of the list")
myList.pop_end()
print(myList)
time.sleep(1)

print("Watching this wasn't exciting, but finishing it was.")
time.sleep(1.3)
print("Have a nice day!")
time.sleep(2)
exit()
