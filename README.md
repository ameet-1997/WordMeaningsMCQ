# Answering MCQs on Word Meanings
Find the closest meanings amongst multiple choice questions using Google Pretrained Word Vectors

### Method
The input to the program is 5 words, the question word, and 4 other words that constitute the options. The model does the following to find the correct answer.

* If the options are words, find cosine similarity between the question word and the options and choose the word which is closest.
* If the option is a sentence, the mean of cosine similarity is used as a measure of semantic similarity. This is motivated by [this](http://white.ucc.asn.au/publications/White2015SentVecMeaning.pdf) work on semantic similarity between words and sentences.

### Evaluation
I used the Magoosh Vocabulary Builder [app](https://gre.magoosh.com/builder/vocabulary/app#/sections) to test the vectors. It involves one question word and 4 options which can either be words or sentences.

### Using the code

Google Pretrained vectors used for this project can be downloaded [here](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?usp=sharing).

To run the code, use the following command
```shell
python driver.py --mode 2
```

This opens up an interactive shell for the user to play with. If the user prefers the program to read from the file, use the following command.
```shell
python driver.py --mode 1
```

### Performance
Performance of this method was unsatisfactory. Though the vectors did well if the options were words, they failed to do well on the long-standing problem of measuring semantic similarity between sentences and words. Newer methods in the future may hopefully help in improving this!