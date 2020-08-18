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

    #https://www.tutorialspoint.com/python/os_utime.htm
    # Showing stat information of file
    stinfo = os.stat(f'{pathIn}/{os.path.basename(file)}')
    #print(stinfo)

    # Using os.stat to recieve atime and mtime of file
    #print("access time: " + str(stinfo.st_atime))
    #print("modified time: " +  str(stinfo.st_mtime))

    #https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html
    #clip.write_videofile(f'{pathOut}/{os.path.basename(file)}', codec='mpeg4', bitrate='15000k')  #40 videos in 10 min
    clip.write_videofile(f'{pathOut}/{os.path.basename(file)}') #40 videos in 19 min

    # Modifying atime and mtime of original file
    os.utime(f'{pathOut}/{os.path.basename(file)}', (stinfo.st_mtime, stinfo.st_mtime))
    
    #original 40 Videos: 3,37 GB
    #default 40 Videos: 1,03 GB time: 19 min
    #codec='mpeg4', bitrate='15000k': 2,39 GB time: 10 min
