from collections import defaultdict
import json
import pandas as pd


dataset_root = 'datasets/'

category = defaultdict(list)
category['benign'].append('normal')

with open('training_attack_types.txt', 'r') as f:
	for line in f.readlines():
		attack, cat = line.strip().split(' ')
		category[cat].append(attack)

attack_mapping = dict((v,k) for k in category for v in category[k])

json_data = json.dumps(attack_mapping, indent=2)

#Test print data
#print(json_data)

# Set training files
train_file = os.path.join(dataset_root, 'KDDTrain+.txt')
test_file = os.path.join(dataset_root, 'KDDTest+.txt')

# Read training data in
train_df = pd.read_csv(traing_file, names=header_names)
train_df['attack_category'] = train_df['attack_type'].map(lambda x: attack_mapping[x])
train
