from app.utils.levenshtein import levenshtein

def score(word: str, candidate: str) -> float:
    dist = levenshtein(word, candidate)

    # base score (lower is better)
    score = dist

    # 1. length penalty (small difference preferred)
    score += abs(len(word) - len(candidate)) * 0.2

    # 2. prefix bonus (VERY important for Amharic)
    prefix_len = 0
    for a, b in zip(word, candidate):
        if a == b:
            prefix_len += 1
        else:
            break

    score -= prefix_len * 0.3

    return score