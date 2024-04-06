import streamlit as st
import pandas as pd
import pickle
import requests 





API_KEY = 'bf4df5a429e3df768869f5831a9caf6e'
url = "https://api.themoviedb.org/3/movie/{}"
poster_url = "https://image.tmdb.org/t/p/w500"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiZjRkZjVhNDI5ZTNkZjc2ODg2OWY1ODMxYTljYWY2ZSIsInN1YiI6IjY0YWQ4NDFhYjY4NmI5MDEyZjg4YTc1NCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.oUN965X5ntJBNaAxcQqsXhl-m79T-79pSiZJlLx9_WQ"
}


def getPoster(movie_id):
    res =  requests.get(url.format(movie_id), headers=headers).json()
    poster = poster_url + res['poster_path']
    return poster

def recommend(movie):
    if movie not in movies_df['title'].values:
        print("movie not found")
        return
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    movie_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key= lambda x: x[1])[1:6]
    result = []
    movie_poster = []
    for i in movie_list:
        result.append(movies_df.iloc[i[0]].title)
        movie_poster.append(getPoster(movies_df.iloc[i[0]].movie_id))
    return result, movie_poster




movies_df = pickle.load(open('index_df', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_titles = movies_df['title'].values

st.title("Movie Recommender")


option = st.selectbox(
    'Which Movie You Like The Most?',
   movie_titles)



if st.button('Recommend'):
    movie_title,movie_poster = recommend(option)
    st.header("Recommended Movies")
    col1, col2 , col3 ,col4 ,col5 = st.columns(5, gap="medium")
    with col1:
        st.text(movie_title[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_title[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_title[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_title[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_title[4])
        st.image(movie_poster[4])
