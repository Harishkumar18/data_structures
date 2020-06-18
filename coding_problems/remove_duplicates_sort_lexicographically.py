class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''Let's start with having three DS - counter for all the character frequecies in the string
                                            - a boolean list for the characters which we encounter so that we can skip them once they are encountered
                                            - a stack to store the lexicographically appropriate order of the string without the duplicates
        '''
        countList = [0]*26
        boolList = [False]*26
        stack = []
        '''Initializer the counter array'''
        for character in s:
            countList[ord(character) - ord('a')] += 1

        '''Traverse the given string'''
        for character in s:
            '''Decrease the count in the counter array as we came across this letter in a respective iteration'''
            countList[ord(character)- ord('a')] -= 1
            '''skip the character altogether if we have encountered it already'''
            if boolList[ord(character) - ord('a')]:
                continue

            '''if the stack is not empty and the iterator points to a character which is smaller than the last element in the stack --> we need to skip all the characters in the stack which are bigger than the current item. And we can only skip the items if there is a chance of encountering them in the future so we also should check for this in this while loop threshold statment'''
            while stack and character<stack[-1] and countList[ord(stack[-1]) - ord('a')] >0:
                '''the control comes here only if the logic found candidates to be removed from the stack. Hence lets just reverse the boolean values for these items as we should consider them fresh new items when we encounter them in the future so that we don't skip them'''
                boolList[ord(stack[-1]) - ord('a')] = False
                '''pop the item'''
                stack.pop()

            '''just add the item to the stack'''
            stack.append(character)

            '''Don't forget to switch the boolean key ON for this item, so we can skip it, if possible'''
            boolList[ord(character) - ord('a')] = True

        return ''.join(stack)



print(Solution().removeDuplicateLetters("babcdc"))