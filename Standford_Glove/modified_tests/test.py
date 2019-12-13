import argparse
import numpy as np

import word_analogy

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--vocab_file', default = 'vocab.txt', type = str)
	parser.add_argument('--vectors_file', default = 'vectors.txt', type = str)
	parser.add_argument('--encoding', default = 'utf-8', type = str)
	args = parser.parse_args()

	with open(args.vocab_file, 'r', encoding = args.encoding) as f:
		words = [x.rstrip().split(' ')[0] for x in f.readlines()]
	with open(args.vectors_file, 'r', encoding= args.encoding ) as f:
		vectors = {}
		for line in f:
			vals = line.rstrip().split(' ')
			vectors[vals[0]] = [float(x) for x in vals[1:]]

	vocab_size = len(words)
	vocab = {w: idx for idx, w in enumerate(words)}    
	ivocab = {idx: w for idx, w in enumerate(words)}
    
    
	filenames = ['capital-common-countries.txt','capital-world.txt', 'currency.txt',
        'city-in-state.txt', 'family.txt', 'gram1-adjective-to-adverb.txt',
                 'gram2-opposite.txt', 'gram3-comparative.txt', 'gram4-superlative.txt',
                 'gram5-present-participle.txt', 'gram6-nationality-adjective.txt',
                  'gram7-past-tense.txt', 'gram8-plural.txt', 'gram9-plural-verbs.txt',
        ]
    
	prefix = 'question-data/'
    
    correct_sem = 0; # count correct semantic questions
    correct_syn = 0; # count correct syntactic questions
    correct_tot = 0 # count correct questions
    count_sem = 0; # count all semantic questions
    count_syn = 0; # count all syntactic questions
    count_tot = 0 # count all questions
    full_count = 0 # count all questions, including those with unknown words

	for i in range(len(filenames)): # for each subset of word analogies to test  
		with open('%s%s' %(prefix, filenames[i]), 'r') as f: # for each 
			full_data = [line.rstrip().split(' ') for line in f]
			full_count += len(full_data)
			data = [x for x in full_data if all(word in vocab for word in x)]
			
			
			indices = np.array([[word for word in row] for row in data])
			
			three_words =  indices[:,0:3]
			strings = np.array([[three_words[i][0] + ' ' + three_words[i][1] + ' ' + three_words[i][2]] for i in range(len(three_words))])
			answers = indices[:,3]
			
			predictions = []
			W, vocab, ivocab = word_analogy.generate()
			vecs = {}
			for input_term in strings:                
				for idx, term in enumerate(input_term[0].split(' ')):
					if term in vocab:
						vecs[idx] = W[vocab[term],:]
					else:
						break
					
				vec_result = vecs[1] - vecs[0] + vecs[2]
				
				vec_norm = np.zeros(vec_result.shape)
				d = (np.sum(vec_result**2,)**(0.5))
				vec_norm = (vec_result.T/d).T

				dist = np.dot(W, vec_norm.T)
				
				for term in input_term[0].split(' '):
					index = vocab[term]
					dist[index] = -np.Inf
				a = ivocab[np.argsort(-dist)[0]]
				predictions += [a]
			predictions = np.array(predictions)

			val = (answers == predictions)
			print(filenames[i])
			print('Correct: %s' %sum(val))
			print('Accuracy: %s' %(sum(val)/len(answers)))
			print('-------------------------------------')
            
                	
			correct_tot += sum(val)
			count_tot += len(answers)
			
			print('Current Accuracy: %s' %(correct_sem/count_sem))
			print('-------------------------------------')
            
            # assign values for semantic tasks  
            if filenames[i] in semantic_tasks: 
                 correct_sem += sum(val) 
                 count_sem += sum(answers)
            elif filenames[i] in syntactic_tasks: 
                correct_syn += sum(val) 
                count_syn += sum(answers)
                 
                
            

if __name__ == "__main__": 
	main()
