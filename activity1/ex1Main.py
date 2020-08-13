from .ex1Utils import retrieveDict, sha1MyDict, md5MyDict, Password


if __name__ == "__main__":
    target = "d54cc1fe76f5186380a0939d2fc1723c44e8a5f7"
    d = retrieveDict(
        f"https://raw.githubusercontent.com/danielmiessler" +
        f"/SecLists/master/Passwords/Common-Credentials/10" +
        f"k-most-common.txt"
        )
    
    d = [Password(string) for string in d]

    for password in d:
        # sha1
        results = sha1MyDict(
            password.getPermutedList(),
            target,
            )
        # md5
        # results = md5MyDict(
        #     password.getPermutedList(),
        #     target,
        #     )

        if results[0]:
            print(results[1]) # result is ThaiLanD lol
            break




