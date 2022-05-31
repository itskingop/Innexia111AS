[![codecov](https://codecov.io/gh/TeamRexoma/Yuriko/branch/master/graph/badge.svg?token=M4U97ZU3N2)](https://codecov.io/gh/TeamRexoma/Innexia)

<h1 align="center">Y U R I K O</h3> 
<p align="center">
  <img src="https://telegra.ph/-05-31-535.jpg">
</p>

### Telegram Group
<p align="left">
<a href="https://t.me/RexomaSupport" alt="Telegram!"> <img src="https://aleen42.github.io/badges/src/telegram.svg" /> </a>

### Bot And Channel 
* Bot Link:  <a href="http://t.me/innexiaBot" alt=" Λ L I S S Λ "> <img src="https://img.shields.io/badge/%F0%9F%A4%96%20-Y U R I K O-blue" /> </a>
* Support Channel: <a  href="https://t.me/Rexoma" alt="Help Centre Logs"> <img  src="https://img.shields.io/badge/%F0%9F%92%A1-Y U R I K O%20UPDATES-9cf" /> </a>
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
