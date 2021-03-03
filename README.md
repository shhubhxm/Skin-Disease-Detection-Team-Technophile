# Skin-Disease-Detection-Team-Technophile
We are team technophiles and participated in 48hrs hackathon organized by Nirma University in collabration with Binghamton University. Our Problem Definition : To develop a solution, the first step is to understand the problem. The problem here is to develop an Application Programming Interface which can be easily integrated with Android and IOS to detect the skin disease without any physical interaction with a Dermatologist. The detected skin disease should be sent through whatsapp to a particular patient and doctor.

Our college name: Pandit Deendayal Energy University
Team Members: Rushabh Thakkar, Divy Patel, Denish Kalariya, Yug Thakkar, and Shubham Vyas.

Project Details:

We made an application which classifies the skin diseases into these given types healthy, lupus, ringworm and scalp_infections 

How did we make?

The data given was analysed first. We came to conclusion that the data given was not enough so we searched for new datasets.
We got these datasets: 
https://ieee-dataport.org/documents/image-dataset-various-skin-conditions-and-rashes
https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T

We segregated the datasets of harvard. Combined all the datasets and trained the tensorflow image classification model multiple times.
Accuracy was not satisfying.

Augmented the data to unbaised the model and the dataset would be balanced.
Data Augmentation was done on the data given . We generated 800 images per disease.
Again we had trained the model.
Accuracy was good.
Exported the .tflite and label.txt file.

We imported the files into android studio

We have used three python codes:
data_removal.py
This code is used to remove data randomly from the folder if there are more number of images than required. We just need to change total_files_req variable in the code to number of files required after deletion.

data_augmentation.py

This code is used to augment the data randomly from the folder if there are less number of images than required. We just need to change total_files_req variable in the code to number of files required after augmentation. We change various parameters of images like clearity, rotation, brightness, etc.

image_classification_code.py

This is the main code in which we have trained the model and exported it to run on the app

  Models we tried:
        efficientnet-lite0(USED in our project)
        efficientnet-lite1
        efficientnet-lite2
        efficientnet-lite3
        efficientnet-lite4
        
  API:
        TensorFlowLite
        
  Used Android studio for App development .
Used Language = java
We sync all the grade files.
Changed the model files and update it with the new model
Working model file name is model.tflite
Tflite classifier working java files are 
CameraActivity.java
CamerConnectionFragment.java
ClasssifierActivity.java
LegacyCameraConnectionFreagment.java

Dataset: Uploaded on Github
 
 
 **WORKING MODEL LINK: https://drive.google.com/file/d/1BnqfFInFkJJDkYDlmdj9VB601f7PjTdj/view?usp=sharing**
