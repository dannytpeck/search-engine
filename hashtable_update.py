from hashtable_get_bucket import hashtable_get_bucket

def hashtable_update(htable, key, value):
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:
        if entry[0] == key:
            entry[1] = value
            return htable
    bucket.append([key, value])
    return htable
