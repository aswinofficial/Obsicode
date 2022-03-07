import qrcode

txt = input("Enter what to be encoded : ")
img = qrcode.make(txt)
img.save("Qrcode.png")