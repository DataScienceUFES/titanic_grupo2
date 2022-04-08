import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.header("Titanic Analysis")
st.subheader("Visualization")

def main():
    df = pd.read_csv("train.csv")

    st.write("Dataframe head:", df.head())

    # survived and sex plot
    st.write("Plotting Sex vs Survived")
    fig = plt.figure(figsize=(12,8))

    sns.barplot(df['Sex'], df['Survived'])
    plt.title("Sex vs Suvived")

    st.pyplot(fig)

main()