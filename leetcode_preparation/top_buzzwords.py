import re

quotes = [
    "Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
    "The new Elmo dolls are super high quality",
    "Expect the Elsa dolls to be very popular this year, Elsa!",
    "Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
    "For parents of older kids, look into buying them a drone",
    "Warcraft is slowly rising in popularity ahead of the holiday season"
]
toys = ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"]
N = 3

toys_freq = {toy: [0, 0] for toy in toys}
# print(toys_freq)
for quote in quotes:
    # for each quote, initiate toy occurence to False
    quote_toy = {toy: False for toy in toys}
    # convert quote to lower case,split
    for word in quote.lower().split():
        # remove anything other than lower cased letters in each word
        word = re.sub('[^a-z]', '', word)
        # increment count of toy if it exists in toys dictionary
        if word in toys_freq:
            toys_freq[word][0] += 1
            if not quote_toy[word]:
                quote_toy[word] = True
                toys_freq[word][1] += 1
print(toys_freq.items())
result = [w[0] for w in sorted(toys_freq.items(), key=lambda x: (-x[1][0],-x[1][1],x[0]))[:N]]
print(result)
