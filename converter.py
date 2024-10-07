import pyttsx3
from pydub import AudioSegment
import os
from rhubarb import run_rhubarb
from dir_saving import save_to_react

def text_to_ogg(text,dialogue_file_name, output_filename,output_filename_mp3 ):
    # Initialize the TTS engine
    curr_dir = os.getcwd()
    dialogue_file_name = rf'dialogues\{dialogue_file_name}'

    with open(dialogue_file_name, 'w', encoding='utf-8') as file:
        file.write(text)  # Write the content to the file

    output_filename = rf'{curr_dir}\audio_gen\{output_filename}'
    print(output_filename)
    engine = pyttsx3.init()

    # Set properties
    engine.setProperty('rate', 150)  # Speed
    engine.setProperty('volume', 1)  # Volume

    # Get available voices
    voices = engine.getProperty('voices')

    # Set male voice (first male voice found)
    for voice in voices:
        if 'male' in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break

    # Save speech to a temporary WAV file
    temp_wav_file = "temp.wav"
    engine.save_to_file(text, temp_wav_file)
    engine.runAndWait()

    # Convert WAV to OGG using pydub
    sound = AudioSegment.from_wav(temp_wav_file)
    sound.export(output_filename, format="ogg")  # Save as OGG format
    sound.export(output_filename_mp3, format="mp3")  # 


    # Clean up temporary WAV file
    os.remove(temp_wav_file)
    print(f"Audio saved as {output_filename}")

    # Example usage
    output_json_path = rf'{curr_dir}\response.json'
    print(f'Output for JSON file Processed: {output_json_path}')
    run_rhubarb(
    input_file=output_filename,           # Path to your input WAV file
    dialog_file=rf'{curr_dir}\{dialogue_file_name}',         # Path to your dialog file
    output_file= output_json_path         # Desired output file
    )

    os.chdir(curr_dir)

    #now we are going to save the ogg file and json file to the react directory
    save_to_react(audio_fp=output_filename, json_fp=output_json_path, audio_mp3_fp=output_filename_mp3)
    print('Successfully moved the audio and the json file to the react directory')

    # with open(output_json_path, 'r') as file:
    #     data = json.load(file)
    # print(data)
    # return data


# # Example usage:
# text = "Hello, this is a sample text being converted to a male voice in OGG format."
# text_to_ogg(text, 'text_1.txt',"male_voice_output.ogg")
