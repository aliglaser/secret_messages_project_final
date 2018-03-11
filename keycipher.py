from ciphers import Cipher

class KeywordCipher(Cipher):
	keywordList=[]
	alphabet="abcdefghijklmnopqrstuvwxyz"
	new_rule = []
	encrypted = []
	decrypted = []

	def __init__(self, kwrd=""):
		self.kwrd = kwrd
		for letter in self.kwrd:
			if letter not in self.keywordList:
				self.keywordList.append(letter)

		rest_letters=(set(self.alphabet).difference(set(self.keywordList)))
		lrest=list(rest_letters)
		lrest.sort()
		self.new_rule.extend(self.keywordList)
		self.new_rule.extend(lrest)


	def encrypt(self, text=""):
		"""
		Method for encrypt the message with keyword cipher
		"""
		zipped = zip(self.alphabet, self.new_rule)
		zipped = list(zipped)
		for letter in text:
			if letter == " ":
				self.encrypted.append(" ")
			for oril, newl in zipped:
				if letter == oril:
					self.encrypted.append(newl)
		return("".join(self.encrypted))	
	


	def decrypt(self, text=""):
		"""
		Method for decrypt the message with keyword cipher
		"""
		zipped = zip(self.alphabet, self.new_rule)
		zipped = list(zipped)
		for letter in text:
			if letter == " ":
				self.decrypted.append(" ")
			for oril, newl in zipped:
				if letter == newl:
					self.decrypted.append(oril)
		return("".join(self.decrypted))		
					
