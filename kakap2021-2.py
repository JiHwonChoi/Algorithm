places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
ans=[]
direction=[(1,0),(-1,0),(0,1),(0,-1)]


for room in places:
    for rowidx, row in enumerate(room):
        for seatidx, seat in enumerate(row):
            if(seat=='O'):
                findp=[]
                for (a,b) in direction:
                    if( 0<=rowidx+a<5 and 0<=seatidx+b<5):
                        findp.append(room[rowidx+a][seatidx+b])
                    