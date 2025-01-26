import pickle
import os
import streamlit as st
import requests
import numpy as np

import sys

class KNN:
    
    def __init__(self):
        self.distance = None
        self.vector_pata_hai = None
        self.vector_ke_result = None
        self.hamara_vector = None

    def fit(self, x_train, y_train):
        # Store training vectors and corresponding results
        self.vector_pata_hai = np.array(x_train)
        self.vector_ke_result = np.array(y_train)  # Corrected to match the shape of x_train

    def predict(self, test):
        # Convert the test vector to a numpy array
        self.hamara_vector = np.array(test)

        # Calculate the difference vectors
        distance_vector = self.vector_pata_hai - self.hamara_vector

        # Calculate squared distances manually
        distance = np.sum(distance_vector**2, axis=1)

        # Compute Euclidean distances
        self.distance = np.sqrt(distance)

        # Find the minimum distance value
        minimum = self.distance.min()

        # Collect results corresponding to the minimum distance
        output = []
        for index, dist in enumerate(self.distance):
            if dist == minimum:
                output.append(self.vector_ke_result[index])  # Index correctly

        return np.array(output)  # Convert output list to numpy array


#st.header("BrizBain")
st.markdown(
    """
    <h2 style="text-align: center;">BrizBain</h2>
    """,
    unsafe_allow_html=True
)
movies_list = ['AI/ML', 'Remote Sensing', 'IoT', 'Embedded Systems', 'Data Analysis', 'Data Science',
                  'Environmental Science', 'Blockchain', 'Security', 'Medical Imaging', 'Robotics', 'Game Development',
                  '3D Modeling', 'nan']


col1, col2, col3 = st.columns(3)

# Add select boxes to the columns with the same options
with col1:
    selected1 = st.selectbox("Select the skill", movies_list, key="selectbox1")

with col2:
    selected2 = st.selectbox("Select the skill", movies_list, key="selectbox2")

with col3:
    selected3 = st.selectbox("Select the skill", movies_list, key="selectbox3")

input_array=[selected1,selected2,selected3]

#vectorizing the input 
def vectorize(front_array):
    categories = ['AI/ML', 'Remote Sensing', 'IoT', 'Embedded Systems', 'Data Analysis', 'Data Science',
                  'Environmental Science', 'Blockchain', 'Security', 'Medical Imaging', 'Robotics', 'Game Development',
                  '3D Modeling', 'nan']
    init_vector = [0] * len(categories)

    for element in front_array:
        if element in categories:
            index = categories.index(element)
            init_vector[index] = 1

    return init_vector[0:13]

#loading the model
model_input=vectorize(input_array)
model_path='knn_model2.pkl'

with open(model_path,'rb') as file:
    model=pickle.load(file)

predictions=model.predict(model_input)

def single_text_box_carousel(text, carousel_id):
    st.markdown(
        f"""
        <div id="{carousel_id}" class="carousel slide" data-ride="carousel" style="width: 50%; margin: 10px 0;">
          <div class="carousel-inner">
            <div class="carousel-item active">
              <div class="d-block text-left" style="height:150px; padding:15px; font-size:16px; background-color:#f7f7f7; border:1px solid #ddd; border-radius:5px;">
                {text}
              </div>
            </div>
          </div>
          <a class="carousel-control-prev" href="#{carousel_id}" role="button" data-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
          </a>
          <a class="carousel-control-next" href="#{carousel_id}" role="button" data-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
          </a>
        </div>
        <style>
          .carousel-item {{
              text-align: left;
          }}
        </style>
        """, unsafe_allow_html=True
    )

# Text for each carousel
text1 = predictions[0]
text2 = predictions[0]
text3 = predictions[0]
text4 = predictions[0]

# Display 4 Carousels
st.write("Carousel 1:")
single_text_box_carousel(text1, "carousel1")

st.write("Carousel 2:")
single_text_box_carousel(text2, "carousel2")

st.write("Carousel 3:")
single_text_box_carousel(text3, "carousel3")

st.write("Carousel 4:")
single_text_box_carousel(text4, "carousel4")

# Add Bootstrap dependencies
st.markdown("""
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
""", unsafe_allow_html=True)






