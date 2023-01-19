# Copyright Bud Patterson, 2022, 2023

# This file is part of Drawer.
# Drawer is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# Drawer is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with Drawer. If not, see <https://www.gnu.org/licenses/>. 


#M = (
#    (-1, 1), (0, 1), (1, 1),
#    (-1, 0), (0, 0), (1, 0),
#   (-1, -1), (0, -1), (1, -1)
#)



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






