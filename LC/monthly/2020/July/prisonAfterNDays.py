class Prison:
     def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        seq = []
        currDay = cells
        while True:
            nextDay =[x for x in cells]
            for i in range(8):
                # print(i)
                if 0<i<7 and (currDay[i-1] == currDay[i + 1] == 1 or currDay[i-1] == currDay[i + 1] == 0):
                    nextDay[i] = 1
                else:
                    nextDay[i] = 0
            if seq and all((x == y for x,y in zip(seq[0],nextDay))):
                break
            seq.append(nextDay)
            print(nextDay)
            currDay = nextDay
        stateLen = len(seq)
        return seq[N%stateLen - 1]

