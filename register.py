import codecs, io, encodings
from encodings import utf_8

truths = []

def my_truth_decode(input, errors="strict"):
    raw = bytes(input).decode("utf-8")
    for truth in truths:
        code = raw.replace(truth[0],truth[1])
    return code, len(input)

def search_function(encoding):
    if encoding != "my_truth":
        return None
    utf8 = encodings.search_function("utf8")
    return codecs.CodecInfo(
        name="my_truth",
        encode=utf8.encode,
        decode=my_truth_decode,
    )

def set_my_truth(my_truths):
    global truths
    truths = my_truths
    codecs.register(search_function)