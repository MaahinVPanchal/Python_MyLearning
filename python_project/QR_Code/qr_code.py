import qrcode as qr
img = qr.make("https://www.youtube.com/results?search_query=python+project+")
img.save("Project_1_QRcode.png")