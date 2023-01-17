import streamlit as st

st.write('铝合金门窗')
floors = st.slider('楼层', 0, 10, 1)
zs = 0
for i in range(floors):
    in_text = st.text_area(f'{i+1}楼')
    al_data = in_text.split()
    height = al_data[1::2]
    width = al_data[::2]
    s = 0
    for j in range(len(height)):
        res = eval(height[j]) * eval(width[j])
        res = round(res, 2)
        s += res
        st.write(f'{width[j]} x {height[j]} = {res}')
    s = round(s, 2)
    st.write('计', s)
    zs += s
st.write('总计', zs)


