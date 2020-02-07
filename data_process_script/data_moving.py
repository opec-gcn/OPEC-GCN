import json
name_sets = set()
with open("crowdpose_test.json",'r') as read:
    json_reader = json.load(read)
    annotations = json_reader['annotations']
    for an in annotations:
        img_id = an['image_id']
        name = str(img_id)+".jpg"
        name_sets.add(name)
name_list = list(name_sets)
name_list = sorted(name_list)
with open("test_list.txt", 'w') as writer:
    for name in name_list:
        writer.write("{}\n".format(name))


