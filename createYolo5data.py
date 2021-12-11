
# Python program to read
# json file
 
 
import json


def load_json():
    global data

    # Opening JSON file
    f = open('train.json')
    
    # returns JSON object as
    # a dictionary
    data =json.load(f)
    
    # Iterating through the json
    # list

    #print(type(data))
    for i in data['images']:
        #print(i['id'])
        print('')

    # Closing file
    f.close()

def write_textfile():

    list1 = ['a', 'b', 'c']
    dict_nine = {}
    for idx,i in enumerate(data['annotations']):
       # print(i[idx])
        #print(str(i['id'])+" "+str(i['bbox'][0])+" "+str(i['bbox'][1])+" "+str(i['bbox'][2])+" "+str(i['bbox'][3]))
        #print('kuy nine')
        
        #open('labels/%s.txt' % i['image_id'], 'w').write(str(i['category_id']-1)+" "+str(i['bbox'][0])+" "+str(i['bbox'][1])+" "+str(i['bbox'][2])+" "+str(i['bbox'][3]))
        if i['image_id'] in dict_nine:
            dict_nine[i['image_id']].append(str(i['category_id']-1)+" "+str((i['bbox'][0]*0.59259259259259)/640)+" "+str((i['bbox'][1]*0.33333333)/640)+" "+str((i['bbox'][2]*0.59259259259259)/640)+" "+str((i['bbox'][3]*0.33333333)/640))
        else:    
            dict_nine[i['image_id']] = [str(i['category_id']-1)+" "+str((i['bbox'][0]*0.59259259259259)/640)+" "+str((i['bbox'][1]*0.33333333)/640)+" "+str((i['bbox'][2]*0.59259259259259)/640)+" "+str((i['bbox'][3]*0.33333333)/640)]
    
    for key, val in dict_nine.items():
        open('labels/%s.txt' % key, 'w').write("\n".join(str(it) for it in val))

            
        #dict_nine = {i['image_id']:str(i['category_id']-1)+" "+str(i['bbox'][0])+" "+str(i['bbox'][1])+" "+str(i['bbox'][2])+" "+str(i['bbox'][3])}
load_json()
print("\n".join("nine"))
print("nine".join("MOo"))
#print(str(data['annotations'][0]['id'])+" "+str(data['annotations'][0]['bbox'][0])+" "+str(data['annotations'][0]['bbox'][1])+" "+str(data['annotations'][0]['bbox'][2])+" "+str(data['annotations'][0]['bbox'][3]))
#print(str(data['annotations'][0]['image_id'])+' '+'1')
# print('end')
#dict = {}
write_textfile()
#print(dict[20201108093343288])
