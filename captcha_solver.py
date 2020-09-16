#!/usr/bin/env python3

from tesserocr import PyTessBaseAPI, PSM, OEM
from sys import argv
import cv2

import locale
locale.setlocale(locale.LC_ALL, 'C')


def resolve(path):
    captcha_image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    captcha_image = cv2.resize(captcha_image, None, fx=6, fy=6, interpolation=cv2.INTER_LINEAR)
    captcha_image = cv2.medianBlur(captcha_image, 9)
    th, captcha_image = cv2.threshold(captcha_image, 65, 250, cv2.THRESH_BINARY)
    cv2.imwrite('captcha.png', captcha_image)

    with PyTessBaseAPI() as api:
        api.SetVariable('tessedit_char_whitelist', 'abcdefghijklmnopqrstuvwxyz1234567890')
        api.SetImageFile('captcha.png')
        return api.GetUTF8Text().replace(' ', '').rstrip().lower()


if __name__ == '__main__':
    captcha_text = resolve(argv[1])
    if captcha_text:
        print(f'[+] Cracked text is {captcha_text}')
    else:
        print('[!] Unable to solve!')
