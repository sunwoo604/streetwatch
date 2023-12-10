#%%
import json
import os
from sklearn.model_selection import train_test_split
import shutil

#%%
OH = ['OH', 'poles', 'Power Poles', 'pole']
UG = ['UG','underground', 'Power Boxes', 'surface structure', 'Underhead Structure', 'surface structures']
ann_path = '../data/annotations'
anns = []
for f in os.listdir(ann_path):
    if f[0] =='.':
        continue
    temp = json.load(open(os.path.join(ann_path,f)))
    anns += [temp]

curr = 0
for i, ann in enumerate(anns):
    id_img = {}
    id_ann = {}

    for img in ann['images']:
        old_id = img['id']
        img['id'] = curr
        curr += 1
        id_img[old_id] = img
    
    for a in ann['annotations']:
        if a['image_id'] not in id_ann:
            id_ann[a['image_id']] = [a]
        else:
            id_ann[a['image_id']] += [a]
    
    imgs = []
    annotations = []
    for k in id_img.keys():
        img = id_img[k]
        imgs += [img]
        if k in id_ann:
            temp = id_ann[k]
            for a in temp:
                a['image_id'] = img['id']
                annotations += [a]
    ann['images'] = imgs
    ann['annotations'] = annotations
    anns[i] = ann

for i, ann in enumerate(anns):
    id_cat = {}
    id_ann = {}

    for cat in ann['categories']:
        old_id = cat['id']
        if cat['name'] in OH:
            cat['id'] = 0
            cat['name'] = 'OH'
        elif cat['name'] in UG:
            cat['id'] = 1
            cat['name'] = 'UG'
        else:
            continue
        id_cat[old_id] = cat
    
    for a in ann['annotations']:
        if a['category_id'] not in id_ann:
            id_ann[a['category_id']] = [a]
        else:
            id_ann[a['category_id']] += [a]
    cats = []
    annotations = []
    for k in id_cat.keys():
        cat = id_cat[k]
        cats += [cat]
        temp = id_ann[k]
        for a in temp:
            a['category_id'] = img['id']
            annotations += [a]
    ann['categories'] = cats
    ann['annotations'] = annotations
    anns[i] = ann


# %%
train = {
    'licenses':[], 
    'info':[], 
    'categories':[], 
    'images':[], 
    'annotations':[]
}
test = {
    'licenses':[], 
    'info':[], 
    'categories':[], 
    'images':[], 
    'annotations':[]
}
idxs = [0,1,2,3,4,5,6,7,8,9]
train_idx, val_idx = train_test_split(idxs, test_size=0.2)

for idx in train_idx:
    if len(train['licenses']) == 0:
        train['licenses'] += [anns[idx]['licenses']]
    if len(train['info']) == 0:
        train['info'] += [anns[idx]['info']]
    if len(train['categories']) == 0:
        train['categories'] = anns[idx]['categories']
    train['images'] += anns[idx]['images']
    train['annotations'] += anns[idx]['annotations']

for idx in val_idx:
    if len(test['licenses']) == 0:
        test['licenses'] += [anns[idx]['licenses']]
    if len(test['info']) == 0:
        test['info'] += [anns[idx]['info']]
    if len(test['categories']) == 0:
        test['categories'] = anns[idx]['categories']
    test['images'] += anns[idx]['images']
    test['annotations'] += anns[idx]['annotations']


# %%
json_path = '../data/json'
with open(os.path.join(json_path,'train.json'), 'w') as fp:
    json.dump(train, fp)
with open(os.path.join(json_path,'val.json'), 'w') as fp:
    json.dump(test, fp)
# %%
img_path = '../data/images'
train_path = '../data/images/train'
val_path = '../data/images/val'

for i in train['images']:
    print(f)
    f = i['file_name']
    shutil.copy(os.path.join(img_path,f),os.path.join(train_path,f))
for i in test['images']:
    f = i['file_name']
    shutil.copy(os.path.join(img_path,f),os.path.join(val_path,f))
# %%
