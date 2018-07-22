import DES_Parameter as DES

ausgabeArr = {}
# Hilfs-Funktionen
################################################################
def von_binary_array_zur_int(arr):
	#print(arr, end="\t=>\t")
	zahl = int("".join(str(i) for i in arr), 2)
	#print(zahl)
	return zahl

def von_int_zur_binary_array(integer):
	#print("\t\t",integer, end="\t=>\t")
	arrB = bin(int(integer)).replace('0b', '').zfill(4)
	#print(arrB)
	return [int(arrB[0]),int(arrB[1]),int(arrB[2]),int(arrB[3])]


def routiereArr(array, routiernummer, direction = 0):
	if direction == 0:
		return array[routiernummer:] + array[:routiernummer]
	else:
		return array[-routiernummer:]+array[:-routiernummer]


# Funktionen
################################################################

def subsitution_von_s(s_te,getArr):
	# 1-te getArr[0],  6-te getArr[5]		// Zeile
	# 2 bis 4-te getArr[1:5]				// Spalte
	#print("",end="\t\t")
	zeile 	= von_binary_array_zur_int([getArr[0],getArr[5]])
	#print("",end="\t\t")
	spalte 	= von_binary_array_zur_int(getArr[1:5])
	int_von_S = DES.S[(s_te-1)][(zeile*16+spalte)]
	#print("",end="\t\t")
	#print("Tabelle von S",s_te,"=>",[zeile,spalte],"=>",int_von_S)
	return [von_int_zur_binary_array(int_von_S),zeile,[getArr[0],getArr[5]],spalte,getArr[1:5],int_von_S]


def permutation(arr_to_Sub, Sub_array):
	#print("########################")
	#print("#   permutation aufruf", end="\n######################## \n")
	returnArr = []
	for i in range(len(Sub_array)):
		returnArr.append(arr_to_Sub[Sub_array[i]-1])
	return returnArr


def transformation(key, i):
	shifts = 0
	if(i in [1,2,9,16]):
		shifts = 1
	else:
		shifts = 2

	links	= routiereArr(key[0], shifts)
	rechts 	= routiereArr(key[1], shifts)

	C_i = links
	D_i = rechts
	ausgabeArr['LSl'].append(C_i)
	ausgabeArr['LSr'].append(D_i)
	funfsechs_arr = []
	funfsechs_arr.extend(C_i)
	funfsechs_arr.extend(D_i)
	return funfsechs_arr

def teileArr(arr_to_half):
	#print("########################")
	#print("#   teileArr aufruf", end="\n######################## \n")
	haelfte = int(len(arr_to_half)/2)
	arr_left = arr_to_half[:haelfte]
	arr_right = arr_to_half[haelfte:]
	return [arr_left,arr_right]


def f_funktion(right,key):
	#print("########################")
	#print("#   f_funktion aufruf", end="\n######################## \n")
	#print("rechte Seite VOR E ",right)
	rechte_E = permutation(right, DES.E)
	ausgabeArr['Expansion'].append(rechte_E)
	#print("rechte Seite nach E",rechte_E)
	#print("Schlussel          ",key)
	xor_rechte_key = []
	for z in range(len(rechte_E)):					#XOR 48-Right ^ 48-Key
		xor_rechte_key.append(int(rechte_E[z]^key[z]))   

	#print("r_i XOR k_i        ",xor_rechte_key)
	ausgabeArr['f_xor'].append(xor_rechte_key)
	s_boxen = []
	zweidrei_arr = []
	for x in range(1,9):
			#print("########################")
			#print("#   6 -> 4 Bit  | S",x, end="\n########################\n")
			sechser_arr = xor_rechte_key[6*(x-1):6*x]
			#print("Input : S",x,"     =>", sechser_arr)
			vierer_arr = subsitution_von_s(x, sechser_arr)
			s_boxen.append([sechser_arr,vierer_arr])
			#print("Output: S",x,"    =>", vierer_arr)
			zweidrei_arr.extend(vierer_arr[0])
	#print("########################")
	#print("#   Finish 6 -> 4 ", end="\n######################## \n")
	#print("32-Bit vor P     ", zweidrei_arr)
	ausgabeArr['f_s_boxen'].append(s_boxen)
	ausgabeArr['f_32_bit'].append(zweidrei_arr)
	sub_P = permutation(zweidrei_arr, DES.P)
	ausgabeArr['f_permutation'].append(sub_P)
	#print("32-Bit nach P    ",sub_P)
	return sub_P


