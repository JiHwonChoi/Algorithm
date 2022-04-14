places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
ans=[]
direction=[(1,0),(-1,0),(0,1),(0,-1)]


for room in places:
    # print(room)
    roomflag=0
    for rowidx, row in enumerate(room):
        # print(rowidx,row)
        for seatidx, seat in enumerate(row):
            # print(seatidx,seat)
            if(seat=='O'): #O의 상하좌우로 있나 P가 두개이상 있나 확인하기
                findp=[]
                for (a,b) in direction:
                    if( 0<=rowidx+a<5 and 0<=seatidx+b<5):
                        findp.append(room[rowidx+a][seatidx+b])
                pflag=0
                for x in findp:
                    if(x=='P'):
                        pflag+=1
                if(pflag>1):#P 가 두개이상 있으면
                    # print('roomflag',rowidx,seatidx,findp)
                    roomflag=1
                    break
            elif(seat=='P'):
                findp=[]
                for (a,b) in direction:
                    if( 0<=rowidx+a<5 and 0<=seatidx+b<5):
                        findp.append(room[rowidx+a][seatidx+b])
                pflag=0
                for x in findp:
                    if(x=='P'):
                        roomflag=1
                        break
        if(roomflag):
            break
    if(roomflag):
        ans.append(0)
    else:
        ans.append(1)
    
print(ans)
                    
                        
                    