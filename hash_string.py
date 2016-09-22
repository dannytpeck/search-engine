def hash_string(keyword, buckets):
    out = 0
    for s in keyword:
        out += ord(s)
    return out % buckets
