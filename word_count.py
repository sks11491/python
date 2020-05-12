import operator

sentence = "This is a demo string and this is a real demo of string to the list."
words = sentence.lower().split(" ")
# print(words)
words_count = {}
for word in words:
    if word in words_count.keys():
        word_count = words_count[word]
        words_count[word] = word_count + 1
    else:
        words_count[word] = 1
print(words_count)

# list comprehension
minValue = words_count[min(words_count, key=words_count.get)]
maxValue = words_count[max(words_count, key=words_count.get)]
countWiseWordsDictionary = {}
for i in range(minValue, maxValue+1):
    countWiseWordsDictionary[i] = [count for count in words_count if words_count[count] == i]
print(countWiseWordsDictionary)

maxCountElement = max(words_count.items(), key=operator.itemgetter(1))[0]
print("Word(s) having maximum occurance in sentance is:",countWiseWordsDictionary[maxValue])
print("Number of occurance for the Word in sentance is:", maxValue)