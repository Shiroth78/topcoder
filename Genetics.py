# coding: utf-8

#https://arena.topcoder.com/#/u/practiceCode/1413/2747/2973/1/1413

class Genetics:
	def getOffspring(self,g1,g2,dom):
		G1 = list(g1)
		G2 = list(g2)
		d = list(dom)

		ans = []
		for i in range(len(d)):
			if G1[i] == G2[i]:
				ans.append(G1[i])
			else:
				if d[i] == 'D':
					ans.append(G1[i].upper())
				elif d[i] == 'R':
					ans.append(G2[i].lower())

		return ''.join(ans)

'''
memo
逐一大文字か小文字か読み取るよりも.upper().lower()を使って処理してしまった方が楽？
'''