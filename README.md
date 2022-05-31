[![codecov](https://codecov.io/gh/TeamRexoma/Yuriko/branch/master/graph/badge.svg?token=M4U97ZU3N2)](https://codecov.io/gh/TeamRexoma/Innexia)

<h1 align="center">Y U R I K O</h3> 
<p align="center"><a href="https://t.meRexomaUpDate"><img src="https://telegra.ph/file/e7c3c6b1218e60204c2c5.jpg" width="300"></a></p>
<p align="center">
    📍A Powerful Group Management Bot:

## How to setup on Heroku 
For starters click on this button 

<p align="center"><a href="https://heroku.com/deploy?template=https://github.com/TeamRexoma/Yuriko"> <img src="https://img.shields.io/badge/Deploy%20To%20Heroku-green?style=for-the-badge&logo=heroku" width="220" height="38.45"/></a></p>

## Our Telegram Channel and Group

<a href="https://t.me/RexomaSupport"><img src="https://img.shields.io/badge/Join-Group%20Support-black.svg?style=for-the-badge&logo=Telegram"></a> <a href="https://t.me/RexomaUpDate"><img src="https://img.shields.io/badge/Join-Updates%20Channel-black.svg?style=for-the-badge&logo=Telegram"></a>

# Preparation

1. Get Config Values and put it in config.py
2. install vps.txt 
4. python3 -m Innexia

# Run Development

- Clone this repo.
- Install vps.txt for all required arguments
- edit config.py  and fill all required fields.
- create an background screen run by using `screen`
- Type `python3 -m Innexia` in your Virtual Private Server.
- Your bot has succesfully working local as Development using Poll mode.

# Run Production

- Clone this repo.
- Install MongoDB and create database e.g. `test`.
- Copy .example.env to .env and fill all required fields.
- Server with domain name must include HTTPS support (e.g https://yoursite.co.id) for using webhook mode.
- Run `go build .` and place your binary somewhere.
- Setup reverse proxy for Web
  Server, [here example](https://www.google.com/search?client=firefox-b-d&q=nginx+reverse+proxy+example).
- Launch bot with `./SiskamlingBot`, your bot will run using poll or webhook.

## Credits 
*   [B L A Z E](https://telegram.dog/PiroxPower)
*   [S H A K A](https://telegram.dog/ShakaOp)
*   [A A Y U S H](https://telegram.dog/Op_Aayu)
