from ollama import chat #ollama->library and chat->function to interact with llm
from ollama import ChatResponse #ChatResponse->class
import ollama

def ner_generator(file,array):    
    with open(file,'r') as file:
        data = file.read()


    response : ChatResponse = chat(model='custom_ner_model',messages= [ #response is an object/instance of ChatResponse class
        {
        'role':'user',
        'content': f'{data}'
        },
    ]
    )
    array.append(response.message.content)
    return array

ner_generator('/Users/aparimeyatiwari/Downloads/MSQ_Bot_Podcast/flask_code/json/richa_resume.txt',[])