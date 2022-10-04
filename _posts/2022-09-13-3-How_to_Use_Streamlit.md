---
layout: post
title:  "How to Create a Simple Data Science App with Streamlit"
date:   2022-09-22
author: "Luke McDowell"
description: Why Snowflake's High-Profile Acquisition Might be the Perfect Place to Deploy your Project.
image: /assets/images/Streamlit.jgg
---

## How to Create a Simple Data Science App with Streamlit

![image:](/assets/images/streamlit_logo.png)

You’ve just created a stunning data science model. You’re proud of your work, but lobbing over the .py file just doesn’t seem like a worthy way of sharing it. If only there was a quick-to-learn web app that would do justice to your marvelous project... 



## Why Streamlit?
Streamlit is an open-source Python library compatible with major Python libraries like Matplotlib, Plotly, Pandas, numpy, scikit-learn, etc. While Streamlit may not be the most widely used web app framework, it is definitely one of the easiest and quickest to learn. Snowflake seems to have seen some potential in it too, as the cloud company [recently acquired Streamlit for $800m](https://techcrunch.com/2022/03/02/snowflake-acquires-streamlit-for-800m-to-help-customers-build-data-based-apps/).If beautiful, easy-to-build and quick-to-deploy apps still aren't enough to entice you, Streamlit is also FREE to use.



## Installing Streamlit:


Opening your terminal of choice and entering a simple 'pip install' should do the trick, though a more detailed installation guide can be found [on Streamlit's web page](https://docs.streamlit.io/library/get-started/installation#install-streamlit-on-windows)
  
![image:](/assets/images/Palindrome Result.png) 
```
pip install streamlit
```

  
  
## Using Streamlit


While Streamlit is most powerful when deployed as an online app hosted in a repository like github, for the purpose of this tutorial, lets create a simple a app that runs locally and determines whether an entered word is a palindrome or not.  We'll start by importing the streamlit library, configuring our app, then integrating our function with Streamlit's framework.




### Configure your app

To start, we'll import the library:
```
import streamlit as st  
```


Streamlit has a respectable array of options when it comes to styling and configuring your app. In this case, we'll create a title for our app, then set it to a wide layout with the side bar expanded using the following syntax: 
```
st.set_page_config(
    page_title="Sample Streamlit App",
    layout="wide",
    initial_sidebar_state="expanded",
)
```


### Integrate 

Now let's add our palindrome function before the main streamlit function for initialization purposes. We'll then add a basic text input function with the main function to pass a word into our palindrome function:


![image:](/assets/images/Palindrome Result.png)


Here is our .py code in full:
```
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Sample Streamlit App",
    layout="wide",
    initial_sidebar_state="expanded",
)

def palindrome(word):
    word = word.replace(" ","")
    x = 0
    result = "Is Not Palindrome"
    if len(word)%2 != 0:
        result = "Is Palindrome"
        while x != (len(word)-1-x):
            if word[x] != word[(len(word)-1-x)]:
                result = "Is not palindrome"
                break
            x += 1          
    return(result)

image = 'https://media.istockphoto.com/photos/beautiful-sunrise-over-the-sea-picture-id610041376?k=20&m=610041376&s=612x612&w=0&h=JoEPWYoq1-FN5ANIQHNNdI2XrRDYnPCUWuLOHMrgLnE='

def main():
    st.title('The Palindrome Test')
    st.image(image,caption = 'Where will you find YOUR next palindrome?')
    print(palindrome('Hi there'))
    text_input = st.text_input(
        "Welcome to the Palindrome Test",
        placeholder='Enter word here',
    )

    if text_input:
        st.metric(label="Result of Palindrome Test: ", value=palindrome(text_input))   
    
if __name__ == "__main__":
    main()
```    

