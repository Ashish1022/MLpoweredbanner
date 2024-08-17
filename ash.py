from PIL import Image
import os
import cv2

def add_image():
    card = os.listdir('C:\\Users\\91932\\Desktop\\Python\\banner\\finalCard')
    # card_objects = [os.listdir(f'finalCard/{filename}') for filename in card]
    print(card)
    # len_card_objects = len(card_objects)

    photos = os.listdir('C:\\Users\\91932\\Desktop\\Python\\banner\\photos')
    # photos_objects = [os.listdir(f'photos/{filename}') for filename in photos]
    print(photos)
    # len_photos_objects = len(photos_objects)

    for i in card:
        for j in photos:
            if(i == j):
                card = Image.open(f'C:\\Users\\91932\\Desktop\\Python\\banner\\finalCard\\{i}')
                img = Image.open(f'C:\\Users\\91932\\Desktop\\Python\\banner\\photos\\{j}')
                Image.Image.paste(card, img, (50,50))
                card.save(f'test/{i}')
                # card.save('test/img.png')
                # card.show()
add_image()
