from typing import List

class WordDictionary:
	def __init__(self):
		self.data = {}

	def addWord(self, word):
		word = word + '$'
		trie = self
		for c in word:
			if c in trie.data:
				trie = trie.data[c]
			else:
				trie.data[c] = WordDictionary()
				trie = trie.data[c]

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




obj = WordDictionary()
print(obj.addWord("apple"))
print(obj.search("apple"))
print(obj.search("app"))
print(obj.addWord("app"))
print(obj.search("app"))
print(obj.search("..p.e"))
