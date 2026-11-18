import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(
    page_title="Netflix Data Analysis",
    page_icon="🎬",
    layout="wide"
)

# Title
st.title("🎬 Netflix Movies & TV Shows Analysis")
st.subheader("Exploratory Data Analysis (EDA)")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("netflix_data.csv")
    return df

df = load_data()

# Display dataset
st.write("### Dataset Overview")
st.write("Total Records:", len(df))
st.dataframe(df.head())

# Dataset information
st.write("### Dataset Information")
st.write("Number of Rows:", df.shape[0])
st.write("Number of Columns:", df.shape[1])

# Movies and TV Shows
st.write("### Movies vs TV Shows")

type_counts = df["type"].value_counts()

fig, ax = plt.subplots()
type_counts.plot(kind="bar", ax=ax)
ax.set_xlabel("Type")
ax.set_ylabel("Count")
ax.set_title("Movies vs TV Shows")

st.pyplot(fig)

# Ratings distribution
st.write("### Ratings Distribution")

if "rating" in df.columns:
    fig, ax = plt.subplots()
    df["rating"].value_counts().plot(kind="bar", ax=ax)
    ax.set_xlabel("Rating")
    ax.set_ylabel("Count")
    ax.set_title("Netflix Content Ratings")
    st.pyplot(fig)

# Release year analysis
st.write("### Release Year Analysis")

if "release_year" in df.columns:
    fig, ax = plt.subplots()
    sns.histplot(df["release_year"].dropna(), bins=30, ax=ax)
    ax.set_xlabel("Release Year")
    ax.set_ylabel("Count")
    st.pyplot(fig)

# Search filter
st.write("### Search Netflix Titles")

search = st.text_input("Enter movie or TV show name")

if search:
    filtered_df = df[df["title"].str.contains(search, case=False, na=False)]
    st.dataframe(filtered_df)
else:
    st.dataframe(df)

st.success("Netflix Data Analysis Dashboard")