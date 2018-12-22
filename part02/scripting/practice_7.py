# Use an import statement at the top
import random
word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)
'''
# Add your function generate_password here
def generate_password():
    # It should return a string consisting of three random words 
    password = str()
    for i in range(3):
        # concatenated together without spaces
        random_index = random.randrange(0,len(word_list))
        password += word_list[random_index]
    return password
'''

# 查看文档的好处,发现更多实用的方法
def generate_password():
    return ''.join(random.sample(word_list,3))

# test your function
print(generate_password())