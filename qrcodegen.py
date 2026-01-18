import qrcode as qr
img = qr.make("https://www.youtube.com/watch?v=vObyE_OR8Aw&list=RDvObyE_OR8Aw&start_radio=1")
img.save("song1.png")