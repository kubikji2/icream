
# function to get unique values
# '-> based on: https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python
# '-> NOTE: fastest from considered options
def unique(non_unique_list : list):
    return list(set(non_unique_list))

# parse string into categories in format:
# <some text> "[" <some tag1> "-" <some tag2> "-" ... "]" <some text>
def icream_parse_tags(s : str, _left_separator = "[", _right_separator = "]", _middle_separator = "-"):
    # splitting to separated levels
    _to_parse = s.split(_right_separator)[0].split(_left_separator)[1].split(_middle_separator)
    # parsing and modifying tags
    _tags = [" ".join(_ss.strip().lower().capitalize().split()) for _ss in _to_parse]
    return _tags

# parse email from mailto: 
def iceam_parse_email(s):
    ret = ""
    if type(s) == type(""):
        ret = s.replace("mailto:","")
    return ret

if __name__=="__main__":

    ws = ["[a-borka a borec-c]", " a dafda fda [ s st - - gfa    fda  fda fad    f. ] dafa fda"]

    for w in ws:
        print("{} -> {}".format(w,icream_parse_tags(w)))
