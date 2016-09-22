def hashtable_get_bucket(htable, key):
    return htable[hash_string(key, len(htable))]
