import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import wifi_qrcode_generator.generator

print("Generate a network QR code...\n")

Net_Name = input("Input ssid: ")
Net_Pass = input("Input pass: ")

# Generate the base Image
calOre_img = Image.open('Assets\\cal_ore_logo.jpg', 'r')
calOre_img_w, calOre_img_h = calOre_img.size
background = PIL.Image.new(mode="RGB", size=(2700, 3600), color=(255, 255, 255))
bg_w, bg_h = background.size
offset = ((bg_w - calOre_img_w) // 2, (bg_h - (calOre_img_h - 2500)) //2)

background.paste(calOre_img, offset)
background.save("Assets\\Base_Image.png")

# Generate the QR code
qr_code = wifi_qrcode_generator.generator.wifi_qrcode(
    ssid=Net_Name, hidden=False, authentication_type='WPA', password=Net_Pass
)

#qr_code.print_ascii()
qr_code.make_image().save('Assets\\QR_Net_Info.png')

# Resize the QR code
img = Image.open('Assets\\QR_Net_Info.png')
new_img = img.resize((1350,1350))
new_img.save("Assets\\QR_Net_Info.png", "PNG", optimize=True)

# QR to base image
QR_img = Image.open('Assets\\QR_Net_Info.png', 'r')
qr_img_w, qr_img_h = QR_img.size
background = PIL.Image.open('Assets\\Base_Image.png')
bg_w, bg_h = background.size
offset = ((bg_w - qr_img_w) // 2, (bg_h - (qr_img_h) - 900) // 2)
background.paste(QR_img, offset)
draw = ImageDraw.Draw(background)
font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 100)
draw.text(((bg_w / 2) - 500, (bg_h / 2) + 500),f"Name: {Net_Name}\n\nPassword: {Net_Pass}",(0,0,0),font=font)
background.save("Assets\\Final_Image.png")