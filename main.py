import streamlit as st
import pandas as pd
st.title ('Hello Streamlit World! :100:')
st.write('We learn Steamlit !')

# Using Magic commands
# ctr + Shift + F10

'Displaying using magic :smile:'

df= pd.DataFrame({
    'first_column' : [1,2,3,4],
    'second_column': [10,20,35,45]

})
df  # st.write(df)
