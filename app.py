import pickle
import numpy as np
import streamlit as st

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

# Custom CSS for full-screen gradient background and carousel styling
st.markdown("""
    <style>
        body {
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #800000, #f5f5dc); /* Maroon to Beige */
            color: #fff;
            font-family: 'Arial', sans-serif;
        }
        .main-header {
            background: linear-gradient(135deg, #800000, #f5f5dc);
            color: #fff;
            text-align: center;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        .stSelectbox {
            background-color: #fff;
            color: #333;
            border-radius: 5px;
            padding: 5px;
        }
        .carousel-container {
            text-align: center;
        }
        .carousel {
            margin: 10px auto;
            width: 90%;
            max-width: 800px;
            background-color: #fff;
            border: 2px solid #800000;
            border-radius: 8px;
            padding: 15px;
            color: #333;
            font-size: 16px;
        }
        .carousel h4 {
            color: #800000;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Header with gradient background
st.markdown("<div class='main-header'><h1>BrizBain</h1></div>", unsafe_allow_html=True)

# Skill List
movies_list = [
    'AI/ML', 'Remote Sensing', 'IoT', 'Embedded Systems', 'Data Analysis',
    'Data Science', 'Environmental Science', 'Blockchain', 'Security',
    'Medical Imaging', 'Robotics', 'Game Development', '3D Modeling', 'nan'
]

# Layout with 3 columns
col1, col2, col3 = st.columns(3)

with col1:
    selected1 = st.selectbox("Skill 1", movies_list, key="selectbox1")

with col2:
    selected2 = st.selectbox("Skill 2", movies_list, key="selectbox2")

with col3:
    selected3 = st.selectbox("Skill 3", movies_list, key="selectbox3")

input_array = [selected1, selected2, selected3]

# Vectorization function
def vectorize(front_array):
    categories = [
        'AI/ML', 'Remote Sensing', 'IoT', 'Embedded Systems', 'Data Analysis',
        'Data Science', 'Environmental Science', 'Blockchain', 'Security',
        'Medical Imaging', 'Robotics', 'Game Development', '3D Modeling', 'nan'
    ]
    init_vector = [0] * len(categories)

    for element in front_array:
        if element in categories:
            index = categories.index(element)
            init_vector[index] = 1

    return init_vector[0:13]

# Load Model
model_input = vectorize(input_array)
model_path = 'knn_model2.pkl'

with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Predictions
predictions = model.predict(model_input)

# Display Predictions in a Carousel Style
def display_carousel(prediction_text, carousel_id):
    st.markdown(f"""
        <div class="carousel-container">
            <div id="{carousel_id}" class="carousel">
                <h4>Suggested Skill:</h4>
                <p>{prediction_text}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Display up to 4 predictions
for i, pred in enumerate(predictions[:4]):
    display_carousel(pred, f"carousel{i+1}")
