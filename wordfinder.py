from random import choice as pick 


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    
    def __init__(self,dire):
        """Saves the directory, creates list of words, and prints number of words in directory """
        self.dire= dire
        self.list= self.get_words()
        list_len = len(self.list)
        print(f"{list_len} words read" )
    


    def random(self):
        """picks a random word"""
        return pick(self.list)
    
    def get_words (self):
        """return a list of the words in the directory"""
        words_list =[]
        file = open(self.dire,"r")
        for line in file:
            clean__line = line.replace("\n","")
            words_list.append(clean__line)
        
        file.close()
        return words_list    

