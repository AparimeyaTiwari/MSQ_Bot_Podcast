from ollama import chat, ChatResponse

def question_generator(combined_data,topics,imp):
    #taking in all the input and generating output questions
    #combined_data.append(response.message.content)
    final_input = "JSON Ner:  "
    final_input += (combined_data[0])
    final_input += "\nTheme input: "
    final_input += (combined_data[1])
    final_input += "\nTopics to cover: "
    final_input += topics
    final_input += "\nImportant topics: "
    final_input += imp

    response : ChatResponse = chat(model="podcast_model",messages = [
        {
            'role':'user',
            'content':f"{final_input}"
        }
    ])
    questions = response.message.content
    return questions