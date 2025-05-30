import streamlit as st

st.title("스트림릿에서의 체크 박스 사용 예")

clicked1 = st.button('checkbox 1')
st.write('checkbox 1 Status: ', clicked1)

if clicked1:
    st.write('checkbox 1 was clicked')
else:
    st.write('checkbox 1 was not clicked')

clicked2 = st.checkbox('checkbox 2')
st.write('checkbox 2 status : ', clicked2)

if clicked2:
    st.write('checkbox 2 was clicked')
else:
    st.write('checkbox 2 was not clikced')