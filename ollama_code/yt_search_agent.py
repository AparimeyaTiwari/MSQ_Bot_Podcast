from youtube_transcript_api import YouTubeTranscriptApi as yta
from ollama import chat
from ollama import ChatResponse
import ollama


combined_data = []

with open('/Users/aparimeyatiwari/Downloads/MSQ_Bot_Podcast/ollama_code/output_resume1.txt','r') as file:
    data = file.read()


response : ChatResponse = chat(model='custom_ner_model',messages= [ #response is an object/instance of ChatResponse class
    {
    'role':'user',
    'content': f'{data}'
    },
]
)
combined_data.append(response.message.content)



link = input("Enter podcast link ")
id = link[32:len(link)]
data = yta.get_transcript(str(id))
total_count = len(data)

response_array = []
cnt = 0
op = ""
quotient = total_count//5
remainder = total_count%5
'''print("total_count: ", total_count)
print(quotient)
print(remainder)'''

for i in data:
    op += "".join(i['text'])
    op += " "
    cnt += 1
    if(cnt % quotient == 0 and total_count - cnt != remainder):
        print("RESEARCHING")
        response : ChatResponse = chat(model="my_sum_model",messages = [
            {
                'role':'user',
                'content':f"{op}",
            },
        ])
        response_array.append(response.message.content)
        op = " "
    if(total_count - cnt == remainder):
        break

final_op = ""
for j in response_array:
    final_op += j
    final_op += " "

response : ChatResponse = chat(model="theme_final_model",messages = [
            {
                'role':'user',
                'content':f"{final_op}",
            },
])


combined_data.append(response.message.content)
final_input = ""
final_input += (combined_data[0])
final_input += " Theme input: "
final_input += (combined_data[1])
response : ChatResponse = chat(model="podcast_model",messages = [
    {
        'role':'user',
        'content':f"{final_input}"
    }
])

with open("question_pdf.text",'w') as file:
    file.write(response.message.content)
print("PDF READY TO VIEW!!")