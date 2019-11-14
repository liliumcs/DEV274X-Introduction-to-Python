#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Program: list-o-matic

def list_o_matic(string, list_items):
    if string=="":
        last_item=list_items.pop()
        return last_item+ " popped from list\n"
    elif string in list_items:
        list_items.remove(string)
        return string+" removed from list\n"
    else:
        list_items.append(string)
        return string+" appended to list\n"
    
animals_on_farm=["cat","goat","cat"]   

while animals_on_farm:
    
    print("look at all the animals:", animals_on_farm)
    animal_checked=input("please enter the name of animal:")
    if animal_checked.lower()!="quit":
        print(list_o_matic(animal_checked,animals_on_farm))
    else:
        print("goodbye")
        break
        
print("Good-Bye")
    
    
    


# In[ ]:




