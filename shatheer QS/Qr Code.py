"""# Importing 
import qrcode

# Data to encode
data = "https://www.linkedin.com/in/mohammad-saatheer-82803867/"

# Creating an instance of QRCode class
qr = qrcode.QRCode(version = 1,
                   box_size = 10,
                   border = 5)

# Adding data to the instance 'qr'
qr.add_data(data)

qr.make(fit = True)
img = qr.make_image(fill_color = '#0077B5',
                    back_color = 'white')

img.save('MyQRCode2.png')"""


import qrcode
from PIL import Image

# Your LinkedIn profile URL
data = "https://www.linkedin.com/in/mohammad-saatheer-82803867/"  # Change to your actual profile URL

# Generate QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

# Customize QR code colors
qr_img = qr.make_image(fill_color="#0077B5", back_color=None).convert('RGB')

# Load LinkedIn logo
logo = Image.open('circle-linkedin-1024.png')

# Calculate size for the logo
qr_width, qr_height = qr_img.size
logo_size = qr_width // 4  # 25% of the QR code size

# Resize logo
logo = logo.resize((logo_size, logo_size))

# Calculate position for the logo
pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

# Paste logo into QR code
qr_img.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)

# Save and show
qr_img.save("LinkedInQRCode.png")
qr_img.show()
