import re
from typing import List
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        processed_paragraph = re.sub(r'[^\w]', ' ', paragraph).lower().split()
        words = [word for word in processed_paragraph if word not in banned]
        return Counter(words).most_common(1)[0][0]


print(Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
