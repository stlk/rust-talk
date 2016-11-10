import ctypes

library_name = "libfastblank/target/release/libfastblank.dylib"
stringtools = ctypes.CDLL(library_name)

text_spaces = """
                                                                                                                               x
Hi, thank you for your talk proposal. We've received a lot of high quality talks and we had very hard time to pick the best one.
"""

text = """
Hi, thank you for your talk proposal. We've received a lot of high quality talks and we had very hard time to pick the best one.
"""

def py_isspace(text):
    text.isspace()

def fast_blank(text):
    stringtools.fast_blank(text)

if __name__ == '__main__':
    import timeit
    print("text")
    print("py_isspace")
    print(timeit.timeit("py_isspace(text)", setup="from __main__ import py_isspace, text"))
    print("fast_blank")
    print(timeit.timeit("fast_blank(text)", setup="from __main__ import fast_blank, text"))

    print("spaces")

    print("py_isspace")
    print(timeit.timeit("py_isspace(text_spaces)", setup="from __main__ import py_isspace, text_spaces"))
    print("fast_blank")
    print(timeit.timeit("fast_blank(text_spaces)", setup="from __main__ import fast_blank, text_spaces"))
