# Principe du pipotron :
# - Partez d'un non terminal  N
# - Choisissez aléatoirement 1 règle qui commence par N -> tableau (to do)
# - Parcourez to do : remplacez par une une règle au hasard jusqu'à uniquement terminaux
# [ TEXTE ] -> [ PHRASE TEXTE ] -> [ SUJET VERBE COMPLEMENT ] -> [ il aime la bière ]

from random import choice


class Symbol:
	def __init__(self, symbol):
		self.symbol = symbol

	def __str__(self):
		return self.symbol


class Terminal(Symbol):
	pass


class NonTerminal(Symbol):
	pass


# --------------------------------------------------------------------------

sujets = [Terminal(x) for x in [
	"il",
	"elle",
	"le chat",
	"le chien",
	"l'araignée",
	"Thomas",
	"Manon",
	"Léo",
	"Quentin",
	"Guillaume",
	"Damien",
	"Antoine",
	"Mathias",
	"Thomas",
	"Volodia",
	"Alexandre",
	"Valentin",
	"Brandon",
	"Quentin",
	"Valentin",
	"Alexis",
	"Valentin",
	"Clovis",
	"Baptiste",
	"Arnaud",
	"Corenthin"]
		  ]

TEXTE = NonTerminal("TEXTE")
PHRASE = NonTerminal("PHRASE")
SUJET = NonTerminal("SUJET")
VERBE = NonTerminal("VERBE")
COMPLEMENT = NonTerminal("COMPLEMENT")

#rule composées de SEQUENCES composées de SYMBOLES
rules = {
	TEXTE: [
		[PHRASE, TEXTE],
		[],
	],
	
	PHRASE: [
		[SUJET, VERBE, COMPLEMENT, Terminal(".")]
	],
	
	SUJET: [[x] for x in sujets],
	COMPLEMENT: [[x] for x in sujets],
	
	VERBE: [
		[Terminal("mange")],
		[Terminal("aime")],
		[Terminal("tape")]
	]
}
	




def randomRuleFromSymbol(nt):
	return choice(rules[nt])


def generate(rule):
	t = []
	for s in rule:
		if isinstance(s, Terminal):
			# si c'est un terminal, on l'ajoute
			t.append(s)
		else:
			# si c'est une règle non-terminale (donc composée) alors on génère récursivement
			newRule = randomRuleFromSymbol(s)
			t.extend(generate(newRule))
	return t
#append ça rajoute 1 élément
#extend ça rajoute plusieurs éléments


text = " ".join(map(str, generate(rules[TEXTE][0])))
#generate génère à partir de cette règle, et nous renvoie une liste de Terminal
#ensuite pour chaque terminal on convertir en chaine (via map)
#et ensuite cette liste de chaines on la convertit en une grosse chaine en collant 
#les éléments ensemble avec des espaces (via join)


print(text)