from pytube import YouTube

link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)

print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)


stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

print("Downloading...")
stream.download()
print("Download completed!!")