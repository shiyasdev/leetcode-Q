class Solution(object):
    def clearDigits(self, s):
        store = []

        for x in s:
            if x.isdigit():
                if store:
                    store.pop()
            else:
                store.append(x)

        return "".join(store)

        
        