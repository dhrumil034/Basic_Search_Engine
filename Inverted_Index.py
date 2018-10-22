import nltk
import re
import math
nltk.download('stopwords')
nltk.download('punkt')

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

stop_words = set(stopwords.words('english'))
pc = PorterStemmer()


class Inverted_Index:

    def __init__(self,file_paths):
          self.filenames = file_paths
          self.total_files = len(file_paths)
          # initialize necessary variable
          self.term_frequency = {}
          self.document_frequency = {}
          self.inverse_document_frequency = {}
          self.file_to_word_map =self.tokenize_files()
          self.final_index = self.makeinverted_index(self.file_to_word_map)

    '''
    This function accomplice 3 task
    1)Convert file to word tokens and remove non-word character such as ' . " etc. and remove more than one blank space
    2)Using nltk remove stopwords (common word such as the , a )
    3)Using nltk to map diffrent word with same origin to original word  using port stemmer.
    '''
    def tokenize_files(self):
          file_to_word_map = {} # create empty dictionary
          for file_name in file_paths:
              file_pointer = open(file_name)
              file_content = file_pointer.read().lower()
              #https://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python
              filtered_content = re.sub(' +',' ',re.sub(r'\W+', ' ', file_content))

              final_words = []

              for word in  filtered_content.split(" "):
                  if word not in stop_words:
                      final_words.append(pc.stem(word))
              file_to_word_map[file_name] = final_words
              self.document_frequency[file_name] = len(final_words)

          return file_to_word_map

    def makeinverted_index(self,file_to_word_map):
        file_wise_index = {}
        final_index = {}
        for file_name in file_to_word_map.keys():
            individual_file_index = {};
            current_position =0;
            for words in file_to_word_map[file_name]:
                if words in individual_file_index:
                    individual_file_index[words].append(current_position)
                else :
                     individual_file_index[words] = [current_position]
                current_position = current_position+1
                file_wise_index[file_name] = individual_file_index
        for file_name in file_wise_index.keys():
            for word in file_wise_index[file_name]:
                if word in final_index:
                    final_index[word][file_name] = file_wise_index[file_name][word]
                else:
                    temp_dictionary = {}
                    temp_dictionary[file_name] = file_wise_index[file_name][word]
                    final_index[word] = temp_dictionary
        return final_index

    def give_term_frequency(word,file_name):
        if self.final_index[word][file_name]







file_paths = ["/home/dhrumil/Desktop/Basic_Search_Engine/TextFiles/temp1.txt",
             "/home/dhrumil/Desktop/Basic_Search_Engine/TextFiles/temp2.txt"]
inv_index = Inverted_Index(file_paths)
print("hello dhrumil")
print(inv_index.final_index[pc.stem('nudity')])
