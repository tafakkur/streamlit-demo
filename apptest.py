import pandas as pd
import streamlit as st
import numpy as np
# import seaborn as sns


st.title('Streamlit App Trial')
st.write('This is a trial dashboard')

# you will need to run the command - streamlit run apptest.py - from the commandline to see the output

dt = pd.read_csv('testdata.csv')  # enter full path of the file
df = pd.DataFrame(dt.iloc[:, 1:], index=None)

s1 = df.head()
st.write('Sample:\n')
st.write(s1)

# s2 = df.describe()
# st.write('Summary:')

st.write('Summary:')
st.write('Average Marks = ', round(df['Marks'].mean()))
st.write('Highest Marks = ', round(df['Marks'].max()))
st.write('Lowest Marks = ', round(df['Marks'].min()))

st.write('Overall Top Scorer:')
st.write(df[df.Total == df.Total.max()][['Name', 'Total']])

# Filter 1
cat_fil = st.selectbox("Select Category:", pd.unique(df['Category']))
df = df[df.Category == cat_fil]

# kpis
kpi1, kpi2 = st.columns(2)
kpi1.metric(
    label='Average Category Marks',
    value=round(df['Marks'].mean())
)

kpi2.metric(
    label='Highest Category Marks',
    value=round(df['Total'].max()),
)

st.write('Top Scorer:')
st.write(df[df.Total == df.Total.max()]['Name'])
