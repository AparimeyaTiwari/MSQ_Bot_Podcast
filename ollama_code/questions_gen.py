from ollama import chat, ChatResponse

def question_generator(response_array,combined_data):
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
    return response.message.content