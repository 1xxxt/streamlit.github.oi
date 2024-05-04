import streamlit as st
from pyproj import Transformer
import math

#设置CGCS2000的编码值、上海2000的原点、中央经线等参数
cgcs=4490
o_x=121.4669
o_y=31.23528
center_x=121.4644
sh2000 = "+proj=tmerc + lon_0=" + str(center_x)                      #创建sh2000坐标系的编码
#计算原点的东偏、北偏
st.title('计算上海2000坐标系的东偏与北偏')
if st.button('计算'):
    transformer=Transformer.from_crs(cgcs,sh2000,always_xy=True)     #从cgcs2000转到sh2000坐标系
    dis_e,dis_n = transformer.transform(o_x,o_y)                     #计算东、北偏
    st.markdown(dis_e,dis_n)
    dis_e=round(-dis_e,2)
    dis_n=round(-dis_n,2)

#计算坐标转换
with st.form('CGCS2000地理坐标转上海2000投影坐标'):
    st.write('CGCS2000地理坐标转上海2000投影坐标')
    x_0=st.text_input('输入经度120-122','121.456')                                                            #创建输入经纬度的文本框
    y_0=st.text_input('输入纬度30-32','31.038')
    x_0=int(x_0)
    y_0=int(y_0)
    select_datum=st.radio('请选择坐标参照系统',['上海2000坐标(WGS84地球椭球体)','上海2000投影坐标(IAU76地球椭球体)'])   #创建单选框

    if st.form_submit_button('提交'):
        sh2000_proj = '+proj=tmerc +lon_0='+str(center_x)+' +x_0='+str(dis_e)+' +y_0='+str(dis_n)            #编写上海2000坐标系的详细编码
        if select_datum='上海2000坐标(WGS84地球椭球体)':                                                      #选择不同的椭球体就为编码添加不同的信息
            ellps=' +ellps=WGS84'
        else:
            ellps=' +ellps=IAU76'
        sh2000_proj=sh2000_proj+ellps
        transformer=Transformer.from_crs(cgcs,sh2000_proj,always_xy=True)                                    #转换cgcs2000下的坐标到上海2000
        poi_x,poi_y=transformer.transform(x_0,y_0)
        st.markdown(poi_x,poi_y)
