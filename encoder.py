dico = [
	 ("a" , "·−"),
	 ("b" , "−···"),
	 ("c" , "−·−·"),
	 ("d" , "−··"),
	 ("e" , "·"),
	 ("f" , "··−·"),
	 ("g" , "−−·"),
	 ("h" , "····"),
	 ("i" , "··"),
	 ("j" , "·−−−"),
	 ("k" , "−·−"),
	 ("l" , "·−··"),
	 ("m" , "−−"),
	 ("n" , "−·"),
	 ("o" , "−−−"),
	 ("p" , "·−−·"),
	 ("q" , "−−·−"),
	 ("r" , "·−·"),
	 ("s" , "···"),
	 ("t" , "−"),
	 ("u" , "··−"),
	 ("v" , "···−"),
	 ("w" , "·−−"),
	 ("x" , "−··−"),
	 ("y" , "−·−−"),
	 ("z" , "−−··"),
	 ("1" , "·−−−−"),
	 ("2" , "··−−−"),
	 ("3" , "···−−"),
	 ("4" , "····−"),
	 ("5" , "·····"),
	 ("6" , "−····"),
	 ("7" , "−−···"),
	 ("8" , "−−−··"),
	 ("9" , "−−−−·"),
	 ("0" , "−−−−−")
]

# for a, b in dico:
# 	print(a, b)

def encode(text):
	for l in text:
		for a, b in dico:
			if l == a:
				print(b, end="")
				print(' ', end="")
	print('')

encode("votre texte ici")