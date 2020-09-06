mainboard = {'top-l':' ','top-m':' ','top-r':' ',
             'mid-l':' ','mid-m':' ','mid-r':' ',
             'bot-l':' ','bot-m':' ','bot-r':' '}
def printboard(board):
     print(board["top-l"]+'|'+board["top-m"]+'|'+board["top-r"])
     print('-+-+-')
     print(board["mid-l"]+'|'+board["mid-m"]+'|'+board["mid-r"])
     print('-+-+-')
     print(board["bot-l"]+'|'+board["bot-m"]+'|'+board["bot-r"])


turn='X'
for i in range(9):
    printboard(mainboard)
    print('turn for '+ turn + 'move to which space?' )
    move = input()
    mainboard[move]=turn
    if turn=='X':
        turn='O'
    else:
        turn='X'
printboard(mainboard)
    
