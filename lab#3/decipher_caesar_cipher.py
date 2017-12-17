from numpy import *
from string import maketrans

def translator(text,alphabet,key):
	transtab = maketrans(alphabet,key)
	return text.translate(transtab)

def caesar_decode(ciphertext,s):
	alpha="abcdefghijklmnopqrstuvwxyz"
	return translator(ciphertext,alpha,alpha[-s:]+alpha[:-s])

class frequency_analysis:
	def __init__(self, ciphertext):
		self.cor=[0.64297,0.11746,0.21902,0.33483,1.00000,0.17541,
		0.15864,0.47977,0.54842,0.01205,0.06078,0.31688,0.18942,
		0.53133,0.59101,0.15187,0.00748,0.47134,0.49811,0.71296,
		0.21713,0.07700,0.18580,0.01181,0.15541,0.00583]
		self.ciphertext=ciphertext.lower()
		self.freq()
		self.min_error()
		self.key=self.minimum[0]
		self.solution=caesar_decode(self.ciphertext,self.minimum[0])

	def freq(self):
		self.arr=zeros(26,float64)
		for l in self.ciphertext:
			x=ord(l)
			if (x>=97 and x<=122):
				self.arr[x-97]+=1.0
		self.arr/=max(self.arr)

	def error(self):
		e=0
		for i in range(0,len(self.arr)):
			e+=abs(self.arr[i]-self.cor[i])**2
		return e

	def min_error(self):
		self.minimum=[0,10000]
		for rot in range(0,25):
			e=self.error()
			print rot,e
			if e<self.minimum[1]:
				self.minimum[1]=e
				self.minimum[0]=rot
			x=self.arr[-1]
			del self.cor[-1]
			self.cor.insert(0,x)

text1 = "AB ZNRL MAX WXTWEBGX YHK MABL ETUHKTMHKR BL MAX MPXGMBXMA HY WXVXFUXK B PHNEW EBDX MH PBLA RHN ZHHW ENVD PBMA BM TGW ATOX T GBVX EBYX"
text2 = """
        WKHSWEC: WI XKWO SC WKHSWEC NOMSWEC WOBSNSEC, MYWWKXNOB YP DRO KBWSOC YP DRO XYBDR,
        QOXOBKV YP DRO POVSH VOQSYXC, VYIKV COBFKXD DY DRO DBEO OWZOBYB, WKBMEC KEBOVSEC.
        PKDROB DY K WEBNOBON CYX, RECLKXN DY K WEBNOBON GSPO. KXN S GSVV RKFO WI FOXQOKXMO,
        SX DRSC VSPO YB DRO XOHD.
        """
text3 = """
        XOXKR IETG BL MH UX VHGLBWXKXW, XOXKR XQIXWBXGM MKBXW TGW XOXKR FXMAHW MTDXG UXYHKX
        FTMMXKL TKX UKHNZAM MH MABL ETLM XQMKXFBMR. ZHHW HYYBVXKL WXVEBGX ZXGXKTE XGZTZXFXGML
        PAXKX MAX HWWL TKX MHH ZKXTM, TGW IKXYXK MAX XFIEHRFXGM HY LMKTMTZXF TGW YBGXLLX MH
        WXLMKHR MAX XGXFR TL FNVA TL IHLLBUEX PBMAHNM XQIHLBGZ MAXBK HPG YHKVXL.
        """
text4 = """
        RD QTAJ KTW YMJ WTRFS JRUNWJ NX ZSIJSNFGQD LWJFYJW YMFS KTW RDXJQK.
        YMJ LWJFYJXY JRUNWJ JAJW YT MFAJ JCNXYJI. N UQJILJ RD JYJWSFQ XJWANYZIJ
        FSI N FR KTWJAJW GTZSI YT XJWAJ NY, NS QNKJ FSI NS IJFYM. YMJD MFAJ RJWJQD LNAJS ZX:
        WTFIX, HJSYWFQ MJFYNSL, HTSHWJYJ, YMJ HFQJSIFW, FSI KQZXMNSL YTNQJYX FSI XJBJWX.
        """
text1_FA = frequency_analysis(text1)
text2_FA = frequency_analysis(text2)
text3_FA = frequency_analysis(text3)
text4_FA = frequency_analysis(text4)

print ("First decrypted text is: " + text1_FA.solution + "\n")
print ("Second decrypted text is: " + text2_FA.solution + "\n")
print ("Third decrypted text is: " + text3_FA.solution + "\n")
print ("Fourth decrypted text is: " + text4_FA.solution + "\n")
