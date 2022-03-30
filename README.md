# Discord Bot for Custom Street
[![CircleCI](https://circleci.com/gh/nikkiwritescode/custom-street-bot/tree/main.svg?style=shield)](https://circleci.com/gh/nikkiwritescode/custom-street-bot/tree/main)
## Table of Contents
* [Functions](#functions)
* [Supported Commands](#supported-commands)
  * [Address Conversion](#address-conversion)
  * [Value Conversion](#value-conversion)
  * [Text Translation (Powered by DeepL)](#text-translation-powered-by-deepl)
  * [Venture Cards](#venture-cards)
  * [URLs](#urls)
* [Running this Bot in Another Environment](#running-this-bot-in-another-environment)
  * [Required Accounts](#required-accounts)
  * [Required Environment Variables](#required-environment-variables)
* [Contributing](#contributing)

## Functions
* Conversion of addresses between Boom Street and Fortune Street
* Conversion of values between hexadecimal and float or int, and vice versa
* Translation of text to English or Japanese (via DeepL)
* Posting of Rules and links to Custom Street accounts (Address Calculator, Discord, GitHub, YouTube, Twitch, and Wiki)
* Posting Venture Card embeds with English and Japanese text

## Supported Commands
### Address Conversion
* `bsv2fsv` - Converts a Boom Street Virtual Address to Fortune Street.
* `fsv2bsv` - Converts a Fortune Street Virtual Address to Boom Street.
* `bsv2bsf` - Converts a Boom Street Virtual Address to Boom Street File Offset.
* `fsv2fsf` - Converts a Fortune Street Virtual Address to Fortune Street File Offset.
### Value Conversion
* `hex2int` - Converts a hexadecimal value to a decimal, or integer, value
* `hex2float` - Converts a hexadecimal value to a floating-point value
* `int2hex` - Converts a decimal, or integer, value to hexadecimal
* `float2hex` - Converts a floating-point value to hexadecimal.
### Text Translation (Powered by DeepL)
* `en` - Translates text of any language to English.
* `jp` - Translates text of any language to Japanese.
### Venture Cards
* `card` - Displays a random Venture Card from Fortune Street Wii with both English and Japanese text.
* `card <number>` - Displays a specific Venture Card from Fortune Street Wii with both English and Japanese text. Accepts numbers 1 through 128.
### URLs
* `calc` - Displays the Address Calculator URL.
* `contribute` - Displays a link to this GitHub repo.
* `github` - Displays the Fortune Street Modding GitHub Organization URL.
* `invite` - Displays the Custom Street Discord Invite URL.
* `twitch` - Displays the Custom Street Twitch Account URL.
* `wiki` - Displays the Fortune Street Modding Wiki URL.
* `youtube` - Displays the Custom Street YouTube Account URL.

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

Super minor readme change!
