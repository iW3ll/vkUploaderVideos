import vk_api
from vk_api import VkUpload

# Your VK.com login and password
LOGIN = ''
PASSWORD = ''

# Read video file paths from a text file
video_file_path = r'' #put path to file here
with open(video_file_path, 'r') as file:
    video_files = file.readlines()
video_files = [video_file.strip() for video_file in video_files]

# Initialize VK API
vk_session = vk_api.VkApi(LOGIN, PASSWORD)
vk_session.auth()
vk = vk_session.get_api()
upload = VkUpload(vk)

# Upload videos
for video_file in video_files:
    # Upload video
    video = upload.video(video_file=video_file, is_private=1) #if 0 = public
    
    # Print URL of the uploaded video
    print('Video URL:', video['video']['player'])