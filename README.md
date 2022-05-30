[![codecov](https://codecov.io/gh/TeamRexoma/Yuriko/branch/master/graph/badge.svg?token=M4U97ZU3N2)](https://codecov.io/gh/TeamRexoma/Innexia)

# Innexia 

Official repository of [@InnexiBot](https://t.me/InnexiaBot), written in python 

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
