import json
import yaml

#---json to yaml

with open("sample_json.json", "r") as file:
	info = json.load(file)

with open("yaml_file.yaml", "w") as new_file:
	yaml.dump(info, new_file)
	

#---json to txt

with open("sample_json.json", "r") as file:
	info = json.load(file)

with open("js_txt_file.txt", "w") as new_txt:
	json.dump(info,new_txt)	


#---yaml to txt

with open("yaml_file.yaml", "r") as file:
	info = yaml.safe_load(file)

with open("yaml_txt_file.txt", "w") as new_file:
	yaml.dump(info,new_file )


#---yaml to json
		
with open("yaml_file.yaml", "r") as file:
	info = yaml.safe_load(file)	

with open("json_file.json", "w") as new_file:
	json.dump(info,new_file)		

	