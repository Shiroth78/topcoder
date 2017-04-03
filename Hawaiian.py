# coding: utf-8

import sys


class Hawaiian:
	def getWords(self,sentence):

		ans = []	
		alphabet = ['a','e','i','o','u','h','k','l','m','n','p','w',
					'A','E','I','O','U','H','K','L','M','N','P','W']
		s = sentence.split()
		print s
		for i in range(len(s)):
			tmp = list(s[i])
			flag = False
			for j in range(len(tmp)):
				if tmp[j] not in alphabet:
					flag = True
					break
			if flag == False:
				ans.append(s[i])

		print ans 
		return ans 

'''
memo
文章を単語に分割→単語をアルファベットに分割→Hawaiian文字かどうか判定の処理
'''