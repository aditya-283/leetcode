from typing import List


# implement imperatively using dicts

class Trie:
	def __init__(self):
		self.data = {}

	def traverse(self, word: str):
		iter = self
		while word:
			if word[0] in iter.data:
				iter = iter.data[word[0]]
				word = word[1:]
			else:
				break

		return iter, word

	def insert(self, word: str) -> None:
		word = word + '.'
		final_match, remainder = self.traverse(word)
		iter = final_match
		for c in remainder:
			iter.data[c] =  Trie()
			iter = iter.data[c]


	def search(self, word: str) -> bool:
		word = word + '.'
		final_match, remainder = self.traverse(word)
		return not remainder


	def startsWith(self, prefix: str) -> bool:
		final_match, remainder = self.traverse(prefix)
		return not remainder


# Your Trie object will be instantiated and called as such:
obj = Trie()
print(obj.insert("apple"))
print(obj.search("apple"))
print(obj.search("app"))
print(obj.insert("app"))
print(obj.search("app"))
# print(obj.children['a'].children['d'].children)
# print('TESTING')
# print(obj.traverse("aditya"))
# print(obj.startsWith("ad"))
# print(obj.search("aditya"))