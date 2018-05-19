from gensim.models import KeyedVectors
from gensim.models import Word2Vec
import argparse
import pandas as pd
import copy
import datetime
import time
import os

class Meanings:

	def __init__(self, args):
		self.vectors = args.load
		self.mode = args.mode

	def calculate_score(self):
		# Check mode
		if self.mode == 2:
			self.interactive_shell()
			return

		# Read the datafile
		data = pd.read_csv('meanings.csv')

		# Load the model
		model = KeyedVectors.load_word2vec_format(self.vectors, binary=True)

		# Count of correct answers
		correct = 0.

		for w in range(data.shape[0]):
			# Minimum similarity score
			sim = 0.
			most_similar = "None"

			try:
				# Find similarity with respect to all the words
				for num_words in range(data.shape[1]-2):
					if model.similarity(data.iloc[w,1], data.iloc[w,1+num_words]) > sim:
						sim = model.similarity(data.iloc[w,1], data.iloc[w,1+num_words])
						most_similar = data.iloc[w,1+num_words]

				# Evaluate
				if most_similar == data.iloc[w,-1]:
					correct += 1
			except:
				continue

		# Print the score
		print("The accuracy is: "+str(float(correct)/data.shape[0]*100))


	def interactive_shell(self):
		print("Loading Vectors")

		# Load the model
		model = KeyedVectors.load_word2vec_format(self.vectors, binary=True)
		print("Done Loading Vectors")

		# Count of correct answers
		correct = 0.
		count = 0.

		while(True):
			# Minimum similarity score
			sim = 0.
			most_similar = "None"

			# Find similarity with respect to all the words
			print("Enter the question word. EXIT to exit")
			word = str(input())

			if word == "EXIT":
				break

			print("Enter 4 choices (sentence/words)")
			raw_choices = [str(input()) for i in range(4)]
			choices = [raw_choices[i].strip().split() for i in range(len(raw_choices))]

			# Sum of words are used as vectors
			for num_words in range(4):
				total_similarity = 0.
				for w in choices[num_words]:
					total_similarity += model.similarity(word, w)
				total_similarity /= len(choices[num_words])
				print(total_similarity)
				if total_similarity > sim:
					sim = total_similarity
					most_similar = raw_choices[num_words]

			# Enter the answer
			print("Enter the answer choice (1,2,3,4)")
			try:
				answer = int(input())
			except:
				continue
			count += 1

			# Check answer
			if raw_choices[answer-1] == most_similar:
				correct += 1
				print("Correct Answer")
			else:
				print("Incorrect Answer")
				

		# Print the score
		print("The accuracy is: "+str(float(correct)/count*100))