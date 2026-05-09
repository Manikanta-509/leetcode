class Solution(object):
    def checkIfPangram(self, sentence):
        alphabets='abcdefghijklmnopqrstuvwxyz'
        for i in alphabets:
            if i not in sentence:
                return False
                break
        return True