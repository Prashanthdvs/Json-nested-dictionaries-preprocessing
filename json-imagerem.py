def get_ids(data, key):
    stack = [data]
    result = []
    while stack:
        elem = stack.pop()
        if isinstance(elem, dict):
            for k, v in elem.items():
                if k == key:
                    result.append(k)
                if isinstance(elem, (list, dict)):
                    stack.append(v)
        elif isinstance(elem, list):
            for obj in elem:
                stack.append(obj)
    return result                   
new = get_ids(data=json_data()[0], key='Images')
print(new)

import json

def json_data():
    with open(r"C:\Users\damojipurapuv.d\Downloads\VMI_04052023.json", encoding='utf8') as f:
        data = json.load(f)
        return data

def delete_keys_from_dict(d, to_delete):
    if isinstance(to_delete, str):
        to_delete = [to_delete]
    if isinstance(d, dict):
        for single_to_delete in set(to_delete):
            if single_to_delete in d:
                del d[single_to_delete]
        for k, v in d.items():
            delete_keys_from_dict(v, to_delete)
    elif isinstance(d, list):
        for i in d:
            delete_keys_from_dict(i, to_delete)

d = json_data()[0]
delete_keys_from_dict(d, ['Images']) # inplace deletion 
print(d)
