# coding: utf-8

import sys

class AB:
	def createString(self, N, K):
		print N,K
		data = ["B" for i in range(N)]

		def checkK(data):
			cnt = 0
			for i in range(N):
				if data[i] == "A":
					for j in range(i,N):
						if data[j] == "B":
							cnt += 1
			return cnt

		anum = 0
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




