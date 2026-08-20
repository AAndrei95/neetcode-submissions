class Solution:
    def countSeniors(self, details: List[str]) -> int:
        seniors = 0

        for person in details:
            if int(person[11:13]) > 60:
                seniors += 1

        return seniors 