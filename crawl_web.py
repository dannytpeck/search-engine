from get_page import get_page
from add_page_to_index import add_page_to_index
from union import union
from get_all_links import get_all_links

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = {}
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index

if __name__ == "__main__":
    print crawl_web("https://www.udacity.com/cs101x/index.html")
