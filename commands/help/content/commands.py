help_choices = {
    "address_conversion": [  # function value
        "Address Conversion commands",  # embed title
        """
            These commands convert Boom/Fortune/Itadaki Street Wii virtual
            addresses,either to File Offsets (for use in hex-editing), or
            to work with a different version of the game. (For example,
            converting a Boom Street address to Fortune Street and back.)
        """,
        """
            `/convert_address_to_file_offset`
            `/convert_address_to_other_region`
        """,
    ],
    "text_translation": [
        "Text Translation commands",
        """
            This command uses the DeepL service to translate text between
            languages. All Itadaki/Fortune/Boom Street languages are
            supported. Source language is automatically detected, but
            destination language must be specified.
        """,
        """
            `/translate`
        """,
    ],
    "value_conversion": [
        "Value Conversion commands",
        """
            These commands convert values to different formats. The
            supported formats are hexadecimal, integer, and float, and
            each command can auto-detect input values of the other two
            types. (For example, `/convert_to_hex` can detect values of
            both integer and floating-point types.)
        """,
        """
            `/convert_value_to_float`
            `/convert_value_to_hex`
            `/convert_value_to_int`
        """,
    ],
    "venture_card": [
        "Venture Card commands",
        """
            These commands allow pulling venture cards from Boom /
            Fortune / Itadaki Street Wii. The `/pull_card` command
            accepts a number parameter between 1 and 128 and will
            pull the card specified. The `/pull_random_card` command
            does not accept a parameter, and will pull a random card
            instead.
        """,
        """
            `/pull_card`
            `/pull_random_card`
        """,
    ],
}
