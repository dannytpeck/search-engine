from hashtable_get_bucket import hashtable_get_bucket

def hashtable_add(htable, key, value):
    hashtable_get_bucket(htable, key).append([key, value])
    return hashtable
