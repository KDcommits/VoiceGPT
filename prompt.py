import openai 
import os

def generateResponse(transcription_filename, path):
    try:
        with open(transcription_filename) as f:
            user_input = "".join(f.readlines())
        print(user_input)

        ### Setting OpenAI environment
        response = openai.ChatCompletion.create(
                            model="gpt-3.5-turbo",
                            messages=[
                                {"role": "system", "content":"You are a helpful assistant."},
                                {"role": "user", "content": user_input},
                            ],
                            temperature=0.5,
                            max_tokens=150,
                            top_p=1,
                            frequency_penalty=0,
                            presence_penalty=0,
                            n=1,
                            stop=["\nUser:"],
                        )
        bot_response = response["choices"][0]["message"]["content"]
        print(bot_response)
        # append text to response file
        path = '.\\Stored Data\\Output\\GPT Response\\'
        textfiles = os.listdir(path)
        if len(textfiles)!=0:
            os.remove(os.path.join(path,textfiles[0]))

        response_filename = 'Stored Data/Output/GPT Response/openai_response.txt'
        with open(response_filename, 'a') as f_write:
            f_write.write(bot_response)

        f.close()
        f_write.close()
        return bot_response
    
    except:
        print("Error ! check 'generateResponse'")

# transcription_filename = 'C:\\Users\\krish\\OneDrive\\Desktop\\Study\\Gen AI\\Voice GPT\\Stored Data\\Input\\Transcription\\input_audio_transcription.txt'
# result = generateResponse(transcription_filename)
# print(result)



