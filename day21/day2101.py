posplayer = [4, 8]
scoreplayer = [0, 0]
numberofrolls = 0
roll1 = 0
roll2 = 0
roll3 = 0

while scoreplayer[0] < 1000 and scoreplayer[1] < 1000:
    for i in range(2):
        roll1 = roll3 + 1
        if roll3 == 100:
            roll1 = 1
        roll2 = roll1 + 1
        if roll1 == 100:
            roll2 = 1
        roll3 = roll2 + 1
        if roll2 == 100:
            roll3 = 1
        totalroll = roll1 + roll2 + roll3
        numberofrolls += 3
        posplayer[i] += totalroll
        if posplayer[i] > 10 and posplayer[i] % 10 == 0:   
            posplayer[i] = 1
        if posplayer[i] > 10 and posplayer[i] % 10 != 0:   
            posplayer[i] = int(str(posplayer[i])[-1])

        scoreplayer[i] += posplayer[i]
        x = i

if scoreplayer[0] < scoreplayer[1]:
    result = scoreplayer[0] * numberofrolls
else:
    result = scoreplayer[1] * numberofrolls

print(result)