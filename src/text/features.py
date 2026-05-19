def keyword_score(text_tokens, query_tokens):
    "Calculates ratio between query words and text words."
    if isinstance(text_tokens, list) and len(text_tokens) >= 1 and isinstance(query_tokens, list) and len(query_tokens) >= 1:
        intersection = set(query_tokens).intersection(set(text_tokens))
        return len(intersection) / len(set(query_tokens))
    else:
        raise ValueError("Both text_tokens and query_tokens must be non-empty lists.")


def density_score(text_tokens, query_tokens):
    "Calculates keywords concentration in query."
    matching_tokens = 0
    for token in text_tokens:
        if token in query_tokens:
            matching_tokens += 1
    
    density_score = matching_tokens / len(text_tokens)
    return density_score

def relevance_score(text_tokens, query_tokens):
    keyword = keyword_score(text_tokens, query_tokens)
    density = density_score(text_tokens, query_tokens)
    relevance_score = (keyword*0.7 + density*0.3)
    return relevance_score



#TEST
text_tokens = ["iran", "iran", "war", "oil"]
query_tokens = ["iran", "war"]
score = keyword_score(text_tokens, query_tokens)
density = density_score(text_tokens, query_tokens)
relevance = relevance_score(text_tokens, query_tokens)
print(f"Keyword score: {score}")
print(f"Density score: {density}")
print(f"Relevance score: {relevance}")
