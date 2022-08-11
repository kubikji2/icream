from datetime import datetime, date, time, timedelta, tzinfo
from pytz import UTC # timezone

# function to get unique values
# '-> based on: https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python
# '-> NOTE: fastest from considered options
def unique(non_unique_list : list):
    return list(set(non_unique_list))

# function to replace multiple spaces and replace spaces on the beginning and the end
# '-> inspired by: https://stackoverflow.com/questions/2077897/substitute-multiple-whitespace-with-single-whitespace-in-python
def replace_mult_spaces(s : str):
    return " ".join(s.split())

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

# convert time to into valid format
# NOTE: this is some kind of magic, but it works
def icream_date_converter(unconv_time):
    conv_time = unconv_time \
                if type(unconv_time) == type(datetime(year=2002,month=7,day=26)) else \
                datetime.combine(unconv_time, time(tzinfo=UTC))
    return conv_time

# format date time into usual formats
def icream_date_formater(date_time : datetime):
    date_format = "%02d. %02m. %Y %02H.%02M"
    return date.strftime(date_time, date_format)

# format duration
# '-> for single day events in: dd. mm. yyyy hh.mm-hh.mm
# '-> for multiday events in: dd. mm. yyyy hh.mm-dd. mm. yyyy hh.mm
# TODO improve for longer events in format similarly to dd. mm. - dd. mm. yyyy
def icream_duration_formater(start_time : datetime, end_time : datetime):    
    
    end_t_fs =  "%02d. %02m. %Y %02H.%02M" \
                if (start_time.day != end_time.day) \
                or (start_time.month != end_time.month) \
                or (start_time.year != end_time.year) else \
                "%02H.%02M" 

    return icream_date_formater(start_time) + "-" + date.strftime(end_time, end_t_fs)

if __name__=="__main__":

    ws = ["[a-borka a borec-c]", " a dafda fda [ s st - - gfa    fda  fda fad    f. ] dafa fda"]

    for w in ws:
        print("{} -> {}".format(w,icream_parse_tags(w)))
