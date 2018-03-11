from ciphers import Cipher
import numpy

class ADFGVXCCipher(Cipher):
	wordlist = [
		list('abcdef'),
		list('hijklm'),
		list('nopqrs'),
		list('tuvwx'),
		list('yz0123'),
		list('456789'),
	]
	e_index = list('ADFGVXC')		


	def __init__(self):
		pass


	def encrypt(self, text):
		"""
		Method for encrypt the message with ADFGVX Cipher
		"""

		output=[]
		for letter in text:
			if letter==" ":
				output.append("  ")	
			for row in self.wordlist:
				for item in row:
					if item == letter:
						index1=self.wordlist.index(row)
						index2=row.index(item)
						output.append(self.e_index[index1]+self.e_index[index2])
		return("".join(output))
	

	def decrypt(self, text=""):
		"""
		Method for decrypt the message with ADFGVX Cipher
		"""
		output = []
		index1 = 0
		index2 = 0
		textlist = [text[i:i+2] for i in range(0, len(text), 2)]
		for letters in textlist:
			if letters=="  ":
				output.append(" ")
			else:	
				for code in self.e_index:
					if letters[0] == code:
						index1 = self.e_index.index(code)
					if letters[1] == code:
						index2 = self.e_index.index(code)
				output.append(self.wordlist[index1][index2])	
		print("".join(output))			

