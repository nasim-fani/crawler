import json
''
file = open('./snopes/output.json', mode='r')
data = json.load(file)
dest_data = json.dumps(data, indent=1)
dest_file = open('prettified_output.json', 'w')
dest_file.write(dest_data)
file.close()
dest_file.close()

