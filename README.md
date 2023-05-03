# Discord Bot for Custom Street
[![CircleCI](https://circleci.com/gh/nikkiwritescode/custom-street-bot/tree/main.svg?style=shield)](https://circleci.com/gh/nikkiwritescode/custom-street-bot/tree/main)
## Table of Contents
* [Features](#features)
* [Running this Bot in Another Environment](#running-this-bot-in-another-environment)
  * [Required Accounts](#required-accounts)
  * [Required Environment Variables](#required-environment-variables)
* [Contributing](#contributing)

## Features
* Conversion of addresses between Boom Street, Fortune Street, and Itadaki Street Wii
* Conversion of values between hexadecimal, float and int
* Translation of text between all Boom/Fortune/Itadaki Street Wii-supported languages (via DeepL)
* Posting of Rules and links to Custom Street accounts (Address Calculator, Discord, GitHub, YouTube, Twitch, and Wiki)
* Posting Venture Card embeds with English and Japanese text
* All commands are slash commands, with help for each command shown inside Discord itself

## Running this Bot in Another Environment
Currently, it is not simple to run this bot elsewhere. This is because I use my own private Terraform modules to power the infrastructure behind it in AWS. Therefore, if you do decide to attempt to do so, you will be on your own when it comes to hosting it. However, the Dockerfile should build just about anywhere, so the knowledge you will need to run it largely pertains to running containerized applications in Docker. You will also need the following external accounts or services:

### Required Accounts
* A DeepL account, as the bot uses an Auth Key for its text translation functionality.
* A Discord Bot account, as you will need a Token in order for the bot to log into Discord.

### Required Environment Variables
* `DISCORD_TOKEN` -- The token used by the bot to interact with Discord
* `DEEPL_AUTH_KEY` -- The token used to interact with the DeepL service

## Contributing
Do you have ideas for bug fixes or new features? Fantastic! If you'd like to contribute to this bot, feel free to clone the repo and perform your work locally, then open a Pull Request with your changes! I will be more than glad to review your work, request changes, and even merge it in if your new functionality works well.
