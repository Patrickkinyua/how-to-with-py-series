import qrcode

data = "+254720061348"


file_path = "qr.png"

image = qrcode.make(data)

image.save(file_path)

print("qr code saved at qr.png")

