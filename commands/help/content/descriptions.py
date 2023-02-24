from app import bot

prefix = bot.command_prefix

address_converters_help = [
    f"`{prefix}bsv2fsv` Boom Street Virtual Address to Fortune Street.\n",
    f"`{prefix}bsv2isv` Boom Street Virtual Address to Itadaki Street Wii.\n",
    f"`{prefix}fsv2bsv` Fortune Street Virtual Address to Boom Street.\n",
    f"`{prefix}fsv2isv` Fortune Street Virtual Address to Itadaki Street Wii.\n",
    f"`{prefix}isv2bsv` Itadaki Street Wii Virtual Address to Boom Street.\n",
    f"`{prefix}isv2fsv` Itadaki Street Wii Virtual Address to Fortune Street.\n",
    f"`{prefix}bsv2bsf` Boom Street Virtual Address to File Offset.\n",
    f"`{prefix}fsv2fsf` Fortune Street Virtual Address to File Offset.\n",
]
help_help = [
    f"`{prefix}aliases` Display alternate triggers for bot commands.\n",
    f"`{prefix}help` Display this panel.\n",
]
text_translation_help = [
    f"`{prefix}en` Convert text to English.\n",
    f"`{prefix}jp` Convert text to Japanese.\n",
]
urls_help = [
    f"`{prefix}calc` Display the Address Calculator URL.\n",
    f"`{prefix}contribute` Display a link to this bot's GitHub repo.\n",
    f"`{prefix}github` Display the Github URL.\n",
    f"`{prefix}invite` Display the server invite link.\n",
    f"`{prefix}twitch` Display the Twitch channel URL.\n",
    f"`{prefix}wiki` Display the Wiki URL.\n",
    f"`{prefix}youtube` Display the YouTube channel URL.",
]
value_converters_help = [
    f"`{prefix}hex2int` Convert Hex to Decimal.\n",
    f"`{prefix}hex2float` Convert Hex to Float.\n",
    f"`{prefix}int2hex` Convert Decimal to Hex.\n",
    f"`{prefix}float2hex` Convert Float to Hex.",
]
venture_cards_help = [
    f"`{prefix}card` Pull a random Venture Card.\n",
    f"`{prefix}card <number>` Pull a specific Venture Card.\n",
]
