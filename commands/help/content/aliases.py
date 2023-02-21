from app import bot

prefix = bot.command_prefix

address_converter_aliases = [
    f"`{prefix}bsv2fsv` => `bsvtofsv` \n",
    f"`{prefix}bsv2isv` => `bsvtoisv` \n",
    f"`{prefix}fsv2bsv` => `fsvtobsv` \n",
    f"`{prefix}isv2bsv` => `isvtobsv` \n",
    f"`{prefix}bsv2bsf` => `bsvtobsf` \n",
    f"`{prefix}fsv2fsf` => `fsvtofsf` \n",
]
card_aliases = [
    f"`{prefix}card` => `chancecard`, `pull_card`, `venture` \n",
]
help_aliases = [
    f"`{prefix}aliases` => `alias`, `alt` \n",
    f"`{prefix}help` => `commands` \n",
]
text_translation_aliases = [
    f"`{prefix}en` => `english`\n",
    f"`{prefix}jp` => `japanese`\n",
]
value_converter_aliases = [
    f"`{prefix}hex2int` => `hextoint`\n",
    f"`{prefix}hex2float` => `hextofloat`\n",
    f"`{prefix}int2hex` => `inttohex`\n",
    f"`{prefix}float2hex` => `floattohex`",
]
url_aliases = [
    f"`{prefix}calc` => `calculator`\n",
    f"`{prefix}github` => `git`, `repo`\n",
    f"`{prefix}invite` => `discord`, `invitation`, `serverlink`\n",
    f"`{prefix}twitch` => `ttv`\n",
    f"`{prefix}youtube` => `channel`, `tube`, `yt`\n",
]
