text_to_analyze = """Python is a high-level programming language. It is known for its simplicity and readability.
Python supports multiple programming paradigms including procedural, object-oriented, and functional programming.

Many developers choose Python for its extensive libraries and frameworks. 
The language is widely used in web development, data science, artificial intelligence, and automation.
Python's philosophy emphasizes code readability and simplicity!"""

# ----- MAIN FUNCTIONS -----

def count_words(text = ""):
    word_list = word_list_no_puntuations(text)

    print(f"Total Words: {len(word_list)}")

def count_sentences(text = ""):
    cleaned_text = text.replace("!", ".").replace("?", ".")
    sentence_list = cleaned_text.split(".")
    sentence_list.remove("")

    print(f"Total Sentences: {len(sentence_list)}")

def count_paragraphs(text = ""):
    paragraph_list = text.split("\n\n")

    print(f"Total Paragraphs: {len(paragraph_list)}")

def most_common_word(text = ""):
    word_list = word_list_no_puntuations(text)
    word_count = {}

    # Counts the numbers of instances of words
    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    most_common_word = ""
    highest_instance = 0

    # Finds the word with the highest instance
    for word in word_count:
        if word_count[word] > highest_instance:
            highest_instance = word_count[word]
            most_common_word = word
    
    print(f'Most Common Word: "{most_common_word}" (appears {highest_instance} times)')

def average_word_length(text = ""):
    word_list = word_list_no_puntuations(text)
    word_count = 0
    character_count = 0

    # Sums up all characters of words
    for word in word_list:
        character_count += len(word)
        word_count += 1
    
    average_word_length = character_count / word_count

    print(f"Average Word Length: {average_word_length} characters")

def find_long_words(text = "", min_length = 8):
    word_list = word_list_no_puntuations(text)
    unique_word_list = []
    long_word_list = []

    # Remove duplicates
    for word in word_list:
        if word not in unique_word_list:
            unique_word_list.append(word)

    # Add appropriate words to final list
    for word in unique_word_list:
        if len(word) > min_length:
            long_word_list.append(word)

    print(f"Words longer than {min_length} characters: {long_word_list}")

# ----- HELPER FUNCTIONS -----

def word_list_no_puntuations(text = ""):
    text_no_punctutations = text.lower().replace("!", ".").replace("?", ".").replace(",", ".").replace(".", "").replace("-", " ").replace("'s", "")
    clean_word_list = text_no_punctutations.split()

    return clean_word_list

# ----- OUTPUT -----

print("=== TEXT ANALYSIS REPORT ===")
count_words(text_to_analyze)
count_sentences(text_to_analyze)
count_paragraphs(text_to_analyze)
most_common_word(text_to_analyze)
average_word_length(text_to_analyze)
find_long_words(text_to_analyze)