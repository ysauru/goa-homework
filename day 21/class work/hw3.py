def find_short(s):
    words = s.split()
    shortest_length = len(words[0])
    
    for w in words:
        word_length = len(w)
        if word_length < shortest_length:
            shortest_length = word_length
            
    return shortest_length

