def generate_swaston(s):
    if len(s) < 2:
        return s
    l_spaced_word = " ".join(s)
    r_spaced_word = " ".join(s)[::-1]
    l_word = s[::-1]
    r_word = s
    center = "{0}{1}\n".format(l_spaced_word, r_spaced_word[1:])
    tab_pre = " " * (len(r_spaced_word) - 2)
    tab_post = tab_pre + " "
    upper, lower = [], []
    size = len(l_word)
    for c in range(size - 1):
        if c == 0:
            upper.append("{0}{1}{2}\n".format(l_word[c], tab_pre, l_spaced_word))
        else:
            upper.append("{0}{1}{2}{3}\n".format(l_word[c], tab_pre, r_word[c], tab_post))

    for c in range(1, size):
        if c == size - 1:
            lower.append("{0}{1}{2}\n".format(r_spaced_word, tab_pre, r_word[c]))
        else:
            lower.append("{0}{1}{2}{3}\n".format(tab_post, l_word[c], tab_pre, r_word[c]))

    return "{0}{1}{2}".format("".join(upper), center, "".join(lower))