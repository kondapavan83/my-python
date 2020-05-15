import string
def ispangram (s,alpbt=string.ascii_lowercase):
    return (set (s.lower())  == set (alpbt))
