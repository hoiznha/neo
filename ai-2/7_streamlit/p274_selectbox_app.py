import streamlit as st

st.title("스트림릿에서 셀렉트 박스 사용 예")

selectbox1_options = ['하이든','베토벤','모차르트','쇼팽']
your_option1 = st.selectbox('좋아하는 음악가는?', selectbox1_options)
st.write('**선택한 답변** : ',your_option1)

selectbox2_options = ['피카소','뭉크','보티챌리','렘브란트']
your_option2 = st.selectbox(' 좋아하는 화가는?', selectbox2_options)
st.write('**선택한 답변** :', your_option2)