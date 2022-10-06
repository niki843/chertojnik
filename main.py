import os

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

SPACE_SIZE = 30
NEW_LINE_SIZE = 48
FIRST_PICTURE_FIRST_PIXEL_START_POSITION_Y = 441
FIRST_PICTURE_FIRST_PIXEL_START_POSITION_X = 270
SECOND_PICTURE_FIRST_PIXEL_START_POSITION_X = 1380
NUMBER_IMAGES_SIZE = (25, 35)
LEFT_RIGHT_DIFFERENCE_RATIO = 37
GRAPHICS_AMMOUNT = 6
EMPTY_IMAGE_PATH = "report_fixed_empty.png"
SPACE_SIZE_PAGE = 25

current_graph_location_message = [
    "Таблица намираща се в горен ляв ъгъл",
    "Таблица намираща се в горен десен ъгъл",
    "Таблица намираща се в средата от ляво",
    "Таблица намираща се в средата от дясно",
    "Таблица намираща се в долен ляв ъгъл",
    "Таблица намираща се в долен десен ъгъл"
]

input_messages = ['Въведете Линия 1:',
                  'Въведете Линия 2:',
                  "Въведете цяло число за разстояние:",
                  "Въведете дробна част на разстояние:",
                  "Въведете часове на ъгъл:",
                  "Въведете минути на ъгъл:",
                  "Въведете секунди на ъгъл:"]

# All of the values that are hardcoded are specific values that were used to get the required positions
# no use of creating special variables as they won't be reused or descriptive enough
coordinates_left = {
    # User inserted values coordinates
    '1x': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_X + (SPACE_SIZE * 10),
    '1y': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_Y,
    '2x': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_X + (SPACE_SIZE * 23),
    '2y': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_Y,
    '3x': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_X + (SPACE_SIZE * 19),
    '3y': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_Y + (NEW_LINE_SIZE * 2),
    '4x': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_X + (SPACE_SIZE * 21) + 3,
    '4y': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_Y + (NEW_LINE_SIZE * 2),
    '5x': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_X + (SPACE_SIZE * 19),
    '5y': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_Y + (NEW_LINE_SIZE * 3) + 4,
    '6x': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_X + (SPACE_SIZE * 21) + 3,
    '6y': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_Y + (NEW_LINE_SIZE * 3) + 4,
    '7x': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_X + (SPACE_SIZE * 24) + 3,
    '7y': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_Y + (NEW_LINE_SIZE * 3) + 4,

    # Program updated coordinates
    '8x': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_X + (SPACE_SIZE * 10) + 11,
    '8y': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_Y + (NEW_LINE_SIZE * 6) + 8,
    '9x': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_X + (SPACE_SIZE * 12) + 4,
    '9y': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_Y + (NEW_LINE_SIZE * 6) + 8,
    '10x': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_X + (SPACE_SIZE * 19) + 15,
    '10y': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_Y + (NEW_LINE_SIZE * 11) + 30,
    '11x': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_X + (SPACE_SIZE * 21) + 4,
    '11y': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_Y + (NEW_LINE_SIZE * 11) + 30,
    '12x': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_X + (SPACE_SIZE * 24) - 3,
    '12y': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_Y + (NEW_LINE_SIZE * 11) + 30,
    '13x': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_X + (SPACE_SIZE * 26) + 14,
    '13y': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_Y + (NEW_LINE_SIZE * 15) + 16
}

coordinates_right = {
    # User inserted values coordinates
    '1x': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_X + (SPACE_SIZE * (10 + LEFT_RIGHT_DIFFERENCE_RATIO)),
    '1y': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_Y,
    '2x': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_X + (SPACE_SIZE * (23 + LEFT_RIGHT_DIFFERENCE_RATIO)),
    '2y': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_Y,
    '3x': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_X + (SPACE_SIZE * (19 + LEFT_RIGHT_DIFFERENCE_RATIO)),
    '3y': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_Y + (NEW_LINE_SIZE * 2),
    '4x': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_X + (SPACE_SIZE * (21 + LEFT_RIGHT_DIFFERENCE_RATIO)) + 3,
    '4y': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_Y + (NEW_LINE_SIZE * 2),
    '5x': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_X + (SPACE_SIZE * (19 + LEFT_RIGHT_DIFFERENCE_RATIO)),
    '5y': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_Y + (NEW_LINE_SIZE * 3) + 4,
    '6x': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_X + (SPACE_SIZE * (21 + LEFT_RIGHT_DIFFERENCE_RATIO)) + 3,
    '6y': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_Y + (NEW_LINE_SIZE * 3) + 4,
    '7x': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_X + (SPACE_SIZE * (24 + LEFT_RIGHT_DIFFERENCE_RATIO)) + 3,
    '7y': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_Y + (NEW_LINE_SIZE * 3) + 4,

    # Program updated coordinates
    '8x': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_X + (SPACE_SIZE * (10 + LEFT_RIGHT_DIFFERENCE_RATIO)) + 11,
    '8y': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_Y + (NEW_LINE_SIZE * 6) + 8,
    '9x': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_X + (SPACE_SIZE * (12 + LEFT_RIGHT_DIFFERENCE_RATIO)) + 4,
    '9y': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_Y + (NEW_LINE_SIZE * 6) + 8,
    '10x': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_X + (SPACE_SIZE * (19 + LEFT_RIGHT_DIFFERENCE_RATIO)) + 15,
    '10y': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_Y + (NEW_LINE_SIZE * 11) + 30,
    '11x': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_X + (SPACE_SIZE * (21 + LEFT_RIGHT_DIFFERENCE_RATIO)) + 4,
    '11y': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_Y + (NEW_LINE_SIZE * 11) + 30,
    '12x': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_X + (SPACE_SIZE * (24 + LEFT_RIGHT_DIFFERENCE_RATIO)) - 3,
    '12y': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_Y + (NEW_LINE_SIZE * 11) + 30,
    '13x': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_X + (SPACE_SIZE * (26 + LEFT_RIGHT_DIFFERENCE_RATIO)) + 14,
    '13y': FIRST_PICTURE_FIRST_PIXEL_START_POSITION_Y + (NEW_LINE_SIZE * 15) + 16
}

