import shutil
import os

def save_to_react(audio_fp,audio_mp3_fp, json_fp):
    base_dest_path_audio = r'C:\Users\pc\Desktop\AvatarLipSyncReact\libsync_fe\public\audios'
    base_dest_path_json = r'C:\Users\pc\Desktop\AvatarLipSyncReact\libsync_fe\public\audios'

    try:
        shutil.copy2(audio_fp, base_dest_path_audio)
        print(f"File moved to {base_dest_path_audio}")
    except Exception as e:
        print(f"Error occurred: {e}")
    
    try:
        shutil.copy2(json_fp, base_dest_path_json)
        print(f"File moved to {base_dest_path_json}")
    except Exception as e:
        print(f"Error occurred: {e}")


    try:
        shutil.copy2(audio_mp3_fp, base_dest_path_json)
        print(f"File moved to {base_dest_path_json}")
    except Exception as e:
        print(f"Error occurred: {e}")
    
