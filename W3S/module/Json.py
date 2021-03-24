import json 

json_object = '{"name":"Rafael", "age":"20","city":"New york"}'


json_to_python = json.loads(json_object) # Will go a be now a dict

print(json_to_python["name"]) 


python_object = {
    "name":"Sasha",
    "age":2
}

python_object_to_json = json.dumps(python_object, indent=2, sort_keys=True)

print(python_object_to_json) # This now is a JSON