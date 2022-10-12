import qrcode

inputUser = input("Please enter the url for generate the qr: ")

qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(inputUser)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save('qr.png')

print(img)

