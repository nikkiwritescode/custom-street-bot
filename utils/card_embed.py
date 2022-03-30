import discord
import json

en_json_path = "commands/venture/cards/text/en.json"
jp_json_path = "commands/venture/cards/text/jp.json"


class CardEmbed:
    def __init__(self, embed, file):
        self.file = file
        self.embed = embed

    def create_card_embed(card_id, username):
        image = f"commands/venture/cards/images/{card_id}.png"
        file = discord.File(image, filename="card.png")

        with open(en_json_path, "r") as read_file_en:
            en_dict = json.load(read_file_en)
        with open(jp_json_path, "r", encoding="utf8") as read_file_jp:
            jp_dict = json.load(read_file_jp)
        card_text = str(
            f"**EN:** {en_dict[str(card_id)]}\n**JP:** {jp_dict[str(card_id)]}"
        ).replace("$name", username)

        embed = discord.Embed(
            title="You got a Venture Card!",
            color=0x000000,
            inline=True,
        )
        embed.add_field(
            name=f"#{card_id}",
            value=card_text
        )
        embed.set_image(url="attachment://card.png")

        return CardEmbed(embed, file)
