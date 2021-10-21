import math
def clean_text(txt):
    """returns a list containing the words in txt after it has been cleaned"""
    cleaned = ''
    for letter in txt:
        if letter not in '.!?;:':
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
    
def paragraph_splitter(s):
    """splits paragraph into strings"""
    new_dictionary = {}
    count = 0
    r = s.split()
    for word in r:
        count += 1
        if word[-1] in '.?!':
                if count in new_dictionary:
                    new_dictionary[count] += 1
                else:
                    new_dictionary[count] = 1
                count = 0
    return new_dictionary
    
def stem(s):
    """returns the stem of s"""
    if s[-1] == 'y':
        new_s = s[:-1]
        new_s += 'i'
        return new_s
    elif s[-3:] == 'ies':
        new_s = s[:-3]
        new_s += 'i'
        return new_s
    elif s[-3:] == 'ing':
        if s[-4] == s[-5]:
            return s[:-4]
        else:
            return s[:-3]
    elif s[-2:] == 'er':
        return s[:-2]
    elif s[-1] == 's':
        stem_rest = s[:-1]
        return stem(stem_rest)
    elif s[-2:] == 'ly':
        return s[:-2]
    elif s[-2:] == 'ed':
        return s[:-2]
    else:
        return s

def compare_dictionaries(d1, d2):
    """takes two feature dictionaries d1 and d2 as inputs, and it should compute and return their log similarity score"""
    score = 0
    total = 0
    for i in d1:
        total += d1[i]
    for i in d2:
        if i in d1:
            score += d2[i] * math.log(d1[i] / total)
        else:
            score += d2[i] * math.log(0.5 / total)
    return score

class TextModel:
    def __init__(self, model_name):
        """constructs a new TextModel object by accepting a string model_name as a parameter"""
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.number_of_vowels = {}
 
    def __repr__(self):
        """Return a string representation of the TextModel."""
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  number of vowels ' + str(len(self.number_of_vowels))
        return s
    
    def add_string(self, s):
        """Analyzes the string txt and adds its pieces to all of the dictionaries in this text model."""
        sentence_lengths = paragraph_splitter(s)
        self.sentence_lengths = sentence_lengths
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
            new_stem = stem(w)
            if new_stem in self.stems:
                self.stems[new_stem] += 1
            else:
                self.stems[new_stem] = 1
        for i in range(len(s)):
            if s[i] in 'aeiou':
                if s[i] in self.number_of_vowels:
                    self.number_of_vowels[i] += 1
                else:
                    self.number_of_vowels[i] = 1
            
            
    def add_file(self, filename):
        """adds all of the text in the file identified by filename to the model"""
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        text = f.read()
        self.add_string(text)
        
    def save_model(self):
        """ saves the TextModel object self by writing its various feature
            dictionaries to files. There will be one file written for each
            feature dictionaries to files.
        """
        filename = self.name + '_' + 'words'
        f = open(filename, 'w')
        f.write(str(self.words))
        f.close()
       
        filename2 = self.name + '_' + 'word_lengths'
        f1 = open(filename2, 'w')
        f1.write(str(self.word_lengths))
        f1.close()
        
        filename3 = self.name + '_' + 'stems'
        f2 = open(filename3, 'w')
        f2.write(str(self.stems))
        f2.close()
        
        filename4 = self.name + '_' + 'sentence_lengths' 
        f3 = open(filename4, 'w')
        f3.write(str(self.sentence_lengths))
        f3.close()
        
        filename5 = self.name + '_' + 'number_of_vowels'
        f4 = open(filename5, 'w')
        f4.write(str(self.number_of_vowels))
        f4.close()
        
              
    def read_model(self):
        """ reads the stored dictionaries for the called TextModel object from
            their files and assigns them to the attributes of the called
            TextModel.
        """
        filename = self.name + '_' + 'words'
        f = open(filename, 'r')
        s_str = f.read()
        f.close()
       
        self.words = dict(eval(s_str))
       
        filename1 = self.name + '_' + 'word_lengths'
        f1 = open(filename1, 'r')
        s_str1 = f1.read()
        f1.close()
       
        self.word_lengths = dict(eval(s_str1))
        
        filename2 = self.name + '_' + 'stems'
        f2 = open(filename2, 'r')
        s_str2 = f2.read()
        f2.close()
        
        self.stems = dict(eval(s_str2))
        
        filename3 = self.name + '_' + 'sentence_lengths' 
        f3 = open(filename3, 'r')
        s_str3 = f3.read()
        f3.close()
        
        self.sentence_lengths = dict(eval(s_str3))
        
        filename4 = self.name + '_' + 'number_of_vowels'
        f4 = open(filename4, 'r')
        s_str4 = f4.read()
        f4.close()
        
        self.number_of_vowels = dict(eval(s_str4))
        
    def similarity_scores(self, other):
        """ returns a list of log similarity scores measuring the similarity of self and other – one score for each type of feature (words, word lengths, stems, sentence lengths, and your additional feature)"""
        word_score = compare_dictionaries(other.words, self.words)
        word_lengths_score = compare_dictionaries(other.word_lengths, self.word_lengths)
        stems_score = compare_dictionaries(other.stems, self.stems)
        sentence_lengths_score = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        number_of_vowels_score = compare_dictionaries(other.number_of_vowels, self.number_of_vowels)
        score_lst = [word_score, word_lengths_score, stems_score, sentence_lengths_score, number_of_vowels_score]
        return score_lst
    
    def classify(self, source1, source2):
        """that compares the called TextModel object (self) to two other “source” TextModel objects (source1 and source2) and determines which of these other TextModels is the more likely source of the called TextModel"""
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        print('scores for source1 : ', scores1)
        print('scores for source2 : ', scores2)
        similarity_1 = 0
        similarity_2 = 0
        if scores1[0] > scores2[0]:
            similarity_1 += 1
        else:
            similarity_2 += 1
        if scores1[1] > scores2[1]:
            similarity_1 += 1
        else:
            similarity_2 += 1
        if scores1[2] > scores2[2]:
            similarity_1 += 1
        else:
            similarity_2 += 1
        if scores1[3] > scores2[3]:
            similarity_1 += 1
        else:
            similarity_2 += 1
        if scores1[4] > scores2[4]:
            similarity_1 += 1
        else:
            similarity_2 += 1
        if similarity_1 > similarity_2:
            print(self.name, 'is more likely to have come from', source1.name)
        else:
            print(self.name, 'is more likely to have come from', source2.name)


    
def test():
    """ your docstring goes here """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')
    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')
    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)
        
def run_tests():
    """ your docstring goes here """
    source1 = TextModel('rowling')
    source1.add_file('rowling_source_text.txt')
    source2 = TextModel('shakespeare')
    source2.add_file('shakespeare_source_text.txt')
    new1 = TextModel('wr120')
    new1.add_file('wr120_source_text.txt')
    new1.classify(source1, source2)
    new2 = TextModel('bostonglobe')
    new2.add_file('bostonglobe_source_text.txt')
    new2.classify(source1, source2)
    new3 = TextModel('drseuss')
    new3.add_file('drseuss_source_text.txt')
    new3.classify(source1, source2)
    new4 = TextModel('edgarallenpoe')
    new4.add_file('edgarallenpoe_source_text.txt')
    new4.classify(source1, source2)