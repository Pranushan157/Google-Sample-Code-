"""A video player class."""

from .video_library import VideoLibrary
import random 

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.vid_title = ""
        self.vid_status = ""
        self.vid_playlists = []
        self.vid_dictionary = {} 

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        array = self._video_library.get_all_videos()
        listofvids = []
        x = 0
        while x<len(array):
            title = array[x].title
            vid_id = array[x].video_id
            tag = array[x].tags
            if tag == ():
                tags = ""
                vid = (title + " (" + vid_id + ") " + "[" + tags + "]")
                listofvids.append(vid)
            else:
                tag1 = array[x].tags[0]
                tag2 = array[x].tags[1]
                vid = title + " (" + vid_id + ") " + "[" + tag1 +" "+ tag2 + "]"
                listofvids.append(vid)
            x = x + 1

        listofvids.sort()

        print("Here's a list of all available videos:")
        y = 0
        while y < len(listofvids):
            print(listofvids[y])
            y = y + 1

    def play_video(self, video_id):
        """Plays the respective video.
        
        Args:
            video_id: The video_id to be played.
        """
        checktitle = self._video_library.get_video(video_id)
        if checktitle == None:
            print("Cannot play video: Video does not exist")
            self.vid_status = "Pause"
        if checktitle != None and self.vid_title == "":
            self.vid_title = checktitle.title
            print("Playing video: "+ self.vid_title)
            self.vid_status = "Play"
        elif checktitle != None and self.vid_title != "":
            print("Stopping video: "+ self.vid_title)
            self.vid_title = checktitle.title
            self.vid_status = "Play"
            print("Playing video: "+ self.vid_title)

        
        

    def stop_video(self):
        """Stops the current video."""
        if self.vid_title == "":
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping video: " + self.vid_title)
            self.vid_title = ""
            self.vid_status = "Pause"


    def play_random_video(self):
        """Plays a random video from the video library."""

        if self.vid_title != "":
            print("Stopping video: "+ self.vid_title)

        allvideos = self._video_library.get_all_videos()
        randomnumber = random.randint(0,len(allvideos)-1)
        self.vid_title = allvideos[randomnumber].title
        self.vid_status = "Play"
        print("Playing video: "+ self.vid_title)


    def pause_video(self):
        """Pauses the current video."""
        if self.vid_title != "" and self.vid_status == "Play":
            print("Pausing video: "+self.vid_title)
            self.vid_status = "Pause"
        elif self.vid_title == "":
            print("Cannot pause video: No video is currently playing")
        elif self.vid_status == "Pause":
            print("Video already paused: "+self.vid_title)

    def continue_video(self):
        """Resumes playing the current video."""
        if self.vid_title != "" and self.vid_status == "Pause":
            print("Continuing video: "+self.vid_title)
            self.vid_status = "Play"
        elif self.vid_title != "" and self.vid_status == "Play":
            print("Cannot continue video: Video is not paused")
        else:
            print("Cannot continue video: No video is currently playing")
        

    def show_playing(self):
        """Displays video currently playing."""
        if self.vid_title != "" and self.vid_status == "Play":
            videos = self._video_library.get_all_videos()
            for i in range(len(videos)):
                if videos[i].title == self.vid_title:
                    vid_id = videos[i].video_id
                    tags = videos[i].tags
                    if tags == ():
                        tag = ""
                        print("Currently playing: "+ self.vid_title+ " (" + vid_id + ") " + "[" + tag + "]")
                    else:
                        tag1 = videos[i].tags[0]
                        tag2 = videos[i].tags[1]
                        print("Currently playing: "+ self.vid_title+ " (" + vid_id + ") " + "[" + tag1 +" "+ tag2 + "]")
        elif self.vid_title != "" and self.vid_status == "Pause":
            videos = self._video_library.get_all_videos()
            for i in range(len(videos)):
                if videos[i].title == self.vid_title:
                    vid_id = videos[i].video_id
                    tags = videos[i].tags
                    if tags == ():
                        tag = ""
                        print("Currently playing: "+ self.vid_title+ " (" + vid_id + ") " + "[" + tag + "] - PAUSED")
                    else:
                        tag1 = videos[i].tags[0]
                        tag2 = videos[i].tags[1]
                        print("Currently playing: "+ self.vid_title+ " (" + vid_id + ") " + "[" + tag1 +" "+ tag2 + "] - PAUSED")
        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.
        
        Args:
            playlist_name: The playlist name.
        """
        condition = False
        playlist_name.replace(" ","")

        for i in range(len(self.vid_playlists)):
            if playlist_name.lower() == self.vid_playlists[i].lower():
                print("Cannot create playlist: A playlist with the same name already exists")
                condition = True
        if condition != True:
            self.vid_playlists.append(playlist_name)
            print("Successfully created new playlist: "+ playlist_name)
            self.vid_dictionary[playlist_name.lower()] = list() 

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.
        
        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        videos = self._video_library.get_all_videos()
        vid_title = ""
        found = False
        for x in range(len(videos)):
            if videos[x].video_id == video_id:
                found = True
                vid_title = videos[x].title
        
        found1 = False
        for y in range(len(self.vid_playlists)):
            if self.vid_playlists[y].lower() == playlist_name.lower():
                found1 = True 

        
        if found1 == False:
            print("Cannot add video to "+playlist_name+": Playlist does not exist")
        elif found == False: 
            print("Cannot add video to "+playlist_name+": Video does not exist")
        else:
            print("Added video to "+playlist_name+": "+vid_title)
            self.vid_dictionary[playlist_name.lower()].append(vid_title)  


    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
