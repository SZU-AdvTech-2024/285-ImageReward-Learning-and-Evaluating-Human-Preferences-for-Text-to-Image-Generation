import os
import json

ex_path = '/raid/maxusen/.cache/huggingface/datasets/downloads/extracted/'

train_json = []
test_json = []
validation_json = []

for split in os.listdir(ex_path):
    if not split.endswith('.lock'):
        split_file = os.path.join(ex_path, split)
        for file in os.listdir(split_file):
            if file.endswith('.json'):
                with open(split_file + '/' + file, 'r', encoding='utf-8') as f:
                    jf = json.load(f)
                    pid = jf[0]['prompt_id']
                    prompt = jf[0]['prompt']
                    generations = []
                    ranking = []
                    meta = {}
                    i = 0
                    for ti in jf:
                        i = i + 1
                        if pid != ti['prompt_id'] or i == len(jf):
                            meta['id'] = pid
                            meta['prompt'] = prompt
                            if i == len(jf):
                                file_size_KB = os.path.getsize(split_file + '/' + os.path.basename(ti['image_path'])) / 1024
                                if file_size_KB >= 100:
                                    generations.append(split_file + '/' + os.path.basename(ti['image_path']))
                                    ranking.append(ti['rank'])
                            meta['generations'] = generations
                            meta['ranking'] = ranking
                            if file.find('train') != -1:
                                train_json.append(meta)
                            if file.find('test') != -1:
                                test_json.append(meta)
                            if file.find('validation') != -1:
                                validation_json.append(meta)
                            pid = ti['prompt_id']
                            prompt = ti['prompt']
                            generations = []
                            ranking = []
                            meta = {}
                        file_size_KB = os.path.getsize(split_file + '/' + os.path.basename(ti['image_path'])) / 1024
                        if file_size_KB >= 100:
                            generations.append(split_file + '/' + os.path.basename(ti['image_path']))
                            ranking.append(ti['rank'])
                break
json_string0 = json.dumps(train_json, indent=4)
with open('/raid/maxusen/ImageReward/train/dataset/train.json', 'w') as f0:
    f0.write(json_string0)

json_string1 = json.dumps(test_json, indent=4)
with open('/raid/maxusen/ImageReward/train/dataset/test.json', 'w') as f1:
    f1.write(json_string1)

json_string2 = json.dumps(validation_json, indent=4)
with open('/raid/maxusen/ImageReward/train/dataset/validation.json', 'w') as f2:
    f2.write(json_string2)

