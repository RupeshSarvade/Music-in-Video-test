import moviepy.editor as mpe

video = mpe.VideoFileClip('data/3.mp4').subclip(0,15).without_audio()
audio_bg = mpe.AudioFileClip("data/audio.mp3")
# final_audio = mpe.CompositeAudioClip([audio_bg, video.audio])
final_clip = video.set_audio(audio_bg)
final_clip.write_videofile("output.mp4")