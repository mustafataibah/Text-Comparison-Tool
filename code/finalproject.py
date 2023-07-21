# Mustafa Taibah
# finalproject.py - (Final Project) 
# Comparing Texts

import math

def clean_text(txt):
        """ returns a list containing the words in txt after it has been cleaned. 
            Meaning there wont be any punctuation or special characters
            input txt : filehandle
        """
        new_text = ''
        txt = txt.lower()
            
        for punctuation in txt:
            if punctuation in 'abcdefghijklmnopqrstuvwxyz1234567890 ':
                new_text += punctuation

        return new_text.split()
    

def sample_file_write(filename):
        """ A function that demonstrates how to write a 
            Python dictionary to an easily-readable file.
        """
        d = {'test': 1, 'foo': 42}
        f = open(filename, 'w')
        f.write(str(d))
        f.close()
    

def sample_file_read(filename):
        """ A function that demonstrates how to read a 
            Python dictionary from a file.
        """
        f = open(filename, 'r')
        d_str = f.read()
        f.close()
        
        d = dict(eval(d_str))
        
        print("Inside the newly-read dictionary, d, we have:")
        print(d)
        
        
def stem(s):
        """ return the stem of s: the root part of the word 
        that excludes any prefixes and suffixes
        input s : string value
        """
        if s[-1] == 's':
            s = s[:-1]
        else:
            s = s
            
        if s[-3:] == 'ing':
            if len(s) < 6:
                s = s
            elif s[-4] == s[-5]:
                s = s[:-4]
            else:
                s = s[:-3]
        
        elif s[-3:] == 'ize':
            if len(s) < 6:
                s = s
            elif s[-4] == s[-5]:
                s = s[:-4]
            else:
                s = s[:-3]
        
        elif s[-3:] == 'ise':
            if len(s) < 6:
                s = s
            elif s[-4] == s[-5]:
                s = s[:-4]
            else:
                s = s[:-3]
        
        elif s[-2:] == 'er':
            if len(s) < 7:
                s = s
            elif s[-3] == s[-4]:
                s = s[:-3]
            else:
                s = s[:-2]
                
        elif s[-2:] == 'ed':
            if len(s) < 6:
                s = s
            else:
                s = s[:-2]
        
        elif s[-3:] == 'ies':
            if len(s) < 7:
                s = s
            else:
                s = s[:-2]
                
        elif s[-3:] == 'ion':
            if len(s) < 8:
                s = s
            else:
                s = s[:-3] 
                
        elif s[-4:] == 'able':
            if len(s) <7:
                s = s
            else:
                s = s[:-4]
        
        elif s[-4:] == 'ship':
            if len(s) < 6:
                s = s
            else:
                s = s[:-4]
        
        elif s[-1] == 'e':
            if len(s) < 4:
                s = s
            else:
                s = s[:-1]
            
        elif s[-1] == 'y':
            s = s[:-1] + 'i'
        
        else:
            s = s
            
        if s[:3] == 'dis':
            s = s[2:]
        
        elif s[:3] == 'sub':
            s = s[2:]
        
        elif s[:3] == 'pre':
            s = s[2:]
            
        else:
            s = s
      
        
        return s
  

def compare_dictionaries(d1, d2):
    """ return their log similarity score
        input d1 : dictionary , d2 : dictionary
    """
    score = 0
    total = sum([d1[x] for x in d1])

    for y in d2:
        if y in d1:
            score += math.log(d1[y] / total) * d2[y]
        else:
            score += math.log(0.5 / total) * d2[y]
            
    return score
        
    
        
        
