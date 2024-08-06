import streamlit as st
import pandas as pd 


st.header('Welcome !!')


df = pd.read_excel('BME_401_CT_ Marksheet.xlsx')

# Text input field
student_id = pd.to_numeric(st.text_input("Enter Student ID:"), errors='coerce')


button_clicked = st.button('Submit')


if button_clicked:
    if student_id in df['Student ID'].values:
        # Find the Total Marks for the given Student ID
        total_marks = df.loc[df['Student ID'] == student_id, 'Total Marks'].values[0]
        if total_marks >= 12:
            with st.expander("Result", expanded=True):
             st.write(f'Total Marks: {total_marks} (passed)')
        else:
           with st.expander("Result", expanded=True):
             st.write(f'Total Marks: {total_marks} (failed)')
    else: 
        st.write('Wrong Student ID')

else: 
   pass
    
        

