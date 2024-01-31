

# Linked List under the Hood

head={
    "value":23,
    "next":{
        "value":10,
        "next":{
            "value":45,
            "next":{
                "value":20,
                "next":None
            }
        }
    }
}

print(head['next']['next']['value'])


# This will only work with Linked list
# print(my_linked_list.head.next.next.value)
