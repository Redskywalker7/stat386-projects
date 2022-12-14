---
layout: post
title:  "How to Create a Simple Data Science App with Streamlit"
date:   2022-09-22
author: "Luke McDowell"
description: Using one of the easiest web app tools to show off your data creations
image: /assets/images/streamlit.jpg
---



You’ve just created a stunning data science model. You’re proud of your work, but lobbing over the .py file just doesn’t seem like a worthy way of sharing it. If only there was a quick-to-learn web app that would do justice to your marvelous project... 


![image:](https://miro.medium.com/max/1400/0*6SYmw6X2cBxePujJ)


## Why Streamlit?
Streamlit is an open-source Python library compatible with major Python libraries like Matplotlib, Plotly, Pandas, numpy, scikit-learn, etc. While Streamlit may not be the most widely used web app framework, it is definitely one of the easiest and quickest to learn. Snowflake seems to have seen some potential in it too, as the cloud company [recently acquired Streamlit for $800m](https://techcrunch.com/2022/03/02/snowflake-acquires-streamlit-for-800m-to-help-customers-build-data-based-apps/).

If beautiful, easy-to-build and quick-to-deploy apps still aren't enough to entice you, Streamlit is also FREE to use.


  <br> 
  
## Using Streamlit



While Streamlit is most powerful when deployed as an online app hosted in a repository like github, for the purpose of this tutorial lets create a simple app that runs locally and determines whether an entered word is a palindrome or not.  We'll start by installing and importing the streamlit library, configuring our app, then integrating our function with Streamlit's framework.

 <br> 

### Installing Streamlit:


Opening your terminal of choice and entering a simple 'pip install' should do the trick, though a more detailed installation guide can be found [on Streamlit's web page].(https://docs.streamlit.io/library/get-started/installation#install-streamlit-on-windows)
  
```
pip install streamlit
```
  <br> 
  
  
### Configuring the App:

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
  <br> 
  
  
### Integrating our Work:

Now let's add our palindrome function before the main streamlit function for initialization purposes. 
```
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
```
 <br> 
 
### Utilizing the Widgets:

Lets add functionality to our app by referencing Streamlits helpful widget documentation. Within our main(): function, lets add and configure a title, [text input box](https://docs.streamlit.io/library/api-reference/widgets/st.text_input), and hang a pretty [image](https://docs.streamlit.io/library/api-reference/media/st.image). 

The app will beckon us to enter some text with which our palindrome app with return it's result in the style of a Streamlit metric. All our code should be encased within Streamlits framework as set out below:


```
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

 <br> 

### Running the App:

Once our .py is finalized, we'll save the file as 'streamlit_app.py' and save it to our local directory of choice. We'll then open up a new terminal window, navigate to the directory our file is found in and enter the following:
```
streamlit run streamlit_app.py
```    

This should produce the following:

![image:](https://i.ibb.co/c8zy0d1/Palindrome-Result.png)

<br> 

Horray!

Once you feel comfortable creating an app locally, deploying your app online is the next natural step. Thankfully, [Streamlit's webpage](https://docs.streamlit.io/) is awash with many helpful tips, cheatsheets and guides. 

There is no going back now, so happing app-baking!

