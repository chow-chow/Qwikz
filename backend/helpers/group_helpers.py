import random
import string

def generate_group_code(group_name):
    words = [word for word in group_name.split() if word]
    first_letters = ''.join(word[0] for word in words[:2]).upper()
    random_part_length = 5 if len(first_letters) == 1 else 4
    random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=random_part_length))
    group_code = f"{first_letters}-{random_part}"
    return group_code

def generate_access_token():
    #  ACCESS_TOKEN with format XXXX-XXXX-XXXX
    parts = [''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) for _ in range(3)]
    access_token = '-'.join(parts)
    return access_token

def prepare_group_object(group_name, teacher_id):
    group_code = generate_group_code(group_name)
    access_token = generate_access_token()
    
    group_object = {
        "GROUP_NAME": group_name,
        "GROUP_CODE": group_code,
        "ACCESS_TOKEN": access_token,
        "TEACHER_ID": teacher_id
    }
    
    return group_object