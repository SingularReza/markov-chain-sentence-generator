original_text = ""
original_text = input("Enter the lines here: ")

text_array = original_text.split('.')

for index, text in enumerate(text_array):
	text_array[index] = text.strip().lower()

text_array.pop()

#print(text_array)

dictionary = []

for text in text_array:
	line_array = text.split(' ')
	#print(line_array)
	for index, word in enumerate(line_array):
		word_data = {'name': '', 'start': {'status': False, 'count': 0}, 'next': [], 'end': {'status': False, 'count': 0}, 'instance': 0, }
		#print(word)
		if not any(item['name'] == word for item in dictionary):
			#print(index, any(item['name'] == word for item in dictionary))
			word_data['name'] = word
			dictionary.append(word_data)
			#print(word_data, index)
		else:
			for item in dictionary:
				if item['name'] == word:
					word_data = item
					break;
		if index == 0:
			dictionary[dictionary.index(word_data)]['start'] = {'status': True, 'count': word_data['start']['count']+1}
			#print(word_data, index)
		if index != len(line_array)-1:
			if not any(item['word'] == line_array[index+1] for item in dictionary[dictionary.index(word_data)]['next']):
				dictionary[dictionary.index(word_data)]['next'].append({'word': line_array[index+1], 'count': 1})
				#print(word_data, index)
			else:
				for ind, item in enumerate(dictionary[dictionary.index(word_data)]['next']):
					if item['word'] == line_array[index+1]:
						dictionary[dictionary.index(word_data)]['next'][ind]['count'] += 1;
						break;
		else:
			dictionary[dictionary.index(word_data)]['end'] = {'status': True, 'count': word_data['end']['count']+1}
			#print(word_data, index)

		print(word_data, index)

#print(dictionary)