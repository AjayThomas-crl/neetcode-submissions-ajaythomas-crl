class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map=defaultdict(list)
        l: List[str] =[]
        for s in strs:
            val=0
            for c in s:
                val+=ord(c)-ord('a')+1
            map[val].append(s)
        for c in map.values():
            l.append(c)
        print(l)
        return l


        