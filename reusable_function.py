## Reusable Function
# Example: Improvement to emoji_converter.py
def emoji_trans(msg):
    text_2_emoji = {
        ":)":"🙂",
        ":D":"😀",
        ":(":"😟"
    }
    output = ''
    words = msg.split(' ')

    for word in words:
        output += text_2_emoji.get(word, word) + ' '
    return output


msg = input('>')
print(emoji_trans(msg))