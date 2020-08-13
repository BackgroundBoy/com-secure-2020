import hashlib, time

from .ex1Utils import retrieveDict

def sha1String(x):
    return hashlib.sha1(x.encode()).hexdigest()

if __name__ == "__main__":

    d = retrieveDict(
        f"https://raw.githubusercontent.com/danielmiessler" +
        f"/SecLists/master/Passwords/Common-Credentials/10" +
        f"k-most-common.txt"
        )
   
    start = time.perf_counter()
   
    # non-Permuted rainbow table (key-value pair)
    rainbowPair = [(x,sha1String(x)) for x in d]

    end = time.perf_counter()
    time = end - start
    print(time)
    # write
    with open("./rainbow.txt","a") as f:
        f.write(f"Time: %f\n" % time)
        for (password, hashed) in rainbowPair:
            print(f"%s : %s" % (password,hashed), file=f)

    


    
