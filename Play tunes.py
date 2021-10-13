import vlc
p = vlc.MediaPlayer("HappyBirthDay.mp3")
p.play()
while True:
    a = input("Press 's' to stop Tune or 'p' to play song again or 'e' to exit the player    ")
    if a == "s" :
        p.stop()
    elif a == "p":
        p.play()
    elif a == "e":
        exit()