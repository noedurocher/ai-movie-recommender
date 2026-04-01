from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def build_similarities(movies):
    descriptions = [movie["overview"] for movie in movies]

    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(descriptions)

    similarity = cosine_similarity(tfidf_matrix)
    return similarity

def get_recommendations(user_input, movies):
    similarity = build_similarities(movies)

    titles = [movie["title"] for movie in movies]
    indices = {title:idx for idx, title in enumerate(titles)}

    scores = [0] * len(movies)
    for fav in user_input:
        idx = indices.get(fav)
        if idx is not None:
            scores = [s+sim for s, sim in zip(scores, similarity[idx])]

    ranked = sorted(list(enumerate(scores)), key=lambda x: x[1], reverse=True)

    recommendations=[]
    for i, _ in ranked[:5]:
        recommendations.append(titles[i])
    return recommendations