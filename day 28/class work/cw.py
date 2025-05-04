#


def cap_me(arr):
    capitalized_list = []

    for word in arr:
        capitalized_list.append(word.capitalize())
    return capitalized_list

#


def word_search(query, seq):
    lower_query = query.lower()
    matched_words = []
    for word in seq:
        lower_word = word.lower()
        if lower_query in lower_word:
            matched_words.append(word)
    
    if not matched_words:
        return ["None"]
    else:
        return matched_words

#
def duplicate_count(text):
    count = 0
    checked = []
    words = text.lower()
    
    for i in words:
        if i in checked:
            continue
        seen = 0
        for c in words:
            if c == i:
                seen += 1
        if seen > 1:
            count += 1
        checked.append(i)
    return count

#
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


#


def to_camel_case(text):
    text = text.replace('-', ' ').replace('_', ' ')
    words = text.split()
    if not words:
        return ''
    
    result = words[0]
    for word in words[1:]:
        if word:
            result += word[0].upper() + word[1:].lower()
    
    return result

