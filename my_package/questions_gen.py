from ollama import chat, ChatResponse

def question_generator(combined_data):
    #taking in all the input and generating output questions
    #combined_data.append(response.message.content)
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
    questions = response.message.content
    return questions