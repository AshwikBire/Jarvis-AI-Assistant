from duckduckgo_search import DDGS

def search_duckduckgo(query):
    with DDGS() as ddgs:
        return list(ddgs.text(query, max_results=5))