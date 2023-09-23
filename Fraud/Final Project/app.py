import streamlit as st

# SCSS Styles
scss_styles = """
$total: 200;
$time: 10s;

html, body, .wrap {
  height: 100%;
}

body {
  background: black;
  background-image: radial-gradient(circle at center, white 0%, #222 10%, black 60%);
  overflow: hidden;
}

.wrap {
  transform-style: preserve-3d;
  perspective: 800px;
}

.tri {
  height: 0;
  width: 0;
  position: absolute;
  top: 50%;
  left: 50%;
}

@for $i from 1 through $total {
  $size: random(50) * 1px;
  $rotate: random(360) * 1deg;
  .tri:nth-child(#{$i}){
    border-top: $size solid hsla(random(360), 100%, 50%, 1);
    border-right: $size solid transparent;
    border-left: $size solid transparent;
    margin-left: -$size/2;
    margin-top: -$size/2;
    -webkit-filter: grayscale(1);
    filter: grayscale(1);
    transform: rotate($rotate) translate3d(0,0,-1500px) scale(0);
    animation: anim#{$i} $time infinite linear;
    animation-delay: $i * -($time/$total);
    opacity: 0;
  }
  
  @keyframes anim#{$i}{
    0% {
      opacity: 1;
      transform: rotate($rotate * 1.5) translate3d(random(1000) * 1px, random(1000) * 1px,1000px) scale(1);
    }
  }
}
"""

# HAML
haml_code = """
-max = 200
%div.wrap
  -max.times do
    %div.tri
"""

# Apply SCSS Styles
st.write(f'<style>{scss_styles}</style>', unsafe_allow_html=True)

# Display HAML content
st.write(haml_code, unsafe_allow_html=True)

# The rest of your Streamlit app goes here
# Add your financial dashboard components below this line
st.title("Financial Health Dashboard - Indian Equity Market")