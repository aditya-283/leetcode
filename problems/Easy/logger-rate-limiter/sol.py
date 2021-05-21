from typing import List

class Logger:

	def __init__(self):
		self.lastReceivedAt = {}
		

	def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
		if message in self.lastReceivedAt and self.lastReceivedAt[message] + 10 > timestamp:
				return False
		self.lastReceivedAt[message] = timestamp
		return True

		


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)