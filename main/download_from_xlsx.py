import pandas as pd
import subprocess

finegym_link_xlsx = 'data/finegym_video_links.xlsx'
finegym_dataset_dir = 'data/FineGym'
video_ext_list = ['.mp4', '.mkv', '.webm']

# Read excel file of links for FineGym dataset
finegym_db = pd.read_excel(finegym_link_xlsx)

# Download all files
for each_link in finegym_db['Link']:
    command_download = ['youtube-dl', str(each_link)]
    subprocess.call(command_download)

    # Move the downloaded file to dataset directory
    for each_video_ext in video_ext_list:
        command_move = ['mv', '*'+str(each_video_ext), str(finegym_dataset_dir)]
        subprocess.call(command_move)