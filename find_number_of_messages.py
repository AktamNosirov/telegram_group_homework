
import json
def find_number_of_messages(data: dict)->int:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        int: Total number of messages.
    
    """
    
    items=data["messages"]
    n=0
    for item in items :
        if item.get("text"):
            n+=1
            
    return int(n)

data=open("data/result.json",'r', encoding="UTF8").read()
data=json.loads(data) 
print(find_number_of_messages(data))   


   