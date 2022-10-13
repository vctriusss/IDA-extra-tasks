# Task 3. Remove stopwords
def delete_stopwords(text, stop):
    index = text.find(stop)
    indexes = []
    while index != -1:
        indexes.append(index + len(stop) * len(indexes))
        text = text[0: index] + text[index + len(stop):]
        index = text.find(stop, index)
    return text, indexes


assert delete_stopwords('asdf fck asdf', 'fck') == ('asdf  asdf', [5])
assert delete_stopwords('asdf fckfck asdf', 'fck') == ('asdf  asdf', [5, 8])
assert delete_stopwords('fckfckfck', 'fck') == ('', [0, 3, 6])
assert delete_stopwords('asdf sss asdf', 'ss') == ('asdf s asdf', [5])

# Task 4.1 & 4.2. Format string via .format() and without {} and variables
bar = 'foo'
# hack as ord('{')=123, ord('}')=125
bar = (chr(123) + chr(125) + ':' + chr(123) + chr(125)).format(bar, bar)
assert bar == 'foo:foo'
