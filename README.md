# Text Preprocessing in Bangla and English
Text preprocessing is done by following few steps which are needed for transferring text from human language to machine-readable format. Traditional text preprocessing follows-
- Converting all letters to lower or upper case
- Converting numbers into words or removing numbers
- Removing punctuations, accent marks and other diacritics
- Removing white spaces
- Expanding abbreviations
- Removing stop words, sparse terms, and particular words
- Text canonicalization


# Purpouse!
This script was created to preprocess text that were obtained from several movie subtitles which. The origin language is english where the translated version is bangla.

Here the following techniques were considered-
**English**:
  - All text to lowercase
    - Convert text to lowercase of an input sentence. 
  - Remove all numbers
    - Automatically remove numbers if they are not relevant to the analyses. Usually, regular expressions are used to remove numbers.
  - Remove all punctuations
    - It removes this set of symbols [!”#$%&’()*+,-./:;<=>?@[\]^_`{|}~] 
  - Remove leading and ending whitespaces
    - By using strip() function leading and ending spaces are removed
  - Tokenization
    - In this process the given text is splitted into smaller pieces called tokens. Words, numbers, punctuation marks, and others can be considered as tokens. 
  - Stop words removal
    - Removes the most common words in a language like “the”, “a”, “on”, “is”, “all” does not carry important meaning. Here, Natural Language Toolkit (NLTK) a suite of libraries and programs for symbolic and statistical natural language processing was used to recognize "stop_words".
  - Stemming
    - It is a process of reducing words to their word stem, base or root form (for example, places — place, watched — watch). 
  - Lemmatization
    - Similar as  stemming, lemmatization reduces inflectional forms to a common base form.
  - Part of speech tagging (POS)
    - It assigns parts of speech to each word of a given text (such as nouns, verbs, adjectives, and others) based on its definition and its context. 
  - Chunking
    - It is a natural language process that identifies constituent parts of sentences (nouns, verbs, adjectives, etc.) and links them to higher order units that have discrete grammatical meanings (noun groups or phrases, verb groups, etc.)
  - Named entity recognition
     - It tries to find named entities in text and classify them into pre-defined categories (names of persons, locations, organizations, times, etc.).

**Bangla**:
In case of normalizing bengali texts only tokenizing was used as other modules are under developed.

### Installation
The scripts requires some libraries to be installed before executing. By running the following code all the required modules can be installed.
```sh
$ pip install -r requirements.txt
```

Some manual installation may required for some ntlk libraries.
### Procedures

-> First the required csv file that contains the input text need to locate to the base directory.
->Then from the manually given column names texts were divided into two dataframes.
->Based on the input texts and the required normalization procedure pre-processing techniques were implied.
->From the output form of preprocessed text again two dataframes were created to insert the preprocessed data to an excel file.

### Development
[References] 
[Text Preprocessing in Python: Steps, Tools, and Examples](https://www.medium.com/@datamonsters/text-preprocessing-in-python-steps-tools-and-examples-bf025f872908)

**Thank You!**

