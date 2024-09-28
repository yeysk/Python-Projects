
# TASK 9: Text Analysis Program

text = str(input("Please enter a text: ")).lower()

print(text.split())

textList = text.split()
print(len(textList))

word_counter = {}

for word in textList:
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1
        
most_repeated_word = max(word_counter, key=word_counter.get)
frequency = word_counter[most_repeated_word]

print(f"\nThe most repeated word: '{most_repeated_word}' used ({frequency} times.)")

seperators = ['.', '?', '!']

sentences = []

for seperator in seperators:
    text = text.replace(seperator, '|')
    
sentences = text.split('|')

sentence_count = len([sentence for sentence in sentences if sentence.strip()])
print(f"\nNumber of sentences in the text: {sentence_count}")

total_length = sum(len(word) for word in textList)

word_number = len(textList)

if word_number > 0:
    average_length = total_length / word_number
    print(f"\nAverage length of the words: {average_length:.2f}")
else:
    print("\nThere is no word in the text.")