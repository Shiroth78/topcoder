# coding: utf-8

import sys

class AB:
	def createString(self, N, K):
		print N,K
		#dataをすべてBとして作る→Kの値は０
		data = ["B" for i in range(N)]

		#dataに対するKの値をチェック
		#すべてのAに対して、後ろのBの数をカウントすればよい	
		def checkK(data):
			cnt = 0
			for i in range(N):
				if data[i] == "A":
					for j in range(i,N):
						if data[j] == "B":
							cnt += 1
			return cnt

		#dataのKと与えられたKの比較
		#一致しなければ後ろの1個をAに変え、それを1個ずつ前にずらす(dataのKの値が1ずつ増える)
		for i in range(N):
			for j in range(N-i):
				if checkK(data) == K:
					for k in range(len(data)):
						sys.stdout.write(data[k])
					return "".join(data)
					sys.exit()
				else:
					if j == 0:
						data[N-1] = "A"
					data[N-1-(j+1)],data[N-1-j] = data[N-1-j],data[N-1-(j+1)]
				print data

		print ""
		return ""

'''
memo
実際にはNの半分以上がAになれば後はKの値は減っていくので、もう少し処理を軽くすることも出来る
'''




