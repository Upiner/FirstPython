import json

sample_dic = {"key21": "value21", "key22": "value22"}
sample_array = ["value31", "value32", "value33"]
main_dic = {"key1": "value1"}
main_dic["key2"] = sample_dic
main_dic["key3"] = sample_array
json_str = json.dumps(main_dic, indent=2)
file_descriptor= open(r'lesson2.json', 'w',encoding='utf-16')
file_descriptor.write(json_str)
file_descriptor.close()

file_descriptor= open(r'lesson2.json','r',encoding='utf-16')
json_str=file_descriptor.read()
main2_dic=json.loads(json_str)
print(main2_dic)
print(main_dic)