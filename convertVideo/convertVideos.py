import moviepy.editor as moviepy
import os

pathIn = 'InputVideos'
pathOut = 'OutputVideos'

fileList = os.listdir(pathIn)
print("Number of Videos:",len(fileList))
print(fileList)

for x,file in enumerate(fileList):
    print(os.path.basename(file))
    clip = moviepy.VideoFileClip(f'{pathIn}/{os.path.basename(file)}')
    clip.write_videofile(f'{pathOut}/{os.path.basename(file)}', bitrate="12000k")
