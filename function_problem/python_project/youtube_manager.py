
import json
videos =[]

def load_data():
    try:
        with open("youtube.txt","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def data_saver_helper(videos):
    with open("youtube.text","w") as file:
        json.dump(videos,file)

def list_all_video(videos):
    for index , video in enumerate(videos,start=1):
        print(f"{index}, {video}")
        
       

def add_video(videos):
    name = input("Enter the name of the movie : ")
    time = input("Enter the duration of the movie ")
    videos.append({'name': name , 'time' : time })
    data_saver_helper(videos)
    
   

def update_videos(videos):
    list_all_video(videos)
    index =int(input("Enter the video number to update : "))
    
    
    if index>=1 <= len(videos):
        name= input(" Enter the name of the movie : ")
        time = input("Enter the duration of the movie : ")
       
        videos[index-1]={'name':name , 'duration' : time}
        
        data_saver_helper(videos)  


def delete_videos(videos):
    list_all_video(videos)
    index = int(input("Enter the video number you want delete : "))
    
    if index>=1 <= len(videos):
        del videos[index-1]
        data_saver_helper(videos)
        
        print("video sucessfully deleted ")
        
    else:
        print("Invalid input ")
        
   

def main(): 
    videos = load_data()
         
    while True:
        print(" \n youtube video manager || choose the option \n ")
        print("1. List all youtube videos. ")
        print("2. Add a  youtube videos. ")
        print("3. update a youtube videos. ")
        print("4. Delete a  youtube videos. ")
        print("5.  Exit the app : ")
        
        choice = input("Enter the choice : ")
        
        print(videos)
        
        
        match choice:
            case '1':
                list_all_video(videos)
                
            case '2':
                add_video(videos)
                
            case '3':
                update_videos(videos)
                
            case '4':
                delete_videos(videos)
                
            case '5':
                break
        
            case _:
                print("Invalid number ")
            
            
if __name__== "__main__":
    main()