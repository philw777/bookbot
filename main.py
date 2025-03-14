import sys

def get_book_text(file_path):
	with open(file_path) as f:
		book_text=f.read()
	return book_text

def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankensten.txt...")
	print("----------- Word Count ----------")
	file_path = sys.argv[1]
	text = get_book_text(file_path)
	from stats import count_words
	print("Found", len(count_words(text)), "total words")
	print("-------- Character Count --------")
	from stats import count_chars
	from stats import sort_dict
	sorted_dict = sort_dict(count_chars(text))
	for dictionary in sorted_dict:
		print(*dictionary.values(), sep=": ")
	print("============== END ==============")
	return

main()
