from PIL import Image, ImageDraw


def create_image_from_frame(frame_as_string):
    image = Image.new('RGB', (610, 850), color=(0, 0, 0))
    drawing = ImageDraw.Draw(image)
    drawing.text((0, 0), frame_as_string, fill=(255, 255, 255))
    
    return image
