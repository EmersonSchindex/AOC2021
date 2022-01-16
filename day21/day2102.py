def p1(pos):
	dice = 1
	score = [0, 0]
	while True:
		for player in range(2):
			newpos = (pos[player] + dice+dice+1+dice+2 - 1) % 10 + 1
			dice += 3
			score[player] += newpos
			pos[player] = newpos

			if score[player] > 999:
				return score[1-player]*(dice-1)

def p2(pos):
	dice = 1
	score = [0, 0]
	while True:
		for player in range(2):
			for quantum in range(3):
       
				newpos = (pos[player] + dice+dice+1+dice+2 - 1) % 10 + 1
				dice += 3
				score[player] += newpos
				pos[player] = newpos

				if score[player] > 999:
					return score[1-player]*(dice-1)

def main():
    print(p1([4, 8])) # 2, 1

if __name__ == '__main__':   
    main()