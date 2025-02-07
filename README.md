AI driven podcast question generator

-> In order to run this code locally on your pc or workstation you will need
a)Ollama setup and ready to use
b)llama3 model downloaded
c)virtual enviornment
d)dependencies mentioned in requirments.txt

->How to load models into Ollama?
Simply run the command: Ollama create "model_name" -f file name

I have used the names:
a)podcast_model for file-> question_generation_model
b)my_sum_model for file-> chunk_theme_model
c)theme_final_model for file-> final_theme_model
d)custom_ner_model for file->ner_model

Run the command mentioned on line 10 4 times accordingly

To launch the webpage, simply run the command

python3 app.py

In the virutal environment
