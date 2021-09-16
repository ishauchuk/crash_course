
def count_words(filename):
	"""Подсчет приблизительного количества слов в файле."""
	try:
		with open(filename, encoding='utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		pass
	else:
		# Подсчет приблизительного количества слов в файле
		words = contents.split()
		word = 'the'
		words_with = str(words).lower()
		words_count = words_with.count(word)
		print(f"The file {filename} has about {words_count} words '{word}'.")

filenames = ["Frankenstein.txt", "The Great Gatsby.txt", 
			"The Adventures of Sherlock Holmes.txt"]
for filename in filenames:
	count_words(filename)
