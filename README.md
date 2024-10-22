# Discord Bot for Custom Street
[![CircleCI](https://circleci.com/gh/nikkiwritescode/custom-street-bot/tree/main.svg?style=shield)](https://circleci.com/gh/nikkiwritescode/custom-street-bot/tree/main)
## Table of Contents
* [Features](#features)
* [Supported Commands](#supported-commands)
  * [Address Conversion](#address-conversion)
  * [Board Validation](#board-validation)
  * [Text Translation](#text-translation)
  * [Value Conversion](#value-conversion)
  * [Venture Cards](#venture-cards)
* [Running this Bot in Another Environment](#running-this-bot-in-another-environment)
  * [Required Accounts](#required-accounts)
  * [Required Environment Variables](#required-environment-variables)
* [Contributing](#contributing)

## Features
* Conversion of addresses between Boom Street, Fortune Street, and Itadaki Street Wii
* Conversion of values between hexadecimal, float and int
* Translation of text between all Boom/Fortune/Itadaki Street Wii-supported languages (via DeepL)
* Validation of CSMM-compatible board bundles via the `cs-board-tools` library
* Posting of Rules and links to Custom Street accounts (Address Calculator, Discord, GitHub, YouTube, Twitch, and Wiki)
* Posting Venture Card embeds with English and Japanese text
* All commands are slash commands, with help for each command shown inside Discord itself

## Supported Commands
### Address Conversion
These commands convert Boom/Fortune/Itadaki Street Wii virtual addresses, either to File Offsets (for use in hex-editing), or to work with a different version of the game. (For example, converting a Boom Street address to Fortune Street and back.)

* `/convert_address_to_file_offset`
* `/convert_address_to_other_region`

### Board Validation
This command takes in a CSMM-compatible board bundle (.zip), extracts it, and tests its components to ensure they are valid. It utilizes the [cs-board-tools](https://github.com/FortuneStreetModding/cs-board-tools) library for its functionality.

* `/validate_board_bundle`

### Text Translation
This command uses the DeepL service to translate text between languages. All Boom/Fortune/Itadaki Street Wii languages are supported. Source language is automatically detected, but destination language must be specified.

* `/translate`

### Value Conversion
These commands convert values to different formats. The supported formats are hexadecimal, integer, and float, and each command can auto-detect input values of the other two types. (For example, `/convert_to_hex` can detect values of both integer and floating-point types.)

* `/convert_value_to_float`
* `/convert_value_to_hex`
* `/convert_value_to_int`

### Venture Cards
These commands allow pulling venture cards from Boom / Fortune / Itadaki Street Wii. The `/pull_card` command accepts a number parameter between 1 and 128 and will pull the card specified. The `/pull_random_card` command does not accept a parameter, and will pull a random card instead.

* `/pull_card`
* `/pull_random_card`

## Running this Bot in Another Environment
Currently, it is not simple to run this bot elsewhere. This is because I use my own private Terraform modules to power the infrastructure behind it in AWS. Therefore, if you do decide to attempt to do so, you will be on your own when it comes to hosting it. However, the Dockerfile should build just about anywhere, so the knowledge you will need to run it largely pertains to running containerized applications in Docker. You will also need the following external accounts or services:

### Required Accounts
* A DeepL account, as the bot uses an Auth Key for its text translation functionality.
* A Discord Bot account, as you will need a Token in order for the bot to log into Discord.

### Required Environment Variables
* `DISCORD_TOKEN` -- The token used by the bot to interact with Discord
* `DEEPL_AUTH_KEY` -- The token used to interact with the DeepL service
* `GDRIVE_API_KEY` -- (Optional). Used with `cs-board-tools` to download music from Google Drive when running Fortune Street board validation tests.

## Contributing
Do you have ideas for bug fixes or new features? Fantastic! If you'd like to contribute to this bot, feel free to clone the repo and perform your work locally, then open a Pull Request with your changes! I will be more than glad to review your work, request changes, and even merge it in if your new functionality works well.
