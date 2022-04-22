
import json
def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """     
    all_users_name=[]
    items=data["messages"]
    for item in items :
        if item.get("actor") and item.get("actor") not in all_users_name:
            user=item.get("actor")
            all_users_name.append(user)
        # if item.get("from") and item.get("from") not in all_users_name:
        #     user=item.get("from")
        #     all_users_name.append(user)
        
    return list(all_users_name)
    

 
data=open("data/result.json",'r', encoding="UTF8").read()
data=json.loads(data) 
print(find_all_users_name(data)) 

