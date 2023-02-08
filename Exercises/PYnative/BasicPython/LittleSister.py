def add_prefix_un(word):
	res = "".join(("un", word))
	return res

def make_word_groups(vocab_words):
	separator = ' :: '

	prefix = vocab_words[0]
	words = vocab_words[1:]

	prefixed_words = [prefix + word for word in words]
	result = prefix + separator + separator.join(prefixed_words)

	return result

print(make_word_groups(['en', 'close', 'joy']))


def remove_suffix_ness(word):
	return word[:-4] if word[-5] != 'i' else word[:-5] + 'y'

print(remove_suffix_ness('happiness'))

def adjective_to_verb(sentence, index):
	return sentence.split()[index].strip('.') + 'en'

print(adjective_to_verb('I need to make that bright.', -1))
print(adjective_to_verb('It got dark as the sun set.', 2))



