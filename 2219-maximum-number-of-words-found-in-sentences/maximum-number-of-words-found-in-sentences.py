class Solution(object):
    def mostWordsFound(self, sentences):
        maxwords=0
        for i in sentences:
            words=len(i.split())
            if words>maxwords:
                maxwords=words
        return maxwords
        