# movie_recommender.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 🎬 Movie dataset (Hollywood + Bollywood)
movies = {
    'title': [
        'Inception', 'The Matrix', 'Interstellar', 'Tenet',
        '3 Idiots', 'Taare Zameen Par', 'Dangal', 'PK',
        'Chhichhore', 'Zindagi Na Milegi Dobara', 'Barfi', 'Queen'
    ],
    'description': [
        'A thief steals corporate secrets using dream-sharing technology.',
        'A hacker discovers the truth about his reality.',
        'Explorers travel through a wormhole in space.',
        'Time inversion and secret agents saving the world.',
        'Three friends discover themselves in an engineering college.',
        'A teacher helps a dyslexic child shine through creativity.',
        'A father trains his daughters to become world-class wrestlers.',
        'An alien lands on Earth and questions human beliefs.',
        'A group of friends reunite to recall their college struggles.',
        'Three friends go on a life-changing road trip in Spain.',
        'A mute man with autism falls in love in a heartwarming story.',
        'A woman goes on a solo honeymoon and finds her self-worth.'
    ]
}

# Convert to DataFrame
df = pd.DataFrame(movies)

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['description'])

# Cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Recommend function
def recommend_movie(title):
    if title not in df['title'].values:
        return "❌ Movie not found in database. Please check spelling."

    idx = df[df['title'] == title].index[0]
    similarity_scores = list(enumerate(cosine_sim[idx]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    recommended = []
    for i in similarity_scores[1:4]:  # top 3 excluding input
        recommended.append(df['title'][i[0]])

    return recommended

# Run recommender
print("🎬 Welcome to the Bollywood+Hollywood Movie Recommender!")
print("Available movies:\n" + ", ".join(df['title'].values))
user_input = input("\nEnter a movie name from the list above: ")
print("🔍 Recommended movies:", recommend_movie(user_input))
