from youtube_transcript_api import YouTubeTranscriptApi as yta
from ollama import chat
from ollama import ChatResponse
import ollama
from fpdf import FPDF
import pymupdf
from AI_Generator.resume_parse import *
from AI_Generator.text_ner import ner_generator
from AI_Generator.questions_gen import question_generator
from AI_Generator.theme_generation import theme
from pathlib import Path
import os

def convert(input,name):
    class PDF(FPDF):
        def header(self):
            self.set_font("DejaVuSans","",30)
            self.cell(0,10,f'{name.upper()}',ln=1,align = 'C')
            self.ln(10)

        def footer(self):
            self.set_y(-10)
            self.set_font('times','I',10)
            self.cell(0,10,f'Page: {self.page_no()}',align='C')

        def add_chapter(self,txt):
            self.set_font('DejaVuSans','',14)
            self.multi_cell(0,5,txt)
            self.ln(2)


    pdf =PDF()
    path_font = os.path.join(os.path.dirname(__file__),"DejaVuSans.ttf")
    pdf.add_font("DejaVuSans","",path_font,uni=True)
    pdf.add_page()
    pdf.set_auto_page_break(auto = True, margin=10)
    pdf.add_chapter(input)
    pdf.output(os.path.join(os.path.expanduser('~'),'Downloads','MSQ_BOT_PODCAST','flask_code','static',f'{name}.pdf'))