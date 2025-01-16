import ollama

with open('/Users/aparimeyatiwari/Downloads/MSQ_Bot_Podcast/open_ai/output_resume1.txt','r') as file:
    data = file.read()

response = ollama.chat(model='phi',messages= [{
    'role':'user',
    'content':f'{data}, extract education details from the given data please'
    },
])

print(response['message']['content'])