def keyword_score(text_tokens, query_tokens):
    "Calculates ratio between query words and text words."
    if isinstance(text_tokens, list) and len(text_tokens) >= 1 and isinstance(query_tokens, list) and len(query_tokens) >= 1:
        intersection = set(query_tokens).intersection(set(text_tokens))
        return len(intersection) / len(set(query_tokens))
    else:
        raise ValueError("Both text_tokens and query_tokens must be non-empty lists.")


#TEST
text_tokens = ["iran", "oil"]
query_tokens = ["iran", "war"]
score = keyword_score(text_tokens, query_tokens)
print(f"Keyword score: {score}")