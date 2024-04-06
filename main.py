import stqdm
import pickle
import pandas as pd
from PIL import Image
from time import sleep
import streamlit as st
from stqdm import stqdm
from streamlit_option_menu import option_menu


@st.cache_resource
def load_model():
    with open('assets/model.pkl', 'rb') as f:
        return pickle.load(f)


st.set_page_config(page_title="Disaster Management", page_icon="💧", initial_sidebar_state="expanded")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
css_style = {
    "icon": {"color": "white"},
    "nav-link": {"--hover-color": "grey"},
    "nav-link-selected": {"background-color": "#FF4C1B"},
}

# Loading assets
img_banner = Image.open("assets/images/banner.png")
img_banner2 = Image.open("assets/images/banner2.png")
img_iiith = Image.open("assets/images/IIITH_Logo.jpg")


def home_page():
    st.write(f"""# Water Inspection System""", unsafe_allow_html=True)
    st.image(img_banner)

    st.write(f"""<h2>The Problem</h2>   
    <p>Access to clean water is a critical challenge in many parts of the world. Water quality prediction is important for ensuring the availability of safe and clean water for drinking, agriculture, and other purposes. However, traditional methods for water quality prediction are often time-consuming and costly, and they may not provide accurate and timely information. To address this challenge, we have initiated a project to develop an automated water quality prediction system using machine learning.</p> """, unsafe_allow_html=True)

    st.write(f"""<h2>Project goals</h2> <p>In this project, our primary goal is to develop an accurate and efficient machine learning model that can predict water quality based on a range of parameters such as Electrical conductivity of water, Amount of organic carbon in ppm, Amount of Trihalomethanes in μg/L, and turbidity. The model will be trained on a large dataset of historical water quality data and will be designed to provide predictions for water quality..</p> """, unsafe_allow_html=True)


# def about_page():
#     st.write("""<h1>Project background</h1>""", unsafe_allow_html=True)
#     st.image(img_banner2)
#     st.write("""
#         <p>Rwanda is a landlocked country located in East Africa, 
#         with a population of approximately 13 million people. Despite efforts to improve access to clean water, 
#         access remains a critical challenge, particularly in rural areas. According to UNICEF, only 47% of the population 
#         has access to basic water services, and only 32% have access to safely managed drinking water services. One of 
#         the challenges in ensuring access to clean water is predicting and monitoring water quality. Traditional water 
#         quality prediction and monitoring methods are often time-consuming, costly, and may not provide timely and 
#         accurate information. This can lead to delays in identifying and addressing water quality issues, putting public 
#         health and agricultural productivity at risk. <br> <br> Machine learning has the potential to revolutionize water 
#         quality prediction and monitoring by providing a faster, more accurate, and cost-effective method for predicting 
#         water quality. By analyzing large datasets of water quality parameters, machine learning models can identify 
#         patterns and relationships between different parameters, enabling accurate predictions of water quality.</p><br>
#     """, unsafe_allow_html=True)


