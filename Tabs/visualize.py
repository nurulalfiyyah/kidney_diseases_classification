# Importing necessary libraries and modules
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn import tree
import streamlit as st
from web_functions import train_model

# Defining the visualization app function
def app(df, x, y):
    # Suppressing warnings and configuring streamlit options
    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    
    # Setting up the title for the Streamlit app
    st.title("Kidney Stone Prediction Visualization")

    # Checking if the user wants to plot the confusion matrix
    if st.checkbox("Plot Confusion Matrix"):
        # Training the model and obtaining predictions
        model, score = train_model(x, y)
        y_pred = model.predict(x)
        
        # Calculating and plotting the confusion matrix
        cm = confusion_matrix(y, y_pred)
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                    xticklabels=['nockd', 'ckd'], yticklabels=['nockd', 'ckd'])
        plt.xlabel('Predicted labels')
        plt.ylabel('True labels')
        plt.title('Confusion Matrix')
        st.pyplot()
    
    # Checking if the user wants to plot the decision tree
    if st.checkbox("Plot Decision Tree"):
        # Training the model and exporting the decision tree visualization
        model, score = train_model(x, y)
        dot_data = tree.export_graphviz(
            decision_tree=model, max_depth=4, out_file=None, filled=True, rounded=True,
            feature_names=x.columns, class_names=['nockd', 'ckd']
        )
        st.graphviz_chart(dot_data)
