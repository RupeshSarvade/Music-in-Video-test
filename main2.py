import moviepy.editor as mpe

video = mpe.VideoFileClip('data/3.mp4').subclip(0,15).without_audio() #import video

audio_bg = mpe.AudioFileClip("data/audio.mp3") #import audio
# final_audio = mpe.CompositeAudioClip([audio_bg, video.audio])
final_clip = video.set_audio(audio_bg) # combine them
final_clip.write_videofile("output.mp4") #save output
