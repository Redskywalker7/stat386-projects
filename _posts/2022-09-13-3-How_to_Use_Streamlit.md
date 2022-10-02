---
layout: post
title:  "How to Create a Simple Data Science App with Streamlit"
date:   2022-09-22
author: "Luke McDowell"
description: Why Snowflake's High-Profile Acquisition Might be the Perfect Place to Deploy your Project.
image: /assets/images/streamlit_logo.png
---

## How to Create a Simple Data Science App with Streamlit

![image:](/assets/images/app1.png)

You’ve just created a stunning data science model. You’re proud of your work, but lobbing over the .py file just doesn’t seem like a worthy way of sharing it. If only there was a quick-to-learn web app that would do justice to your marvelous project... 



## Why Streamlit?
Streamlit is an open-source Python library compatible with major Python libraries like Matplotlib, Plotly, Pandas, numpy, scikit-learn, etc that While Streamlit may not be the most widely used data web science app framework, it is definitely one of the easiest and quickest to learn. Snowflake seems to have seen some potential in it too, as the cloud company [recently acquired Streamlit for $800m](https://techcrunch.com/2022/03/02/snowflake-acquires-streamlit-for-800m-to-help-customers-build-data-based-apps/). If beautiful, easy-to-build and quick-to-deploy apps aren't enough to entice you, Streamlit is also FREE to use.



## Installing Streamlit:

```
pip install streamlit
```
Opening your terminal of choice and entering a simple 'pip install' should do the trick, though a more detailed installation guide can be found [on Streamlit's web page](https://docs.streamlit.io/library/get-started/installation#install-streamlit-on-windows)
  
  
  
  
## Using Streamlit



### Import the Streamlit Library
Once Streamlit is installed, integrating your project with Streamlit's framework is fairly simple. To start, we'll import the library:
```
import streamlit as st  
```


### Configure your app

Streamlit has a respectable array of options when it comes to styling and configuring your app. In this case, we are going to create a title for our app, then set the it to a wide layout with the side bar expanded using the following syntax: 
```
st.set_page_config(
    page_title="Sample Streamlit App",
    layout="wide",
    initial_sidebar_state="expanded",
)
```
I've had to make some emergency modifications to my blog. Please re-visit this on Monday to grade me properly. Sorry for the inconvenience!
