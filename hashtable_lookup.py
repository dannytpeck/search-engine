from hashtable_get_bucket import hashtable_get_bucket

def hashtable_lookup(htable,key):
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:
        if entry[0] == key:
            return entry[1]
    return None
