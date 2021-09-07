# sort selling amount by month by company

file = open("alux20-1-9.txt", "r", encoding="utf-16")

result = open("result.txt", "a", encoding="utf-16")

lines = file.readlines()

resultList = []

for lineNum in range(len(lines)):
    if lineNum == 0 or lineNum == 1:
        continue

    line = lines[lineNum]
    chunks = line.replace('\t', '').replace('\n', '').split('"')

    checker = 0

    if (len(resultList) == 0):
        resultList.append([chunks[3], [[chunks[0], chunks[1], chunks[6]]]])
        continue
    else:
        # Check if same company exists
        for i in range(len(resultList)):
            if (chunks[3] == resultList[i][0]):
                checker = 1
                checker2 = 0
                # Check if same year/month exists
                for k in range(len(resultList[i][1])):
                    if (chunks[0] == resultList[i][1][k][0] and chunks[1][:2] == resultList[i][1][k][1][:2]):
                        oldNum = int(resultList[i][1][k][2])
                        oldNum += int(chunks[6])
                        resultList[i][1][k][2] = str(oldNum)
                        checker2 = 1
                        break

                if (checker2 == 0):
                    resultList[i][1].append([chunks[0], chunks[1], chunks[6]])
                    break

        if (checker == 0):
            resultList.append([chunks[3], [[chunks[0], chunks[1], chunks[6]]]])

    if lineNum == 14878:
        break


for item in resultList:
    # print(item)
    result.write(str(item) + "\n\n")

file.close()
result.close()

