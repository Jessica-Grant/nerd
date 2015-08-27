import random



def makeBoard(board, word, pick):
	newboard = ''
	count = 0
	for char in word:	
		if char == pick:
			newboard += char
		else:
			newboard += board[count]
		count += 1
	return newboard
	
def main():
	wordlist = ['abate','abdicate','aberration','abhor','abstain','adversity','aesthetic','amicable','anachronistic','arid','asylum','benevolent','bias','boisterous','brazen','brusque','camaraderie','canny','capacious','capitulate','clairvoyant','collaborate','compassion','compromise','condescending','conditional','conformist','convergence','deleterious','demagogue','digression','diligent','discredit','disdain','divergent','empathy','emulate','enervating','ephemeral','evanescent','exemplary','extenuating','florid','forbearance','fortitude','fortuitous','foster','fraught','frugal','hackneyed','haughty','hedonist','hypothesis','impetuous','impute','inconsequential','inevitable','intrepid','intuitive','jubilation','lobbyist','longevity','mundane','nonchalant','opulent','orator','ostentatious','parched','perfidious','pragmatic','precocious','pretentious','procrastinate','prosaic','prosperity','provocative','prudent','querulous','rancorous','reclusive','reconciliation','renovation','restrained','reverence','sagacity','scrutinize','spontaneous','spurious','submissive','substantiate','subtle','superficial','superfluous','surreptitious','tactful','tenacious','transient','venerable','vindicate','wary']
	wrong = []
	word = wordlist[random.randrange(len(wordlist))]	
	
	board = makeBoard('_' * len(word),word,'*')
	print (board)
	while True:
		inp = input('pick a letter. ')
		print (inp)
		if inp in word:
			board = makeBoard(board,word,inp)
			if board == word:
				print ('Yes, it is ' + word + '!  You Win!!!!!')
				exit()
			else:	
				print (board)
			
		else:
			wrong.append(inp)
			print ("Nope.  You've chosen " + str(len(wrong)) + ' letters. ' + str(wrong))
			
main()
