from PIL import Image, ImageDraw, ImageFont
image = Image.open('your_image.jpg')
draw = ImageDraw.Draw(image)
fonts = [
    ImageFont.truetype("arial.ttf", size=40),
    ImageFont.truetype("arial.ttf", size=60),
    ImageFont.truetype("arial.ttf", size=80)
]
colors = ["white", "yellow", "red", "blue"]
texts = ["Top Left", "Center", "Bottom Right", "Random Spot"]
positions = [(10, 10), (image.width // 2, image.height // 2), (image.width - 200, image.height - 100), (150, 300)]
for i, (text, pos) in enumerate(zip(texts, positions)):
        draw.text(pos, text, font=fonts[i % len(fonts)], fill=colors[i % len(colors)])
image.show()
