# coding: utf-8

#https://arena.topcoder.com/#/u/practiceCode/1475/3645/3946/1/1475

class Stitch:
	def stitch(self,A,B,overlap):
		
		#A,Bを取得して数値化
		a = []
		b = []
		for i in range(len(A)):
			a.append(list(A[i]))
			for j in range(len(a[i])):
				a[i][j] = ord(a[i][j])
		for i in range(len(B)):
			b.append(list(B[i]))
			for j in range(len(b[i])):
				b[i][j] = ord(b[i][j])
		#print a,b

		#一行だけ計算する関数
		def calpixel(p,q,overlap):
			ans = []
			#overlapしないp
			if len(p) > overlap:
				for i in range(len(p)-overlap):
					ans.append(p[i])
			#overlap部分
			for i in range(overlap):
				tmp = 1.0 * ((overlap+1-(i+1))*p[len(p)-overlap+i]+((i+1)*q[i]))/(overlap+1)
				ans.append(int(round(tmp)))
			#overlapしないq
			if len(q) > overlap:
				for i in range(len(q)-overlap):
					ans.append(q[i+overlap])
			print ans
			return ans

		#a,bを1行ずつ計算,テキスト化
		ans = []
		for i in range(len(a)):
			ans.append(calpixel(a[i],b[i],overlap))
			for j in range(len(ans[i])):
				ans[i][j] = chr(ans[i][j])
			ans[i] = ''.join(ans[i])
		print ans
		return ans


'''
memo
オーバーラップ部分の式は問題文ではi=1からだが、実装ではi=0からになっていることに注意する
文字はord()で整数にし、計算処理を行った後でstr()で再び文字に直す
'''







