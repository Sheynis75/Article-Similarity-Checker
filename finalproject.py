def clean_text(txt):
    """returns a list containing the words in txt after it has been cleaned"""
    cleaned = ''
    for letter in txt:
        if letter.isalpha() or letter.isspace():
            cleaned += letter
    return cleaned.lower().split(' ')

def sample_file_write(filename):
    """A function that demonstrates how to write a
       Python dictionary to an easily-readable file.
    """
    d = {'test': 1, 'foo': 42}   # Create a sample dictionary.
    f = open(filename, 'w')      # Open file for writing.
    f.write(str(d))              # Writes the dictionary to the file.
    f.close()                    # Close the file.
    
def sample_file_read(filename):
    """A function that demonstrates how to read a
       Python dictionary from a file.
    """
    f = open(filename, 'r')    # Open for reading.
    d_str = f.read()           # Read in a string that represents a dict.
    f.close()   
    d = dict(eval(d_str))      # Convert the string to a dictionary.
    print("Inside the newly-read dictionary, d, we have:")
    print(d)


class TextModel:
    def __init__(self, model_name):
        """constructs a new TextModel object by accepting a string model_name as a parameter"""
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
 
    def __repr__(self):
        """Return a string representation of the TextModel."""
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths))
        return s
    
    def add_string(self, s):
        """Analyzes the string txt and adds its pieces to all of the dictionaries in this text model."""
        word_list = clean_text(s)
        for w in word_list:
            if w in self.words:
                self.words[w] += 1
            else:
                self.words[w] = 1
            word_length = len(w)
            if word_length in self.word_lengths:
                self.word_lengths[word_length] += 1
            else:
                self.word_lengths[word_length] = 1
            
    def add_file(self, filename):
        """adds all of the text in the file identified by filename to the model"""
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        text = f.read()
        self.add_string(text)
        
    def save_model(self):
        """saves the TextModel object self by writing its various feature dictionaries to files"""
        file_1 = open(self.name + '_' + 'words', 'w')
        file_1.write(str(self.words))
        file_1.close()
        file_2 = open(self.name + '_' + 'word_lengths', 'w')
        file_2.write(str(self.word_lengths))
        file_2.close()
        
    def read_model(self):
        """reads the stored dictionaries for the called TextModel object from their files and assigns them to the attributes of the called TextModel"""
        file_1 = open(self.name + '_' + 'words', 'r')
        dictionary_1 = file_1.read()
        file_1.close()
        new_dictionary_1 = dict(eval(dictionary_1))
        file_2 = open(self.name + '_' + 'word_lengths', 'r')
        dictionary_2 = file_2.read()
        file_2.close()
        new_dictionary_2 = dict(eval(dictionary_2))
        self.words = new_dictionary_1
        self.word_lengths = new_dictionary_2
    
        
    