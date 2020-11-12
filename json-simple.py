import json
import os


def put(object: json, key, value):
    info = json.dumps(object).strip("{").strip("}").split(", ")
    info.append(f'"{key}": {value}')
    result_string = "{"
    i = 0    
    for x in info:
            if i < len(info) - 1:
                result_string += f"{x}, "
            else:
                result_string += f"{x}"
            i += 1
    result_string += "}"
    return json.loads(result_string)


def get(object: json, key):
    info = json.dumps(object).strip("{").strip("}").split(", ")
    for x in info:
        if str(f'"{key}"') in x:
            return str(x).split(":")[1].strip()
