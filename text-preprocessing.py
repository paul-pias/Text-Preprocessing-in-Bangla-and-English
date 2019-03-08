"""Text Pre-processing techniques for English and Bengali Language

This script allows the users to retrieve both bengali and english text from csv file to execute pre-process text based on their particular criteria.

This tool accepts comma separated value files (.csv) as well as excel
(.xlsx) files.

This script requires that `pandas`,'nlltk', 'cltk', 'textblob' be installed within the Python
environment you are running this script in.

@author Pias Paul
"""


import nltk
from nltk import pos_tag, ne_chunk
import pandas as pd
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
from cltk.tokenize.sentence import TokenizeSentence

"""
English Text Pre-processing
First english text were retrieved using panda to create data-frame
"""
input_frame = pd.read_csv('eng2ben.csv',encoding = "ISO-8859-1")  # Loading text from csv file
# input_frame = pd.read_excel("/yourpath/input.xlsx")  # Loading text from excel file
eng_column = input_frame['english_version']  # Retrieving english text from input file
eng_sentence= eng_column.str.cat(sep=', ')  # Insert all text to a single paragraph


def lower_case(text):
    """Gets the spreadsheet's header column named 'english_version' and convert all text to lowercase

        Parameters
        ----------
        text : str
            The texts retrieved from the spreadsheet

        Returns
        -------
        list
            a list of strings that are converted to lowercase
        """
    x = []
    for line in text:
        l_case = line.lower()
        x.insert(0,l_case)
    return x[::-1]


def no_digit(text):
    """Gets the spreadsheet's header column named 'english_version' and remove numbers

            Parameters
            ----------
            text : str
                The texts retrieved from the spreadsheet

            Returns
            -------
            list
                a list of strings that contains no digits
            """
    x = []
    for line in text:
        no_dig = ''.join([i for i in line if not i.isdigit()])
        x.insert(0, no_dig)
    return x[::-1]


def no_punctuation(text):
    """Gets the spreadsheet's header column named 'english_version' and remove punctuations

                Parameters
                ----------
                text : str
                    The texts retrieved from the spreadsheet

                Returns
                -------
                list
                    a list of strings that are converted to lowercase
                """
    x = []
    for line in text:
        no_punc = line.translate(str.maketrans('', '', string.punctuation))
        x.insert(0, no_punc)
    return x[::-1]


def no_whitespace(text):
    """Gets the spreadsheet's header column named 'english_version' and remove whitespace"

                    Parameters
                    ----------
                    text : str
                        The texts retrieved from the spreadsheet

                    Returns
                    -------
                    list
                        a list of strings that contains no ending and starting whitespace
                    """
    x = []
    for line in text:
        no_space = line.strip()
        x.insert(0, no_space)
    return x


def tokenize(text):
    """Gets the spreadsheet's header column named 'english_version' and tokenize each text based on that particular grammar"

                        Parameters
                        ----------
                        text : str
                            The texts retrieved from the spreadsheet

                        Returns
                        -------
                        list
                            a list of tokens
                        """
    x = []
    for line in text:
        words = word_tokenize(line)
        x.insert(0, words)
    return x[::-1]


def stop_words(text):
    """Gets the spreadsheet's header column named 'english_version' then identify and removes the stop words in given sentence"

                            Parameters
                            ----------
                            text : str
                                The texts retrieved from the spreadsheet

                            Returns
                            -------
                            list
                                a list of sentences that contains no stop words
                            """
    stop_words = set(stopwords.words('english'))
    x=[]
    for line in text:
        tokens = word_tokenize(line)
        result = [i for i in tokens if not i in stop_words]
        x.insert(0, result)
    return x[::-1]


def stemming(text):
    """Gets the spreadsheet's header column named 'english_version' then identify and modify words based on Porter stemming algorithm"

                                Parameters
                                ----------
                                text : str
                                    The texts retrieved from the spreadsheet

                                Returns
                                -------
                                list
                                    a list of strings in their stemmed form
                                """
    stemmer = PorterStemmer()
    x=[]
    for line in text:
        input_str = word_tokenize(line)
        for word in input_str:
            stemmer.stem(word)
        x.insert(0, input_str)
    return x[::-1]


