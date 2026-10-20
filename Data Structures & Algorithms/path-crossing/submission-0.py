class Solution:
    def isPathCrossing(self, path: str) -> bool:
        trail = []
        location = [0, 0]

        for direction in path:
            temp = location
            if direction == "N":
                location = [location[0]+1, location[1]]
            if direction == "S":
                location = [location[0]-1, location[1]]
            if direction == "E":
                location = [location[0], location[1]+1]
            if direction == "W":
                location = [location[0], location[1]-1]

            if temp in trail:
                return True

            trail.append(temp)

        return location in trail
            

            