coordinates_max_param_size = {
    1: 1,
    2: 1,
    3: 3,
    4: 4,
    5: 4,
    6: 2,
    7: 3
}

move_locations_first_row = [(FIRST_PICTURE_FIRST_PIXEL_START_POSITION_X, FIRST_PICTURE_FIRST_PIXEL_START_POSITION_Y),
                            (270, 1430), (270, 2400)]

move_locations_second_row = [(SECOND_PICTURE_FIRST_PIXEL_START_POSITION_X, FIRST_PICTURE_FIRST_PIXEL_START_POSITION_Y),
                             (1383, 1427), (1383, 2400)]


def main():
    numbers = []
    img = Image.open(EMPTY_IMAGE_PATH)
    first_row_updates = []
    second_row_updates = []

    # Fix the size of the number images as this results in spacing differences for two images
    # as an img with width 22px will move with 3px less than 25px img for a space which in more spaces gets multiplied
    for i in range(0, 10):
        numbers.append(Image.open(f"cifri\\{i}.png").resize(NUMBER_IMAGES_SIZE))

    for i in range(0, GRAPHICS_AMMOUNT):
        print(current_graph_location_message.pop(0))
        if (i + 1) % 2 != 0:
            set_graph(img, numbers, use_left=True)
            first_row_updates.append(img.crop((268, 441, 1264, 1307)))
        else:
            set_graph(img, numbers, use_left=False)
            second_row_updates.append(img.crop((1379, 438, 2375, 1303)))
        img = Image.open(EMPTY_IMAGE_PATH)

    for index in range(0, len(first_row_updates)):
        img.paste(first_row_updates.pop(0), move_locations_first_row[index])
    for index in range(0, len(second_row_updates)):
        img.paste(second_row_updates.pop(0), move_locations_second_row[index])

    page = input("Моля въведете номер на страница:")

    while not page.isnumeric():
        page = input("Номерът на страницата може да бъде съставен само от цифри! Моля въведете номер на страница:")

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("times.ttf", 48)
    draw.text((2350 - (len(page) * SPACE_SIZE_PAGE), 3350), page, (118, 114, 110), font=font)

    write_out_to_desktop(img, page)


def set_graph(img: Image, numbers: list, use_left: bool):
    if use_left:
        coordinates = coordinates_left.copy()
    else:
        coordinates = coordinates_right.copy()

    for message in input_messages:
        param = input(message)
        # This is adjusting leading zero just for the record at position 5
        # as it's the only one that will require one for now
        if input_messages.index(message) == 5 and len(param) == 1:
            param = f"0{param}"

        if not validate(param, coordinates_max_param_size.get(input_messages.index(message) + 1)):
            while True:
                param = input(f"Неправилен параметър! {message} ")
                if validate(param, coordinates_max_param_size.get(input_messages.index(message) + 1)):
                    break

        if len(param) == 1:
            img.paste(numbers[int(param)], (coordinates.get(f"{input_messages.index(message) + 1}x"), coordinates.get(f"{input_messages.index(message) + 1}y")))
            if input_messages.index(message) == 1:
                img.paste(numbers[int(param)], (coordinates.get(f"{input_messages.index(message) + 12}x"), coordinates.get(f"{input_messages.index(message) + 12}y")))
            if input_messages.index(message) > 1:
                img.paste(numbers[int(param)], (coordinates.get(f"{input_messages.index(message) + 6}x"), coordinates.get(f"{input_messages.index(message) + 6}y")))
        elif input_messages.index(message) in [2, 4]:
            for char in param[::-1]:
                img.paste(numbers[int(char)], (coordinates.get(f"{input_messages.index(message) + 1}x"), coordinates.get(f"{input_messages.index(message) + 1}y")))
                img.paste(numbers[int(char)], (coordinates.get(f"{input_messages.index(message) + 6}x"), coordinates.get(f"{input_messages.index(message) + 6}y")))
                coordinates[f"{input_messages.index(message) + 1}x"] = coordinates[f"{input_messages.index(message) + 1}x"] - SPACE_SIZE
                coordinates[f"{input_messages.index(message) + 6}x"] = coordinates[f"{input_messages.index(message) + 6}x"] - SPACE_SIZE
        else:
            for char in param:
                img.paste(numbers[int(char)], (coordinates.get(f"{input_messages.index(message) + 1}x"), coordinates.get(f"{input_messages.index(message) + 1}y")))
                img.paste(numbers[int(char)], (coordinates.get(f"{input_messages.index(message) + 6}x"), coordinates.get(f"{input_messages.index(message) + 6}y")))
                coordinates[f"{input_messages.index(message) + 1}x"] = coordinates[f"{input_messages.index(message) + 1}x"] + SPACE_SIZE
                coordinates[f"{input_messages.index(message) + 6}x"] = coordinates[f"{input_messages.index(message) + 6}x"] + SPACE_SIZE


def validate(param: str, param_size) -> bool:
    if not param.isnumeric() or len(param) > param_size or len(param) <= 0:
        return False
    else:
        return True


def write_out_to_desktop(img, page):
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    folder_full_path = desktop + '\\graphics'
    file_full_path = folder_full_path + f'\\graphic_{page}.png'
    if not os.path.exists(folder_full_path):
        os.makedirs(folder_full_path)
    img.save(file_full_path)


if __name__ == '__main__':
    main()
