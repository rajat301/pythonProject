import streamlit as st;
import pandas as pd ;

# TEXT INPUT
name= st.text_input('Your name: ')
if name:
    st.write(f'Hello {name}!')

## NUmber Input
x=st.number_input('Enter a number',min_value=1, max_value=99,step=1)
st.write(f'The current number is {x}')

st.divider()

# Button

clicked=st.button('Click me!')
if clicked:
    st.write(':ghost:'*3)

st.divider()


# CHECKBOX

agree= st.checkbox('I agree')
if agree:
    'Great, you agreed!'

st.divider()

df= pd.DataFrame({'Name': ['Raj','Sachin'],
                  'Age':[22,33]})

if st.checkbox('Show data'):
    st.write(df)

st.divider()

#select

cities=['London','Berlin','Paris','Madrid']
city=st.selectbox('Your City',cities,index=1)
st.write(f'You live in {city}')


# SLIDER

x=st.slider('x',value=15,min_value=12,max_value=100,step=4)
st.write(f'x is {x}')

st.divider()

#FILE UPLOADER

uploaded_file= st.file_uploader('Upload a file :', type=['txt','csv','xlsx','.jpeg'])
if uploaded_file:
    st.write(uploaded_file)
    if uploaded_file.type == 'text/plain':
        from io import StringIO
        stringio=StringIO(uploaded_file.getvalue().decode('utf-8'))
        string_data=stringio.read()
        st.write(string_data)
    elif uploaded_file.type == 'text/csv':
        import pandas as pd
        df=pd.read_csv(uploaded_file)
        st.write(df)
    else:
        import pandas as pd
        df=pd.read_excel(uploaded_file)
        st.write(df)


 # Camera Input
camera_photo= st.camera_input('Take a photo')
if camera_photo:
    st.image(camera_photo)
st.image ('https://static.streamlit.io/examples/owl.jpg')



