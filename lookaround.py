


M = (
    (-1, 1), (0, 1), (1, 1),
    (-1, 0), (0, 0), (1, 0),
   (-1, -1), (0, -1), (1, -1)
)



def buildLookAround(w, h):
    #You will always start at NEGITIVE Width
    #Top Row's Y will always be MAX `h`
    M = []
    for y in range(-h, h+1):
        temp = []
        for x in range(-w, w+1):
            temp.append((x, -y))
        M.append(temp)
    return M






