startord="hej"
for a in range(3):
	s = list(startord)
	for i in range(26):
		s[a]=chr(97+i)
		ordet="".join(s)
		print(ordet)
	s[a]=chr(228)
	print(s)
	s[a]=chr(229)
	print(s)
	s[a]=chr(246)
	print(s)
		# print(chr(228))
		# print(chr(229))
		# print(chr(246))
