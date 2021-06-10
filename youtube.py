from pytube import YouTube
import time

class YoutubeVideo(YouTube):
    previous_progress = 0
    downloading_video = False
    progressBar = None

    def downloadVideo(self, quality, path):
        self.previous_progress = 0

        #Extract itag
        select_video = self.streams.filter(resolution=quality, progressive=True)

        start = str(select_video).find("\"")
        end = str(select_video).find("mime_type")
        itag = str(select_video)[start+1 :end-2]
        itag = int(itag)

        #download
        self.register_on_progress_callback(self.calculateDownloadProgress)
        self.stream = self.streams.get_by_itag(itag)
        self.stream.download(path)
        
    def receiveProgressBar(self, progressBar):
        #we use this for update the progress bar value 
        self.progressBar = progressBar

    def calculateDownloadProgress(self, stream, chunk, bytes_remaining):
        size = stream.filesize
        bytes_downloaded = size - bytes_remaining

        live_progress = int(bytes_downloaded/size * 100)

        if live_progress == 100:
            self.progressBar.setValue(100)
            time.sleep(3)
            
            #restart progress var
            self.progressBar.setValue(0)
            return 0;

        if live_progress > self.previous_progress:
            self.previous_progress = live_progress

            #update progress bar
            self.progressBar.setValue(live_progress)
        



        
        