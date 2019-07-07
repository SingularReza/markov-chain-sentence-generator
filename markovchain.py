import random

original_text = ""
original_text = input("Enter the lines here: ")

# Dictionary Generation

text_array = original_text.split('.')

for index, text in enumerate(text_array):
	text_array[index] = text.strip().lower()

text_array.pop()

dictionary = []

for text in text_array:
	line_array = text.split(' ')
	for index, word in enumerate(line_array):
		word_data = {'name': '', 'start': {'status': False, 'count': 0}, 'next': [], 'end': False,}
		if not any(item['name'] == word for item in dictionary):
			word_data['name'] = word
			dictionary.append(word_data)
		else:
			for item in dictionary:
				if item['name'] == word:
					word_data = item
					break;
		if index == 0:
			dictionary[dictionary.index(word_data)]['start'] = {'status': True, 'count': word_data['start']['count']+1}
		if index != len(line_array)-1:
			if not any(item['word'] == line_array[index+1] for item in dictionary[dictionary.index(word_data)]['next']):
				dictionary[dictionary.index(word_data)]['next'].append({'word': line_array[index+1], 'count': 1})
			else:
				for ind, item in enumerate(dictionary[dictionary.index(word_data)]['next']):
					if item['word'] == line_array[index+1]:
						dictionary[dictionary.index(word_data)]['next'][ind]['count'] += 1;
						break;
		else:
			dictionary[dictionary.index(word_data)]['end'] = True

# Sentence generation

option = input("Generate a Sentence(1), exit(any other key):")

start_words = []
		
for word in dictionary:
	if word['start']['status']:
		for instance in range(0, word['start']['count']):
			start_words.append(word['name'])

print('start', start_words)

while option == '1':
	sentence = ''
	word = random.choice(start_words)
	sentence = sentence + word
	word_index = 0

	while word_index < len(dictionary):
		item = dictionary[word_index]
		word_data = {}
		if item['name'] == word:
			word_data = item
			next_words = []
			if word_data['end']:
				print(word_data)
				sentence = sentence+'.'
				break
			else:
				#print(word_data)
				for next_word in word_data['next']:
					for instance in range(0, next_word['count']):
						next_words.append(next_word['word'])
				add_word = random.choice(next_words)
				sentence = sentence + ' ' + add_word
				word = add_word
				word_index = 0
				continue

		word_index += 1

	print(sentence)
	option = input("Generate a Sentence(1), exit(any other key):")