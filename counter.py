import os 
import re

def generateResponse(transcription_filepath, path):
    try:
        transcription_filename = os.path.join(transcription_filepath, "input_audio_transcription.txt")
        with open(transcription_filename) as f:
            user_input = "".join(f.readlines())
        print(user_input)

        textfiles = os.listdir(path)
        if len(textfiles)!=0:
            os.remove(os.path.join(path,textfiles[0]))

        final_user_input = re.sub(r'[^\w\s]','',user_input)
        word_count = len(final_user_input.split(' '))
        bot_response = f"Input audio contains '{word_count}' words." 

        response_filename = os.path.join(path,'response.txt')
        with open(response_filename, 'a') as f_write:
            f_write.write(bot_response)

        f.close()
        f_write.close()
        return bot_response
    except:
        print("Error ! check 'generateResponse'")