def model_section():
    st.write("""<h1>Predict Water Quality</h1>
    <p>Enter these values of the parameters to know if the water quality is suitable to drink or not.</p><hr>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, gap="large")
    with col1:
        Do = st.number_input(label="Dissolved Oxygen (mg/l)", min_value=0.0, max_value=1000.0, step=2.0, format="%f",
                             key="test_slider0")
        pH = st.number_input(label="pH", min_value=0.0, max_value=14.0, step=1.0, format="%f", key="test_slider1")
        
    with col2:
        Conductivity = st.number_input(label="Conductivity (μS/cm)", min_value=0.0, max_value=5000.0, step=2.0,
                                       format="%f", key="test_slider2")
        Bod = st.number_input(label="Biochemical Oxygen Demand (mg/l)", min_value=0.0, max_value=1000.0, step=2.0,
                              format="%f", key="test_slider3")
        st.write("<br>", unsafe_allow_html=True)
        predict_button = st.button('  Predict Water Quality  ')

    with col3:
        Na = st.number_input(label="Nitrate_N_Nitrite_N (mg/l)", min_value=0.0, max_value=1000.0, step=2.0, format="%f",
                             key="test_slider4")
        Fc = st.number_input(label="Fecal Coliform (MPN/100ml)", min_value=0.0, max_value=100000.0, step=2.0,
                             format="%f", key="test_slider5")
        
    dataframe = pd.DataFrame({'Dissolved_Oxygen': [Do], 'pH': [pH], 'Conductivity': [Conductivity], 'BOD': [Bod], 'Nitrate': [Na], 'Fecal_Coliform': [Fc], 'Potability': [0.0]})

    dataframe['npH']=dataframe.pH.apply(lambda x: (0 if (8>=x>=6.5)  
                                 else(40 if  (8.5>=x>=8) or (6.5>=x>=6) 
                                      else(60 if (9>=x>=8.5) or (6>=x>=5.5) 
                                          else(80 if (9.5>=x>=9) or (5.5>=x>=5)
                                              else 100)))))
    
    dataframe['ndo']=dataframe.Dissolved_Oxygen.apply(lambda x:(0 if (x>=7)  
                                 else(40 if  (7>=x>=5.5) 
                                      else(60 if (5.5>=x>=4)
                                          else(80 if (4>=x>=2) 
                                              else 100)))))
    
    dataframe['nco']=dataframe.Fecal_Coliform.apply(lambda x:(0 if (x<=10)  
                                 else(40 if  (10<=x<=100) 
                                      else(60 if (100<=x<=1000)
                                          else(80 if (1000<=x<=10000) 
                                              else 100)))))
    
    dataframe['nbdo']=dataframe.BOD.apply(lambda x:(0 if (x<=3)  
                                 else(40 if  (3<x<=6) 
                                      else(60 if (6<x<=15)
                                          else(80 if (15<x<=25) 
                                              else 100)))))
    
    dataframe['nec']=dataframe.Conductivity.apply(lambda x:(0 if (x<=500)  
                                 else(40 if  (500<x<=1000) 
                                      else(60 if (1000<x<=1500)
                                          else(80 if (1500<x<=2000) 
                                              else 100)))))
    
    dataframe['nna']=dataframe.Nitrate.apply(lambda x:(0 if (x<=10)  
                                 else(40 if  (10<x<=20) 
                                      else(60 if (20<x<=50)
                                          else(80 if (50<x<=100) 
                                              else 100)))))
    
    dataframe['wph']=dataframe.npH * 0.165
    dataframe['wdo']=dataframe.ndo * 0.281
    dataframe['wbdo']=dataframe.nbdo * 0.234
    dataframe['wec']=dataframe.nec* 0.009
    dataframe['wna']=dataframe.nna * 0.028
    dataframe['wco']=dataframe.nco * 0.281
    dataframe['wqi']=dataframe.wph+dataframe.wdo+dataframe.wbdo+dataframe.wec+dataframe.wna+dataframe.wco

    dataframe['quality']=dataframe.wqi.apply(lambda x:('Excellent' if (25>=x>=0)  
                                 else('Good' if  (50>=x>=26) 
                                      else('Poor' if (75>=x>=51)
                                          else('Very Poor' if (100>=x>=76) 
                                              else 'Unsuitable')))))

    if predict_button:
        model = load_model()
        # result = model.predict(dataframe)
        for _ in stqdm(range(50)):
            sleep(0.015)
        
        if dataframe['quality'].values[0] == 'Excellent':
            st.success(f"Water Quality Index: {dataframe['wqi'].values[0]}")
            st.success(f"The Water Quality is {dataframe['quality'].values[0]}")
        elif dataframe['quality'].values[0] == 'Good':
            st.success(f"Water Quality Index: {dataframe['wqi'].values[0]}")
            st.success(f"The Water Quality is {dataframe['quality'].values[0]}")
        elif dataframe['quality'].values[0] == 'Poor':
            st.warning(f"Water Quality Index: {dataframe['wqi'].values[0]}")
            st.warning(f"The Water Quality is {dataframe['quality'].values[0]}")
        elif dataframe['quality'].values[0] == 'Very Poor':
            st.error(f"Water Quality Index: {dataframe['wqi'].values[0]}")
            st.error(f"The Water Quality is {dataframe['quality'].values[0]}")
        else:
            st.error(f"Water Quality Index: {dataframe['wqi'].values[0]}")
            st.error(f"The Water Quality is {dataframe['quality'].values[0]}")
        # if result[0] == 1.0:
        #     st.error("This Water Quality is Non-Potable")
        # else:
        #     st.success('This Water Quality is Potable')

    st.write("""<h2>Dissolved Oxygen: </h2>
             <p>Dissolved Oxygen (DO) refers to the amount of oxygen gas (O2) dissolved in water. For most freshwater ecosystems, dissolved oxygen levels above 5 mg/L are considered acceptable for supporting aquatic life.</p>""", unsafe_allow_html=True)
    st.write("""<h2>pH: </h2>
                <p>pH is a measure of how acidic or basic a solution is. The pH scale ranges from 0 to 14, with 7 being neutral. pH values below 7 indicate acidity, while values above 7 indicate alkalinity. Most aquatic organisms prefer a pH range of 6.5 to 8.5.</p>""", unsafe_allow_html=True)
    st.write("""<h2>Conductivity: </h2>
                <p>Conductivity is a measure of the ability of water to conduct an electrical current. It is influenced by the presence of dissolved ions in the water, such as salts and minerals. High conductivity levels can indicate pollution or the presence of contaminants in the water. In freshwater ecosystems, electrical conductivity values typically range from 50 to 1500 microsiemens per centimeter (μS/cm) or 0.05 to 1.5 millisiemens per centimeter (mS/cm).</p>""", unsafe_allow_html=True)
    st.write("""<h2>Biochemical Oxygen Demand: </h2>
                <p>Biochemical Oxygen Demand (BOD) is a measure of the amount of dissolved oxygen required by bacteria to break down organic matter in water. High BOD levels can indicate pollution or the presence of organic contaminants in the water. In freshwater ecosystems, BOD values typically range from less than 2 milligrams per liter (mg/L) to 8 mg/L or higher.</p>""", unsafe_allow_html=True)
    st.write("""<h2>Nitrate and Nitrite: </h2>
                <p>Nitrate and nitrite are forms of nitrogen that can be found in water. High levels of nitrate and nitrite can indicate pollution from agricultural runoff, sewage, or industrial discharges. Nitrate levels above 10 mg/L can pose health risks, particularly for infants and pregnant.</p>""", unsafe_allow_html=True)
    st.write("""<h2>Fecal Coliform: </h2>
                <p>Fecal coliform bacteria are a type of bacteria found in the intestines of warm-blooded animals. High levels of fecal coliform bacteria in water can indicate contamination with human or animal waste. Fecal coliform bacteria can cause waterborne illnesses and pose a health risk to humans. In many jurisdictions, the acceptable level of fecal coliform bacteria for recreational waters, such as swimming areas and beaches, is typically less than 200 colony-forming units (CFU) per 100 milliliters (mL) of water, based on single-sample measurements.</p>""", unsafe_allow_html=True)


def contributors_page():
    st.write("""
                <h1 style="text-align: center; color:#FFF6F4;">Contributors</h1><hr>
                <div style="text-align:center;">
                <table>
                    <tbody>
                        <tr>
                            <th width="20%" style="font-size: 140%;" colspan="2">Contributors</th>
                        </tr>
                        <tr>
                            <th width="20%">Name</th>
                            <th width="20%">Roll.No.</th>
                        <tr>
                            <td width="20%"> Akhil Gupta</td>
                            <td width="20%"> 2021101012</td>
                        </tr>
                        <tr>
                            <td>Ishan Kavathekar</td>
                            <td>2022121003</td>
                        </tr>
                        <tr>
                            <td>Kunal Bhosikar</td>
                            <td>2022121005</td>
                        </tr>
                        <tr>
                            <td>Rayaan Khan</td>
                            <td>2021101120</td>
                        </tr>
                        <tr>
                            <td>Utsav Shekhar</td>
                            <td>2021114006</td>
                        <tr>
                    </tbody>
                </table>
                </div>
                <hr>
            """, unsafe_allow_html=True)


with st.sidebar:
    st.image(img_iiith)
    selected = option_menu(
        menu_title=None,
        options=["Home", "Check Water Quality", "Contributors"],
        icons=["house", "droplet", "info-circle", "people"],
        styles=css_style
    )

if selected == "Home":
    home_page()

elif selected == "Check Water Quality":
    model_section()

# elif selected == "About":
#     about_page()

elif selected == "Contributors":
    contributors_page()

