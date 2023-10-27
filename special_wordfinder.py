from wordfinder import WordFinder

class SpecialWordfinder(WordFinder):

    def __init__(self, dire):
        """starts the wordfinder, but with a cleaner list """
        super().__init__(dire)
        self.list = self.clean_list()

    def clean_list(self):
        """makes a list with only letters in the alphabet"""
        list =[]
        for word in self.list:
            if word.isalpha():
                list.append(word)
        return list 
        