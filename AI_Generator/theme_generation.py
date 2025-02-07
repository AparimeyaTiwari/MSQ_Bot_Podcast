import ollama
from ollama import chat,ChatResponse
from youtube_transcript_api import YouTubeTranscriptApi as yta

def theme(link,array):
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
        final_op += "\n\n"

    response : ChatResponse = chat(model="theme_final_model",messages = [
                {
                    'role':'user',
                    'content':f"{final_op}",
                },
    ])
    array.append(response.message.content)
    return array