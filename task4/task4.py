rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
rus_caps = rus.upper()
lat = 'abcdefghijklmnopqrstuvwxyz'
lat_caps = lat.upper()
param = 2


def shift(text, param):
    text_out = ''
    for char in text:
        if char == ' ':
            text_out += ' '

        elif char in rus:
            index = (rus.index(char) + param) % 33
            text_out += rus[index]

        elif char in rus_caps:
            index = (rus_caps.index(char) + param) % 33
            text_out += rus_caps[index]

        elif char in lat:
            index = (lat.index(char) + param) % 26
            text_out += lat[index]

        elif char in lat_caps:
            index = (lat_caps.index(char) + param) % 26
            text_out += lat_caps[index]

    return text_out


def main():
    with open('test_task_4.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        text = ''.join(lines)
        print(text)

    with open('answer_task_4.txt', 'w', encoding='utf-8') as file:
        text_out = shift(text, param)
        print(text_out)
        file.write(text_out)


if __name__ == "__main__":
    main()
