import streamlit as st

# Title
st.title("Four Carousels with Smaller Left-Aligned Text Boxes")

# Function to create a single carousel with one text box
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
text1 = "This is the text for Carousel 1."
text2 = "This is the text for Carousel 2."
text3 = "This is the text for Carousel 3."
text4 = "This is the text for Carousel 4."

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
text2 = predictions[1]
text3 = predictions[2]
text4 = predictions[3]

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






