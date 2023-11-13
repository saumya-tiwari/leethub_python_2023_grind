class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        answer = []

        for current in range(n):
            while answer and heights[answer[-1]] <= heights[current]:
                answer.pop()
            answer.append(current)
        return answer



        