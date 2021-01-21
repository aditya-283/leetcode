from typing import List

class WordDictionary:
	def __init__(self):
		self.data = {}

	# def traverse(self, word: str):
	# 	iter = self
	# 	while word:
	# 		if word[0] in iter.data:
	# 			iter = iter.data[word[0]]
	# 			word = word[1:]
	# 		else:
	# 			break

	# 	return iter, word

	# def insert(self, word: str) -> None:
	# 	word = word + '$'
	# 	final_match, remainder = self.traverse(word)
	# 	iter = final_match
	# 	for c in remainder:
	# 		iter.data[c] =  WordDictionary()
	# 		iter = iter.data[c]


	def addWord(self, word):
		word = word + '$'
		trie = self.data
		for c in word:
			if c in trie:
				trie = trie[c]
			else:
				trie[c] = {}
				trie = trie[c]
		
		# return self.insert(word)


	def searchRec(self, word):
		if not word:
			return True
		if word[0] == '.':
			return any([trie.searchRec(word[1:]) for trie in self.data.values()])
		elif word[0] in self.data:
			return self.data[word[0]].searchRec(word[1:])
		else:
			return False

	def search(self, word):
		word = word + '$'
		return self.searchRec(word)




obj = Trie()
print(obj.insert("apple"))
print(obj.search("apple"))
print(obj.search("app"))
print(obj.insert("app"))
print(obj.search("app"))
print(obj.search("..p.r"))
