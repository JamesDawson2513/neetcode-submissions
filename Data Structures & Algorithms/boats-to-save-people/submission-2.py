class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        l = 0
        r = len(people) - 1
        boats = 0
        
        while l <= r:
            # If the lightest + heaviest fit together, put the lightest on the boat too
            if people[l] + people[r] <= limit:
                l += 1
            
            # The heaviest person ALWAYS gets a boat
            r -= 1
            boats += 1
            
        return boats

        