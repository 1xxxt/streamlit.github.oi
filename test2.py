import streamlit as st
import pandas as pd
pmdata=pd.read_csv('D:/geo/3/软件工程和GIS开发/3/实习2/csj_pm25.csv')
st.title('长三角PM2.5监测数据')
with st.expander('显示原始数据'):
    st.dataframe(pmdata)
with st.form('基于属性表达式查询记录'):
    st.write('基于属性表达式查询记录')
    mon=st.selectbox('请选择月份',pmdata.columns[4:])
    rel=st.selectbox('请选择关系',['>','<'])
    num=st.text_input('输入一个值','0')
    if st.form_submit_button('提交'):
        fig=float(num)
        if rel == '>':
            outputdf=pmdata[pmdata[mon]>fig]
        elif rel=='<':
            outputdf=pmdata[pmdata[mon]<fig]
        st.write('共有'+str(len(outputdf))+'条数据')
        st.dataframe(outputdf)
