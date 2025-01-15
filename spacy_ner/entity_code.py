import pandas as pd
import spacy
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
import scispacy
import spacy.displacy
from spacy.tokens import Doc,DocBin
from spacy.util import filter_spans
import json
from tqdm import tqdm
from spacy import displacy


nlp = spacy.load('en_core_web_lg')
cnt = 0
with open('train_data.json', 'r') as file:
    data = json.load(file)

train_data = []
for i in data:
    ent_dict = {}
    ent_dict['text'] = i[0]
    ent_dict['entities'] = []
    for j in i[1]['entities']:
        start = j[0]
        end = j[1]
        label = j[2]
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
        span = doc.char_span(start, end, label=label, alignment_mode='contract')
        if span is None:
            print('No span found!!!')
        else:
            ent.append(span)
    final_ent = filter_spans(ent) #remove duplicate entries
    doc.ents = final_ent
    doc_bin.add(doc)

doc_bin.to_disk('custom_ner.spacy')



'''
resume_text = """Education
MKSSS's Cummins College of Engineering for Women                                     Pune, Maharashtra
      BTech Electronics and Telecommunication, CGPA: 9.37/10.0                                                        2026
      Honours in Data Science.
MT Balwadkar Jr College                                                                                           Pune, Maharashtra
      12th Class - HSC, Score: 80.7%                                                                                                             2022
Akshara International School                                                                                  Pune, Maharashtra
      10th Class - CBSE, Score: 94.6%                                                                                                          2020
Projects
 1) Generic File Base Database Management System                                                                    GitHub 
      Created a C program with file handling to create a new C program and to compile it 
      dynamically.  Implemented record creation, reading, and deletion. Utilized CSV files for
      streamlined data management. 
 2) CertiGen - Certificate Generator                                                                                            GitHub
      CertiGen is a web application that generates the award certificates. Developed using 
      Java and HTML / CSS, CertiGen provides an easy-to-use interface to upload SVG template 
      and a CSV data file for generating final certificate images.
 3) Pandas DataFrame in Java                                                                                                     GitHub
     Developed a Java DataFrame library similar to Python's Pandas for tasks like sorting, filtering, 
     and CSV handling, simplifying data analysis for Java developers
 4) Loan Approval Prediction                                                                                                       GitHub
     Made a loan classification model with 98.1% accuracy using SVM, Random Forest, 
      Linear Regression and preprocessing.
Achievements
Secured internship offers from Microsoft and Wells Fargo for Summer 2025.
Competitive Programming
    - Solved 400+ problems on LeetCode.
    - Earned two ‘5 Stars’ badges and certificates in ‘Java’, ‘SQL’, ‘Problem Solving’ & 
       ‘Software Engineer Intern’ on HackerRank.
Teachnook Certification in Web Development                                  IIT Bhubaneshwar - May, 2023
Loop Buffer 4.0 - 1st place in First Year Category                                                       CCOEW, 2023 
Loop Buffer 5.0 - 1st place in Second Year Category                                                  CCOEW, 2024
Mentee at Codess Cafe                                                                                                      June, 2024
Top 5 in E&TC Department
Participated in Hacktoberfest, Code-IT (ACM), Dassault Hackathon, Barclays Hackathon, 
     DSA Craft (Innovation 2024), Vizathon 2.0 (VIIT). 
Programming and Technical Skills
Proficient in: C, Java, Machine Learning, HTML/CSS, JDBC, Tableau & Power BI.
Familiar with: JavaScript, Python, JDBC, SQL.
Upcoming Software Engineering Intern at Microsoft - Summer, 2025.
richa.rathi.2511@gmail.com | richa.rathi@cumminscollege.in | +91 8767603801 | Leetcode | HackerRank
GitHub: https://github.com/RiRa25  | LinkedIn: https://www.linkedin.com/in/richa-rathi-775871257/                         
Richa Rathi
Responsibilities
FiSOC - Finance Club of CCOEW, Pune - Head of PR and Operations Team
     Contributed to organizing the “Trade Trek” event in our college tech fest - “Innovation”
LOOP - DSA Club of CCOEW, Pune - Technical Organiser.                                                                
Ecell Yukta - Entrepreneurship Cell of CCOEW, Pune - Part of the Operations Team
      Headed the "Money Multiplication" game at the "Empulse" entrepreneurial fest.
AICVS - Artificial Intelligence and Computer Vision Society - Part of the PR and Sponsorship
Team                                                                             
"""

output = custom_pod_model(resume_text)
print(spacy.displacy.serve(output,style="ent",port=5500))
'''