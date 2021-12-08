def color(msg):
    print(("\033[35m {}".format(msg)))


text = '\n'.join([''.join([('Юля'[(x - y) % len('Юля')]
                            if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (
            y * 0.1) ** 3 <= 0 else ' ')
                           for x in range(-30, 30)]) for y in range(30, -30, -1)])
color(text)
print('Люблю тебя моя малышка')
