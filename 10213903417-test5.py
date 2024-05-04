import streamlit as st
from pyproj import Transformer
import math

#设置CGCS2000的编码值、上海2000的原点等参数
cgcs=4490
gsklg=2346
o_x=121.4669
o_y=31.23528
center_x=121.4644
#计算原点的东偏、北偏
st.title('计算上海2000坐标系的东偏与北偏')
if st.button('计算'):
    transformer=Transformer.from_crs(cgcs,gsklg,always_xy=True)  #
    o_x1 = transformer.transform(o_x,0)
    center_x1=transformer.transform(center_x,0)                  #获得纬度都为0时，经度为原点经度和中央经线经度的高斯克吕格投影的坐标
    o_y1 = transformer.transform(0,o_y)
    center_y1=transformer.transform(0,0)
    dis_e = int(math.sqrt((o_x1[0]-center_x1[0])**2 + (o_x1[1]-center_x1[1])**2))  #计算东偏
    dis_n = int(math.sqrt((o_y1[0]-center_y1[0])**2 + (o_y1[1]-center_y1[1])**2))  #计算北偏
    st.markdown(dis_e,dis_n)

#计算坐标转换
with st.form('CGCS2000地理坐标转上海2000投影坐标'):
    st.write('CGCS2000地理坐标转上海2000投影坐标')
    x_0=st.text_input('输入经度120-122','121.456')
    y_0=st.text_input('输入纬度30-32','31.038')
    st.radio('请选择坐标参照系统',['上海2000坐标(WGS84地球椭球体)','上海2000投影坐标(IAU76地球椭球体)'])

    if st.form_submit_button('提交'):
        x=1
