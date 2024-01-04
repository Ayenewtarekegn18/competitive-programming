class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        chemistry = 0
        sum = 0
        i = 0
        j = len(skill) - 1
        skill.sort()
        while i <= j:
            if i == 0:
                sum = skill[i] + skill[j]
            elif sum != skill[i] + skill[j]:
                chemistry = -1
                break
            chemistry += (skill[i] * skill[j])
            i += 1
            j -= 1
        return chemistry

