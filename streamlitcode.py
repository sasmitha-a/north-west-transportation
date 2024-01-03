import streamlit as st
import numpy as np
import pandas as pd

centered_header_style = """
    <style>
    .centered-header {
        text-align: center;
    }
    </style>
"""
centered_button_style = """
    <style>
    .centered-button {
        font-size: 20px;            
        padding: 10px;      
        border-radius: 5px;
        display: flex;
        justify-content: center;
    }
    </style>
"""
def make_grid(col,row):
    grid = [0]*col
    for i in range(col):
        with st.container():
            grid[i] = st.columns(row,gap="medium")
    return grid



# Render centered header
st.markdown(centered_header_style, unsafe_allow_html=True)
st.markdown('<h1 class="centered-header">NorthWest Corner Rule</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="centered-header">Transportation problem</h3>', unsafe_allow_html=True)


st.markdown("\n\n")

col1, col2= st.columns(2)

# Place content in the first column
with col1:
    demand = st.selectbox('Select no of demands', ['',1,2,3,4,5,6,7,8,9,10],key='demand')

# Place content in the second column
with col2:
    supply = st.selectbox('Select no of supplies', ['',1,2,3,4,5,6,7,8,9,10],key='supply')
  

row = st.selectbox('Select no of rows', [1,2,3,4,5,6,7,8,9,10],key='row')

col = st.selectbox('Select no of columns', [1,2,3,4,5,6,7,8,9,10],key='col')

with col1:
    input1 = st.text_area("Enter demand (one element per line)")

# Convert the input string into a NumPy array
    dema = input1.strip().split("\n")
    demarray = np.array([float(line) for line in dema if line.strip()])
  
with col2:
     array2 = st.text_area("Enter supply (one element per line)")
     sup = array2.strip().split("\n")
     suparray = np.array([float(line) for line in sup if line.strip()])

st.write("Enter the matrix values")
mygrid = make_grid(row,col)

l=[]
l1=[]
for i in range(row):
    for j in range(col):
        a=mygrid[i][j].number_input(":",key=(i*10+j),label_visibility="collapsed",value=0,step=0)
        l.append(a)
    l1.append(l)   
    l=[]

st.markdown(centered_button_style, unsafe_allow_html=True)
st.markdown('<div class="centered-button"><button>Submit</button></div>', unsafe_allow_html=True)