class TextModel:
        """ blueprints for the objects that model a body of a text, a collection of one or more documents
        """
    
        def __init__(self, model_name):
            """ constructs a new TextModel object by initializing name, words, and word_lengths
                name : a string that is a label for this text model used in the filename saving, 
                model_name is passed in as a parametr
                words : a dictionary that records the number of times each word appears in text
                word_lengths : a dictionary that records the number of times each word length appears
            """
            self.name = model_name
            self.words = {}
            self.word_lengths = {}
            self.stems = {}
            self.sentence_lengths = {}
            self.adjective_words = {}
    
        def __repr__(self):
            """ returns a string representation that indicates the name of the model as well as the size  
                of the dictionaries for each feature of the text
            """
            s =  'text model name: ' + self.name + '\n'
            s += '  number of words: ' + str(len(self.words)) + '\n'
            s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
            s += '  number of stems: ' + str(len(self.stems)) + '\n'
            s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
            s += '  number of adjective words: ' + str(len(self.adjective_words)) 
    
            return s
    
    
        def add_string(self, s):
            """ Analyzes the string txt and adds its pieces 
                to all of the dictionaries in this text model.
                input s : string value
            """
            sentence_count = 0
            for l in s.split():
                sentence_count += 1
                if l[-1] in '.?!':
                    if sentence_count in self.sentence_lengths:
                        self.sentence_lengths[sentence_count] += 1
                        sentence_count = 0
                    else:
                        self.sentence_lengths[sentence_count] = 1
                        sentence_count = 0
            
            adjective_count = 0
            #https://www.ef.com/wwen/english-resources/english-vocabulary/top-50-adjectives/
            for l in s.split():
                    if l =='bad' or l == 'best'or l == 'better'or l =='big'or l =='black'or l =='certain'\
                        or l =='clear' or l =='different'or l =='early'or l =='easy'or l =='economic'\
                        or l =='federal'or l =='free'or l =='full'or l =='good'or l =='hard'or l =='high'\
                        or l =='human'or l =='important'or l =='international'or l =='large'or l =='late'\
                        or l =='little'or l =='local'or l =='long'or l =='low'or l =='major'or l =='military'\
                        or l =='national'or l =='old'or l =='only'or l =='other'or l =='political'\
                        or l =='possible'or l =='public'or l =='real'or l =='recent'or l =='right'\
                        or l =='small'or l =='social'or l =='special'or l =='strong'or l =='sure'or l =='true'\
                        or l =='white'or l == 'whole'or l == 'young'or l == 'adventurous'or l == 'adventurous':
                    
                            adjective_count += 1
                            if l in self.adjective_words:
                                self.adjective_words[l] += 1
                            else:
                                self.adjective_words[l] = 1
                    
            word_list = clean_text(s)
        
            for w in word_list:
                if w in self.words:
                    self.words[w] += 1
                else:
                    self.words[w] = 1
        
            for w in word_list:
                if len(w) in self.word_lengths:
                    self.word_lengths[len(w)] += 1
                else:
                    self.word_lengths[len(w)] = 1
                
            for w in word_list:
                if stem(w) not in self.stems:
                    self.stems[stem(w)] = 1
                else:
                    self.stems[stem(w)] += 1
                    
            
                
        
        def add_file(self, filename):
            """ adds all of the text in filename to the model
            """
            file = open(filename, 'r', encoding='utf8', errors='ignore')
            text = file.read()
            file.close()
            
            self.add_string(text)
            
    
        def save_model(self):
            """ Saves the TextModel object self by writing its 
                various feature dictionaries to files 
            """
            f = open(self.name + '_' + 'words' , 'w')
            f.write(str(self.words))
            f.close()
        
            fi = open(self.name + '_' + 'word_lengths' , 'w')
            fi.write(str(self.word_lengths))
            fi.close()
        
            fil = open(self.name + '_' + 'stems' , 'w')
            fil.write(str(self.stems))
            fil.close()
        
            file = open(self.name + '_' + 'sentence_lengths' , 'w')
            file.write(str(self.sentence_lengths))
            file.close()
        
            fileh = open(self.name + '_' + 'adjective_words', 'w')
            fileh.write(str(self.adjective_words))
            fileh.close()
        
        
        def read_model(self):
            """ Reads the stored dictionaries for the called TextModel object from their files
            and assigns them to the have the attributes of the called TextModel
            """
            f = open(self.name + '_' + 'words' , 'r')
            d_str = f.read()
            f.close()
        
            fi = open(self.name + '_' + 'word_lengths' , 'r')
            di_str = fi.read()
            fi.close()
        
            fil = open(self.name + '_' + 'stems' , 'r')
            dic_str = fil.read()
            fil.close()
        
            file = open(self.name + '_' + 'sentence_lengths' , 'r')
            dict_str = file.read()
            file.close()
            
            fileh = open(self.name + '_' + 'adjective_words' , 'r')
            dicti_str = fileh.read()
            fileh.close()
        
            self.words = eval(d_str)
            self.word_lengths = eval(di_str)
            self.stems = eval(dic_str)
            self.sentence_lengths = eval(dict_str)
            self.adjective_words = eval(dicti_str)
    
    
        def similarity_scores(self, other):
            """ returns a list of log similarity scores measuring the similarity of self and other
                input : other : dictionary 
            """
            words_score = compare_dictionaries(other.words, self.words)
            
            word_lengths_score = compare_dictionaries(other.word_lengths, self.word_lengths)
            
            stems_score = compare_dictionaries(other.stems, self.stems)

            sentence_lengths_score = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
            
            adjective_words_score = compare_dictionaries(other.adjective_words, self.adjective_words)
            
            score = [words_score, word_lengths_score, stems_score, sentence_lengths_score, adjective_words_score]
            return score
        
        
        def classify(self, source1, source2):
            """ compares the called TextModel object to two other 'sources' TextModel objects
                and determines which of these TextModel is the more likely source of the called TextModel
                input : source1 : dictionary , source2 : dictionary
            """
            sc1_score = self.similarity_scores(source1)
            sc2_score = self.similarity_scores(source2)
            
            print('scores for ', source1.name , ':' , sc1_score)
            print('scores for ', source2.name , ':', sc2_score) 
            
            weighted_sum1 = 0
            weighted_sum2 = 0
            
            if sc1_score[0] > sc2_score[0]:
                weighted_sum1 += 1
            else:
                weighted_sum2 += 1
            
            if sc1_score[1] > sc2_score[1]:
                weighted_sum1 += 2
            else:
                weighted_sum2 += 2
            
            if sc1_score[2] > sc2_score[2]:
                weighted_sum1 += 1.5
            else:
                weighted_sum2 += 1.5
            
            if sc1_score[3] > sc2_score[3]:
                weighted_sum1 += 1
            else:
                weighted_sum2 += 1
                
            if sc1_score[4] > sc2_score[4]:
                weighted_sum1 += 0.5
            else:
                weighted_sum2 += 0.5
            
            if weighted_sum1 > weighted_sum2:
                print(self.name, 'is more likely to have come from ', source1.name)
            else:
                print(self.name, 'is more likey to come from ', source2.name)
                

def test():
    """ a function to test different textmodelsx and sources and classify them """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)


def run_tests():
    """ a function to test different textmodels and sources and also classifying them"""
    source1 = TextModel('Friends')
    source1.add_file('Friends.txt')

    source2 = TextModel('HIMYM')
    source2.add_file('HIMYM.txt')

    new1 = TextModel('WR Paper')
    new1.add_file('WRPaper.txt')
    new1.classify(source1, source2)
    
    new2 = TextModel('Friends 2')
    new2.add_file('Friends2.txt')
    new2.classify(source1, source2)
    
    new3 = TextModel('HIMYM 2')
    new3.add_file('HIMYM2.txt')
    new3.classify(source1, source2)
    
    new4 = TextModel('Community')
    new4.add_file('Community.txt')
    new4.classify(source1, source2)
    
    
            
             
            

            
        

        

            
            
        
    
    
            
    
    
        
    
    
        
        
