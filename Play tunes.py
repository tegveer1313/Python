import vlc
p = vlc.MediaPlayer("SP_Balasubrahmanyam_&_Chitra_live_Sathiya_Ye_Tune_Kya_Kiya_-_साथिया_ये_तूने_क्या_किया_subscribe(256k).mp3")
p.play()
a = input("Press 's' to stope Tune.    ")
if a == "s" :
    p.stop()