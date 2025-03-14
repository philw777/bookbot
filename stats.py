def count_words(text):
	words = text.split()
	return words

def count_chars(text):
	body = text.lower()
	char_count = {}
	for char in body:
		if char not in char_count:
			char_count[char] = 1
		else:
			char_count[char] += 1
	return char_count

def sort_on(dict):
	return dict["count"]


def sort_dict(text):
	dict_list = []
	keys = []
	values = []
	for i in text:
		if i.isalpha():
			keys.append(i)
			values.append(text[i])
	for n in range(len(keys)):
		dict_list.append({'char': keys[n], 'count': values[n]})
	dict_list.sort(reverse=True, key=sort_on)
	return dict_list
