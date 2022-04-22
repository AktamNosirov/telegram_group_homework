import json
def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
        
    """
    all_users_id=[]
    items=data["messages"]
    for item in items :
        if item.get("actor_id") :
            user=item.get("actor_id")
            all_users_id.append(user)
        if item.get("from_id") :
            user=item.get("from_id")
            all_users_id.append(user)
            
    return len(list(set(all_users_id)))
    # foydalanuvchilar_id_raqamlari=[]
    # foydalanuvchilar=data["messages"]
    
    # for foydalanuvchi in foydalanuvchilar:
    #     if foydalanuvchi.get("from_id") and foydalanuvchi["from_id"] not in foydalanuvchilar_id_raqamlari: 
    #         foydalanuvchi_id_raqami=foydalanuvchi["from_id"]
    #         foydalanuvchilar_id_raqamlari.append(foydalanuvchi_id_raqami)
    #     # if foydalanuvchi.get("actor_id") and foydalanuvchi["actor_id"] not in foydalanuvchilar_id_raqamlari:   
    #     #     foydalanuvchi_id_raqami=foydalanuvchi["actor_id"]
    #     #     foydalanuvchilar_id_raqamlari.append(foydalanuvchi_id_raqami)
    
    
    return foydalanuvchilar_id_raqamlari
   
data=open("data/result.json",'r', encoding="UTF8").read()
data=json.loads(data) 

print(find_all_users_id(data)) 
