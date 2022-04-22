from read_data import read_data
from pprint import pprint 
import json
def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
        
    """
    foydalanuvchilar_id_raqamlari=[]
    foydalanuvchilar=data["messages"]
    for foydalanuvchi in foydalanuvchilar:
        if foydalanuvchi.get("from_id", False):
            foydalanuvchi_id_raqami=foydalanuvchi["from_id"]
            foydalanuvchilar_id_raqamlari.append(foydalanuvchi_id_raqami)
        # else:
        #     foydalanuvchi_id_raqami=foydalanuvchi["actor_id"]
        #     foydalanuvchilar_id_raqamlari.append(foydalanuvchi_id_raqami)
    
    
    return list(set(foydalanuvchilar_id_raqamlari))
   


pprint(find_all_users_id(read_data("data/result.json"))) 