def DES_encrypt(klartext_x, schlussel_k):
	#print("Klartext vor IP    ",klartext_x)
	ausgabeArr['Klartext']  = klartext_x
	eingangsbits = permutation(klartext_x, DES.IP)
	#print("Klartext nach IP   ",eingangsbits)
	ausgabeArr['Eingang_IP']  = eingangsbits
	ausgabeArr['Schlussel']  = schlussel_k
	#print("Schlussel vor PC_1 ",schlussel_k)
	schlussel_k  = permutation(schlussel_k, DES.PC_1)
	ausgabeArr['PC-1']  = schlussel_k
	#print("Schlussel NACH PC_1",schlussel_k)
	ausgabeArr['L'] = []
	ausgabeArr['R'] = []
	ausgabeArr['C'] = []
	ausgabeArr['D'] = []
	ausgabeArr['LSl'] = []
	ausgabeArr['LSr'] = []
	ausgabeArr['PC-2-INPUT'] = []
	ausgabeArr['key'] = []
	ausgabeArr['Expansion'] = []
	ausgabeArr['f_xor'] = []
	ausgabeArr['f_32_bit'] = []
	ausgabeArr['f_s_boxen'] = []
	ausgabeArr['f_permutation'] = []
	ausgabeArr['xor_nach_f'] = []
	#TODO: FOR
	################################################################
	for runde in range(0,16):
		eingangsbits = teileArr(eingangsbits)
		#print("left/Right text   ",eingangsbits)
		ausgabeArr['L'].append(eingangsbits[0])
		ausgabeArr['R'].append(eingangsbits[1])
		#TODO: Schlusse_k_Transformer
		schlussel_k = teileArr(schlussel_k)
		ausgabeArr['C'].append(schlussel_k[0])
		ausgabeArr['D'].append(schlussel_k[1])

		#print("left/Right key     ",schlussel_k)
		schlussel_k 	= transformation(schlussel_k,runde+1)
		ausgabeArr['PC-2-INPUT'].append(schlussel_k)
		schlussel_k_i 	= permutation(schlussel_k, DES.PC_2)
		ausgabeArr['key'].append(schlussel_k_i)

		# eingangsbits[0] left
		# eingangsbits[1] right 

		output_f = f_funktion(eingangsbits[1] ,schlussel_k_i)

		neuer_rechte_seite = []
		for z in range(len(eingangsbits[0])):
			neuer_rechte_seite.append(int(eingangsbits[0][z]^output_f[z])) # left XOR f_output

		ausgabeArr['xor_nach_f'].append(neuer_rechte_seite)
		#print("rechts           ",eingangsbits[0])
		#print("f_output         ",output_f)
		neuer_zweidrei_arr = []
		neuer_zweidrei_arr.extend(eingangsbits[1])    #Linke-Hälfe
		neuer_zweidrei_arr.extend(neuer_rechte_seite)  #Rechte-Hälfe
		#print("righ XOR f_output",neuer_rechte_seite)

		#print("Neu links        ", eingangsbits[1])
		#print("Neu rechts       ", neuer_rechte_seite)
		eingangsbits = neuer_zweidrei_arr;
		#print("neu VOR IP_1     ", eingangsbits)

	################################################################
	#TODO: FOR-END
	eingangsbits = teileArr(eingangsbits)
	# print("left/Right text   ",eingangsbits)
	ausgabeArr['L'].append(eingangsbits[0])
	ausgabeArr['R'].append(eingangsbits[1])
	neuer_zweidrei_arr = []
	neuer_zweidrei_arr.extend(eingangsbits[1])  # Linke-Hälfe
	neuer_zweidrei_arr.extend(neuer_rechte_seite)#Rechte-Hälfe
	eingangsbits = neuer_zweidrei_arr;
	ausgabeArr['ausgangspermutation_input'] = neuer_zweidrei_arr
	ausgangspermutation = permutation(eingangsbits, DES.IP_1)
	ausgabeArr['Ausgang_IP_1']  = ausgangspermutation
	#print("neu NACH IP_1    ",ausgangspermutation)
	return ausgangspermutation


def zeigeTabelle(name):
	des = 	{
				"IP" : [DES.IP, 8],
				"IP_1" : [DES.IP_1, 8],
				"E" : [DES.E, 6],
				"P" : [DES.P, 8],
				"IP" : [DES.IP, 8],
				"S_1" : [DES.S[0], 16],
				"S_2" : [DES.S[1], 16],
				"S_3" : [DES.S[2], 16],
				"S_4" : [DES.S[3], 16],
				"S_5" : [DES.S[4], 16],
				"S_6" : [DES.S[5], 16],
				"S_7" : [DES.S[6], 16],
				"S_8" : [DES.S[7], 16],
				"PC_1" : [DES.PC_1, 8],
				"PC_2" : [DES.PC_2, 8]
			}
	ausgabe = name +" ("+ str(len(des[name][0])) +" Bit) Permutation\n------------------------------------------------------"

	for i,z in enumerate(des[name][0]):
		if(i%des[name][1]==0):
			ausgabe += "\n"
		ausgabe+=str(z).zfill(2)+" "
	return ausgabe+"\n------------------------------------------------------\n"