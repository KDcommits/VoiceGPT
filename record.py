import pyaudio
import wave

def record_audio(filename, duration):
    try:
        chunk = 1024  # Buffer size
        format = pyaudio.paInt16  # Audio format
        channels = 2  # Stereo
        sample_rate = 44100  # Sample rate (Hz)
        record_seconds = duration

        p = pyaudio.PyAudio()

        stream = p.open(format=format,
                        channels=channels,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=chunk)

        print("Recording audio...")

        frames = []

        for i in range(0, int(sample_rate / chunk * record_seconds)):
            data = stream.read(chunk)
            frames.append(data)

        print("Finished recording.")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wavefile = wave.open(filename, 'wb')
        wavefile.setnchannels(channels)
        wavefile.setsampwidth(p.get_sample_size(format))
        wavefile.setframerate(sample_rate)
        wavefile.writeframes(b''.join(frames))
        wavefile.close()

        print(f"Audio saved as {filename}")

    except:
        print("Error! check 'record_audio' function")


# audio_filename = "Stored Data/Input/Input Audio/recorded_audio.wav"
# recording_duration = 5  
# record_audio(audio_filename, recording_duration)