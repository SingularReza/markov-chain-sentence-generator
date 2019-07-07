A /g/ challenge

# markov-chain-sentence-generator
A simple python script that takes a sample set of sentences and return probable sentences using markov chains

## Dictionary Generation
  1. Seperate the sentences
  2. Iterate through every word and note their next words, whether it is a starting word or ending word
  3. Record the no of occurences of each word while you are recording them as the next words
  4. Store them in whichever data structure you want. I used a list of dictionaries in this case
 
## Sentence Generation
  1. Start with a word that's noted as a starting word weighted by the number of times it occurred as a starting word amongst other starting words
  2. Select the next probable word from the generated dictionary based on the weightage of its occurence among other next words
  3. Do this until you hit something recorded as an ending word
  
  ### Note: You can implement the weightage in multiple ways. In this case I made a list for each time I selected a word. I populated the list with next words multiplied by the no of times they occurred as next word for a given word and used random choice for it. A better way to do it is using randint on a unique list
