#!/usr/bin/env bash

PAYLOAD=$(curl -X POST -H "Content-Type: application/json; charset=UTF-8" --data-binary "{\"null\":null}" "https://api.whatspos.com/p-market-web/v1/auth/captcha" 2>/dev/null)
TOKEN=$(echo $PAYLOAD | jq -r .token | cut -c 9-)

echo "[+] Getting some image from Pax Store Marketplace Demo (you can change to any instance of you want c:)..."
echo "[+] Current captcha token is $TOKEN (also saving in ./images)"
[ ! -d "./images" ] && mkdir ./images
echo $PAYLOAD | jq -r .img | base64 -d > "./images/$TOKEN.jpg"
echo "[+] Rendering image..."
echo $PAYLOAD | jq -r .img | base64 -d | imgcat --width 24 --height 6
echo "[+] Trying to crack captcha..."
./captcha_solver.py "./images/$TOKEN.jpg"
echo "[+] Analysed image was:"
imgcat captcha.png
rm captcha.png
