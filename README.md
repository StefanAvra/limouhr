# About

    time could also be

    speculating about
    the past

    puzzling over
    the future

    estimating
    the present.

Project by [Sonja Schwarz](https://www.instagram.com/soennecken/)

Code Stefan Avramescu  
Product Design IG:@lenn.gerlach  
2nd Brain IG:@janoschkratz.eu

This project was developed in context of the exhibition "Punkt Punkt Komma Strich” about code and computer languages at the Museum of Literature in Marbach. An algorythm generates a poem describing the current time in poetry instead of numbers. The poem is then printed by a thermal printer as soon as the visitor pushes the button.

## Quick start

-   Setup a Raspberry Pi install. If you need to connect a headless setup to wifi you can use `wpa_supplicant.conf` but by now there should be an official, more convenient way for headless setup.
-   Clone repo to `/home/pi`
-   Create a venv called `venv` and activate it
-   Install requirements
-   Connect a button to GPIO 26
-   Setup your thermal printer. The script will assume `/dev/usb/lp0` is your printer, change that if necessary.
-   Use `start.sh` in a cron job to start on boot.



https://user-images.githubusercontent.com/18117169/165856843-511135e4-7010-40a1-b017-a97387726f0c.mp4


![photo_back](https://user-images.githubusercontent.com/18117169/165856765-4133200b-526b-49f5-ada6-941876047fd8.jpg)


## FAQ

_Q: Why is this not an installable package?_

A: Had to hack this too quick to actually structure it properly. Not really a problem since this was never supposed to be released. Feel free to improve and contribute.

_Q: What printer should I use?_

A: We used an old Epson TM-T88 IV via USB.

_Q: What is OCRB Regular.ttf?_

A: The font we used. It's not included because of licensing.

_Q: Has anyone actually asked one of these questions?_

A: No but I realised I never wrote a readme so I thought maybe someone will see this and be happy to have like a bit of guidance.
