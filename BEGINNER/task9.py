
# TASK 9: Text Analysis Program

while True: 
    try:
        text = str(input("\nPlease enter a text or press q to quit: ")).lower()
        
        if text == 'q':
            break
   
        textList = text.split()
        
        word_counter = {}
        
        for word in textList:
            if word in word_counter:
                word_counter[word] += 1
            else:
                word_counter[word] = 1
        
        # En yüksek frekansı bulma
        max_frequency = max(word_counter.values())
        
        # En sık tekrar eden kelimeleri listeye ekleme
        most_repeated_words = [word for word, count in word_counter.items() if count == max_frequency]
        
        # En sık tekrar eden kelimeleri ve tekrar sayısını ekrana yazdırma
        if len(most_repeated_words) > 1:
            print(f"\nThe most repeated words: {', '.join(most_repeated_words)} used ({max_frequency} times each.)")
        else:
            print(f"\nThe most repeated word: '{most_repeated_words[0]}' used ({max_frequency} times.)")
        
        seperators = ['.', '?', '!']
        
        # Cümle sayısını bulma
        for seperator in seperators:
            text = text.replace(seperator, '|')
            
        sentences = text.split('|')
        
        sentence_count = len([sentence for sentence in sentences if sentence.strip()])
        print(f"\nNumber of sentences in the text: {sentence_count}")
        
        # Ortalama kelime uzunluğunu bulma
        total_length = sum(len(word) for word in textList)
        word_number = len(textList)
        
        if word_number > 0:
            average_length = total_length / word_number
            print(f"\nAverage length of the words: {average_length:.2f}")
        else:
            print("\nThere is no word in the text.")
    except ValueError:
        print("The text can't be empty. Please try again.")
