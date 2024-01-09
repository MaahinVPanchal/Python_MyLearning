import qrcode
from PIL import Image

qr = qrcode.QRCode(version = 1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size = 10, 
                   border = 4,)
qr.add_data("https://www.pxfuel.com/en/desktop-wallpaper-okiyc")
qr.make(fit=True)
img =  qr.make_image(fill_color = "green",
                     back_color = "black")
img.save("E://LenovoEdrive/Python-Programming/python_project/QR_Code/Project_2_QRcode.png")