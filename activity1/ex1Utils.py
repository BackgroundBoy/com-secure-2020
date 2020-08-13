import hashlib
import requests
from typing import List


class Password:
    """
        Password object: *Sad permutation noise*

        params:

            - string(str): original string 
            - permutedList(list): list of permuted strings 
    """

    def __init__(self, string: str):
        super().__init__()
        self.string = string
        self.permutedList = []

    def _permute(self, idx: int, currentString: str):
        if idx >= len(self.string):
            self.permutedList.append(currentString)
        else:
            # gen upper/lower
            self._permute(idx+1, currentString+self.string[idx].lower())
            self._permute(idx+1, currentString+self.string[idx].upper())
            # gen i/l -> 1 and o -> 0
            if self.string[idx].lower() == "o":
                self._permute(idx+1, currentString+"0")
            if self.string[idx].lower() == "i" or \
                    self.string[idx].lower() == "l":
                self._permute(idx+1, currentString+"1")

    def getPermutedList(self) -> List[str]:
        self._permute(0, "")
        return self.permutedList


def retrieveDict(url: str = None):
    if not url:
        return None
    req = requests.get(url)
    wordText = set(req.text.split("\n"))
    wordText.remove("")
    wordText = list(wordText)
    return wordText


def sha1MyDict(dictList: List[str], target: str) -> (bool, str):
    found = False
    original = ""
    for string in dictList:
        hashed = hashlib.sha1(string.encode()).hexdigest()
        if hashed == target:
            found = True
            original = string
            break
    return (found, original)


def md5MyDict(dictList: List[str], target: str) -> (bool, str):
    found = False
    original = ""
    for string in dictList:
        hashed = hashlib.md5(string.encode()).hexdigest()
        if hashed == target:
            found = True
            original = string
            break
    return (found, original)


