from nltk import tokenize
import random, re

class Text(object):

        def __init__(self, text):
                """
                import text to use
                text - a (preferably large) body of text to find strings in
                """
                self.text = text.replace('\n', ' ').replace('\r', '')
                self.text = self.text.replace('_', '')
                self.sentences = tokenize.sent_tokenize(self.text)

        def len(self):
                """
                return number of sentences in text
                """
                return len(self.sentences)

        def include(self, term, case_sensitive=False):
                """
                Only include those sentences which include a given string
                term - a search string
                TODO - consider accepting a list of terms
                """
                newlist = []
                for line in self.sentences:
                        if case_sensitive:
                                if re.search(term, line, re.IGNORECASE):
                                        newlist.append(line)
                        else:
                                if re.search(term, line):
                                        newlist.append(line)

                self.sentences = newlist

        def reject(self, term, case_sensitive=False):
                """
                Remove all lines that include search term
                term - a string
                """
                
                newlist = []
                for line in self.sentences:
                        if case_sensitive:
                                if not re.search(term, line, re.IGNORECASE):
                                        newlist.append(line)
                        else:
                                if not re.search(term, line):
                                        newlist.append(line)

                self.sentences = newlist

        def select_custom(self, select_func):
                """
                Select all lines that pass a given test
                select_func - a function to run on the text, must return boolean
                """
                newlist = []
                for line in self.sentences:
                        if (select_func(line)):
                                newlist.append(line)

                self.sentences = newlist

        def cleanup(self):
                """
                Make sure first character is always uppercase
                TODO - all features such as closing all quotes
                """
                for line in self.sentences:
                        line = "".join(line[0].upper() + line[1:])

        def write(self, filename):
                """
                Write the current list of sentences to the given file
                """
                with open(filename, 'w') as f:
                        try:
                                for line in self.sentences:
                                        f.write(line + "\n")
                        finally:
                                f.close()

        def print(self):
                """
                print all lines
                """
                for line in self.sentences:
                        print(line, '\n\n')

        def printRandom(self, num=10):
                """
                print a random selection of sentences from the text
                num - the number of lines to print
                """
                for i in range(num):
                        lineno = random.randint(0, len(self.sentences))
                        print("Line: %d" % lineno)
                        print(self.sentences[lineno], '\n\n')
