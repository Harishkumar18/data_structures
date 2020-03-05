class AnagramMappings:
    def index_mapping(self, a, b):
        mappings = []
        for element in range(len(a)):
            mappings.append(b.index(a[element]))
        return mappings

    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        lookup = {val: i for i, val in enumerate(B)}
        return [lookup[val] for val in A]


A = [12, 46, 32, 50, 28]
B = [50, 12, 32, 28, 46]
anagram_obj = AnagramMappings()
# get_mappings = anagram_obj.index_mapping(A, B)
get_mappings = anagram_obj.anagramMappings(A, B)
print(get_mappings)