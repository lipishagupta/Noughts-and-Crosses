 def GAME():	
	P1="p1"
	P2="p2"
	board=['','','','','','','','','']
	for i in range(9):
	N=input("enter the patner name")
	if N==P1:
	Player1=int(input("PLAYER 1ENTER THE NUMBER AT WHICH YOU WANT TO PLACE:"))
	board.pop(Player1)
	board.insert(Player1,"X")
	print(board[0],' | ',board[1],' | ',board[2],end='\n')
	print('--------------------------',end='\n')
	print(board[3],' | ',board[4],' | ',board[5],end='\n')
	print('--------------------------',end='\n')
	print(board[6],' | ',board[7],' | ',board[8],end='\n')
	if ((board[0] and board[1] and board[2]) or (board[3] and board[4] and board[5]) or (board[6] and board[7] and board[8]) or
	(board[2] and board[1] and board[0]) or (board[5] and board[4] and board[3]) or (board[8] and board[7] and board[6])or
	(board[0] and board[3] and board[6]) or (board[1] and board[4] and board[7]) or (board[2] and board[5] and board[8]) or
	(board[6] and board[3] and board[0]) or (board[7] and board[4] and board[1]) or (board[8] and board[7] and board[2])or
	(board[0] and board[4] and board[8]) or (board[2] and board[4] and board[6])or
	(board[8] and board[4] and board[0]) or (board[6] and board[4] and board[2])):
	break
	if N==P2:
	Player2=int(input("PLAYER2 ENTER THE NUMBER AT WHICH YOU WANT TO PLACE:"))
	board.pop(Player2)
	board.insert(Player2,"O")
	print(board[0],' | ',board[1],' | ',board[2],end='\n')
	print('--------------------------',end='\n')
	print(board[3],' | ',board[4],' | ',board[5],end='\n')
	print('--------------------------',end='\n')
	print(board[6],' | ',board[7],' | ',board[8],end='\n')
	if ((board[0] and board[1] and board[2]) or (board[3] and board[4] and board[5]) or (board[6] and board[7] and board[8]) or
	(board[2] and board[1] and board[0]) or (board[5] and board[4] and board[3]) or (board[8] and board[7] and board[6])or
	(board[0] and board[3] and board[6]) or (board[1] and board[4] and board[7]) or (board[2] and board[5] and board[8]) or
	(board[6] and board[3] and board[0]) or (board[7] and board[4] and board[1]) or (board[8] and board[7] and board[2])or
	(board[0] and board[4] and board[8]) or (board[2] and board[4] and board[6])or
	(board[8] and board[4] and board[0]) or (board[6] and board[4] and board[2])):
	break
	"""THIS IS FOR PLAYER 1"""
	if ((board[0] and board[1] and board[2]) or (board[3] and board[4] and board[5]) or (board[6] and board[7] and board[8]) or
	(board[2] and board[1] and board[0]) or (board[5] and board[4] and board[3]) or (board[8] and board[7] and board[6])or
	(board[0] and board[3] and board[6]) or (board[1] and board[4] and board[7]) or (board[2] and board[5] and board[8]) or
	(board[6] and board[3] and board[0]) or (board[7] and board[4] and board[1]) or (board[8] and board[7] and board[2])or
	(board[0] and board[4] and board[8]) or (board[2] and board[4] and board[6])or
	(board[8] and board[4] and board[0]) or (board[6] and board[4] and board[2])=='x'):
	print("Player1 Wins")
	else:
	print("Player 2")
	GAME()