def lemmatization(text):

    """Gets the spreadsheet's header column named 'english_version' then reduce inflectional forms to a common base form for each word"

                                 Parameters
                                 ----------
                                 text : str
                                     The texts retrieved from the spreadsheet

                                 Returns
                                 -------
                                 list
                                     a list of strings in their lemmatized form
                                 """
    lemmatizer = WordNetLemmatizer()
    x=[]
    for line in text:
        input_str = word_tokenize(line)
        for word in input_str:
            lemmatizer.lemmatize(word)
        x.insert(0, input_str)
    return x[::-1]


def pos(text):
    """Gets the spreadsheet's header column named 'english_version' and assign parts of speech to each word of given texts"

                                     Parameters
                                     ----------
                                     text : str
                                         The texts retrieved from the spreadsheet

                                     Returns
                                     -------
                                     list
                                         a list of strings in their Parts of Speech tags
                                     """
    x = []
    for line in text:
        result = TextBlob(line)
        x.insert(0, result.tags)
    return x[::-1]


def chunking(text):
    """Gets the spreadsheet's header column named 'english_version' and identifies constituent parts of sentences"

                                         Parameters
                                         ----------
                                         text : str
                                             The texts retrieved from the spreadsheet

                                         Returns
                                         -------
                                         list
                                             a list of strings of chunks
                                         """
    result = TextBlob(text)
    x = []
    reg_exp = "NP: { < DT >? < JJ > * < NN >}"
    rp = nltk.RegexpParser(reg_exp)
    result = rp.parse(result.tags)
    x.insert(0, result)
    return x[::-1]
    # result.draw()


def named_entity(text):
    """Gets the spreadsheet's header column named 'english_version' and find named entities in text and classify them into pre-defined categories"

                                             Parameters
                                             ----------
                                             text : str
                                                 The texts retrieved from the spreadsheet

                                             Returns
                                             -------
                                             list
                                                 a list of strings of corresponding named entities
                                             """
    x = []
    for line in text:
        entity = ne_chunk(pos_tag(word_tokenize(line)))
        x.insert(0,entity)
    return x[::-1]


new_eng_sentence = tokenize(eng_column)  # Pre-processed form of input english sentences



"""
Bangla Text Pre-processing
First bangla text were retrieved using panda to create data-frame
"""
input_ban_frame = pd.read_csv('eng2ben.csv',encoding = "UTF-8")  # Loading text from csv file
# input_ban_frame = pd.read_excel("/yourpath/input.xlsx")  # Loading text from excel file
ban_column = input_ban_frame['bengali_version'] # Retrieving text from input file
ban_sentence= ban_column.str.cat(sep=', ')


def bangla_tokenize(text):
    """Gets the spreadsheet's header column named 'bengali_version' and toeknize each text based on that particular grammar"

                        Parameters
                        ----------
                        text : str
                            The texts retrieved from the spreadsheet

                        Returns
                        -------
                        list
                            a list of tokens
                        """
    x = []
    for line in text:
        tokenizer = TokenizeSentence('bengali')
        bengali_text_tokenize = tokenizer.tokenize(line)
        x.insert(0,bengali_text_tokenize)
    return x[::-1]


new_ban_sentence = bangla_tokenize(ban_column) # Pre-processed form of input bengali sentences
# print(new_ban_sentence)
#
# print(new_eng_sentence)

output_frame = pd.DataFrame({'English Version' : new_eng_sentence, 'Bengali Version': new_ban_sentence})  # Splitting preprocessed text
print(output_frame)
# d.to_csv(r'E:/Blind/temp/temp.csv') #Writing the output frame to a csv file
output_frame.to_excel('./temp/temp.xlsx', engine='xlsxwriter')  # Writing the output frame to an excel file

