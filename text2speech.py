import os
from gtts import gTTS

def synthesize_speech(openai_text_response_path, path):
    try:
        openai_text_response = os.path.join(openai_text_response_path,'response.txt')
        with open(openai_text_response, "r") as f:
            response_text = f.read().replace("\n", " ")

        language = 'en'
        speech_obj = gTTS(text=response_text, lang=language, slow=False) 

        audiofiles = os.listdir(path)
        if len(audiofiles)!=0:
            os.remove(os.path.join(path,audiofiles[0]))

        audio_response_filename = os.path.join(path,'openai_audio_response.wav')
        speech_obj.save(audio_response_filename) 

    except:
        print("Error! check 'synthesize_speech'")

# openai_text_response = 'C:\\Users\\krish\\OneDrive\\Desktop\\Study\\Gen AI\\Voice GPT\\Stored Data\\Output\\GPT Response\\openai_response.txt'
# audio = synthesize_speech(openai_text_response)