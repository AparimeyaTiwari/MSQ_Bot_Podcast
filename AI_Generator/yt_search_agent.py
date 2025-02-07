from youtube_transcript_api import YouTubeTranscriptApi as yta
from ollama import chat
from ollama import ChatResponse
import ollama
from fpdf import FPDF
import pymupdf
from my_package.resume_parse import *
from my_package.text_ner import ner_generator
from my_package.questions_gen import question_generator
from my_package.theme_generation import theme
from pathlib import Path


def convert(input,name):
    class PDF(FPDF):
        def header(self):
            self.set_font('Helvetica','BI',30)
            self.cell(0,10,f'{name.upper()}',ln=1,align = 'C')
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
    pdf.output(os.path.join(os.path.expanduser('~'),'Downloads','MSQ_BOT_PODCAST','flask_code','static',f'{name}.pdf'))