from youtube_transcript_api import YouTubeTranscriptApi as yta
from ollama import chat
from ollama import ChatResponse
import ollama
from fpdf import FPDF
import pymupdf
from ollama_code.resume_parse import *
from ollama_code.text_ner import ner_generator
from ollama_code.questions_gen import question_generator
from theme_generation import theme


'''combined_data = [] #used to store all data which is to be feed into our final model

# Reading file data and convertint to ner json
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


# Extracting data about theme from reference youtube video
link = input("Enter podcast link ")
id = link[32:len(link)]
data = yta.get_transcript(str(id))
total_count = len(data)

response_array = []
cnt = 0
op = ""
quotient = total_count//5
remainder = total_count%5
print("total_count: ", total_count)
print(quotient)
print(remainder)

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
    final_op += "\n\n"

response : ChatResponse = chat(model="theme_final_model",messages = [
            {
                'role':'user',
                'content':f"{final_op}",
            },
])

#taking in all the input and generating output questions
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

'''

def convert(input,guest):
    class PDF(FPDF):
        def header(self):
            self.set_font('times','BI',30)
            self.cell(0,10,f'{guest} QUESTIONS',ln=1,align = 'C')
            self.ln(10)

        def footer(self):
            self.set_y(-10)
            self.set_font('times','I',10)
            self.cell(0,10,f'Page: {self.page_no()}',align='C')

        def add_chapter(self,txt):
            self.set_font('times','',14)
            self.multi_cell(0,5,txt)
            self.ln(2)


    pdf =PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto = True, margin=10)
    pdf.add_chapter(input)
    pdf.output(f'{guest}')
    print("PDF READY TO VIEW!!")