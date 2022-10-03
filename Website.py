import qrcode

#QRCode class which can control physical properties of the actual image 
qr = qrcode.QRCode(version = 1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size = 10, border = 2)

#Link that gets put in QRCode format
Link = "www.google.com"
qr.add_data(Link)
qr.make(fit=True)

#Assign color and background of the actual QRCode image
img = qr.make_image(fill_color="black", back_color="white")
#Save the image in local folder
img.save("QRCode.png")

