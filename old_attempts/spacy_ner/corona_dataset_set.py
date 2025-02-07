import pandas as pd
import spacy
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
import scispacy
from spacy.tokens import Doc,DocBin
from spacy.util import filter_spans
import json
from tqdm import tqdm
from spacy import displacy


nlp = spacy.load('en_core_web_lg')
cnt = 0
with open('Corona2.json', 'r') as file:
    data = json.load(file)

train_data = []
for example in data['examples']:
    ent_dict = {}
    ent_dict['text'] = example['content'] 
    ent_dict['entities'] = []
    for annotation in example['annotations']:
        start = annotation['start']
        end = annotation['end']
        label = annotation['tag_name'].upper()
        ent_dict['entities'].append((start,end,label))
    train_data.append(ent_dict)


nlp = spacy.blank('en') #creating an empty spacy model
doc_bin = DocBin() #binary format to store model on disk


for train_doc in tqdm(train_data): #wrap training data in tqdm
    text = train_doc['text'] #text part
    labels = train_doc['entities'] #label part
    doc = nlp.make_doc(text) #intialise doc object
    ent = [] #used to store entities 
    for start,end,label in labels:
        span = doc.char_span(start,end,label=label,alignment_mode='contract')
        if span is None:
            print("No span found!!!")
        else:
            ent.append(span)
    final_ent = filter_spans(ent) #remove duplicate entries
    doc.ents = final_ent
    doc_bin.add(doc)

doc_bin.to_disk('custom_ner.spacy')

