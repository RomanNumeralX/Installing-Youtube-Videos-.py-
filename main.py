import pytube
from pytube import YouTube
import time


save_path = "C:\\Users\\User\\Videos\\" #Use your own path to save the videos to, if you wish.
list = []
finisher = ""

def installer():
    if len(list) > 0:
        print(list, " Here is the list I will be iterating over.")
        time.sleep(2)
        for url_in_list in list:
            video_url = url_in_list
            yt = YouTube(video_url)
            stream = yt.streams.get_highest_resolution()
            installed_video = stream.download(save_path)
            print("Video downloaded successfully!")
            print(f"Video's name : {installed_video.title}")
            
    else:
        print("No video URLs found.")
    
    print("Process completed. All video(s) have been installed.")


while finisher != "stop":
    
    url = input("URL : ")
    
    if url == "stop":
        print("Process completed.")
        time.sleep(2)
        finisher = "stop"
        break
    
    elif url == "begin":
        installer()
        time.sleep(2)
        break
    
    else:
        list.append(url)
        print("URL successfully added.")


print("All processes have been completed.")
time.sleep(2)
