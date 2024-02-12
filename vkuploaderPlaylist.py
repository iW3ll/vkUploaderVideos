import vk_api
from vk_api import VkUpload
import os

LOGIN = ''
PASSWORD = ''

video_directory = r''  

playlist_id = 1 


vk_session = vk_api.VkApi(LOGIN, PASSWORD)
vk_session.auth()
vk = vk_session.get_api()
upload = VkUpload(vk)


video_files = [f for f in os.listdir(video_directory) if f.endswith(('.mp4', '.avi', '.mov'))]


for video_file in video_files:
    video_title = os.path.splitext(video_file)[0]  
    
    video = upload.video(os.path.join(video_directory, video_file), is_private=0, name=video_title, album_id=playlist_id)
    
    
    video_owner_id = video['owner_id']
    video_id = video['video_id']
    video_url = f"https://vk.com/video{video_owner_id}_{video_id}"
    print(f'Uploaded Video: {video_title} - URL: {video_url}')