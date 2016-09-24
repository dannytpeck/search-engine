def lucky_search(index, ranks, keyword):
    pages = lookup(index, keyword)
    if not pages:
        return None
    best_page = pages[0]
    for page in pages:
        if ranks[page] > ranks[best_page]:
            best_page = page
    return best_page
