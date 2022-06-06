from multiprocessing.sharedctypes import Value
from pickle import TRUE


set = {'banana','strawberry','cherry','grapes','apple','berry'}
print(set)
remove = input("Enter the item you want to remove from the set : ")
mod_list = remove in set
if mod_list == True:
    set.discard(remove)
print(set)