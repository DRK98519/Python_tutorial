## Emoji Converter (Dict project)
text_2_emoji = {
    ':)': "🙂",
    ':D': "😀",
    ':(': "🙁"
}

msg = input('>')
words = msg.split(' ')  # msg.split(' ') returns a list consisting of msg parts. The string ' ' is considered as the seperator that determines
                        # when to assign a new element in the output string. Suppose msg = "Hello World", msg.split(' ') returns ['Hello', 'World']
# print(words)
output = ''
for word in words:
    output += text_2_emoji.get(word, word) + ' '  # If word is a key in text_2_emoji, its value (all string here) will be added to output string.
                                            # If word is not a key in text_2_emoji, return the word string itself and added to output
print(output)