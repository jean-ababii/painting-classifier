# painting-classifier

The goal of this project is to deploy an app which can recognize the painting in front of the user, and give some additional details on it. This file explains all the steps I went through during this project.

On a personal level, my goal was to deepen my knowledge in the deep learning field by going through all the steps of a data science project: collecting the data, training a model and testing it, deploying it... Moreover, it is a nice way to discover or apply some technologies such as the cloud computing, transfer learning, data augmentation, or the app development.

## Goal of the wanted app

The final objective of this project is as follows: a visitor walks through a museum when he sees a very interesting painting, but unfortunately there is little information about it (only the name of the painter, the name and the year). He then takes out his smartphone, takes a picture of it and immediately obtains additional information about it (biography of the painter, information about the artistic style, painting techniques...). In case the app has incorrectly recognized the painting or does not have it in its database, it allows you to choose from among the most "similar" paintings. After starting my project and presenting it to friends, I realized that a very similar app already exists, called Smartify, and works in some very famous museums all over the world. However, this project having a purely educational vocation, that did not bother me.

## Data collection

During my internships or discussions with specialists in the data science field, I have often heard that the longest step is collecting and cleaning the data. This turned out to be true in my case, but it was just a very good opportunity for me to better understand the difficulties that we may encounter at this level. Indeed, during my internships, the databases necessary for training were provided directly, and I was only giving advice on acquiring new data. Moreover, during the various school projects I did, I often have used already existing datasets, well adapted to what we needed. 

In this project, the objective is to have many images from different points of view, different light exposures and different qualities for each painting, to help my trained model to "understand" each painting (but looking at the useful properties/patterns). This is why I directly limited my app to paintings, and in case of very good results, extend it to other art works such as sculptures for example. I chose the Louvre in Paris to set up my app, by limiting myself to one of the very numerous rooms of the museum. Indeed, according to the museum conditions, we have the right to take pictures of the paintings as much as we want, at the condition that we do not commercialize these images afterwards. 

I had to take many images for each painting under different angles, because many paintings look very similar. Therefore I made the decision to film each painting turning around it to have a lot of images. For each painting, I had a video of about 8 seconds with 60 frames per second, which corresponds to 8 x 60 = 480 images per painting approximatively.

ADD PICTURE

My validation dataset was directly composed of 20% of the available images. Theoretically, this is a desired thing since we want the distribution of the images making up these 2 categories to be as close as possible. However, in practice, the training images are extremely close to the validation databases, hence the false very good performance I was expecting and had.

At the same time, I took pictures of these paintings directly with my smartphone, introducing problems in a wanted way (blurred image, too far, too close, person walking in front, annoying reflections, several paintings at the same time...) in order to better simulate the use of the app by real users, in the worst case. The images acquired in this way compose my test database. Once these videos had been acquired for 55 paintings (limit imposed by lack of storage during my visit to the museum, but still largely sufficient), I extracted all the images making up each painting using the "Video to JPG converter”.

ADD PICTURE

ADD PICTURE

## Data preprocessing

Once the images were on my computer and distributed by folder, I used the ImageDataGenerator class from Keras, one of the deep learning frameworks. All my classes are named with a number between 1 and 55, because that "id" was making my work easier. The ImageDataGenerator class allowed me directly to provide the training and validation image directories to train a model. This step gave me a problem before finding this class because although I could see theoretically how to provide the data, I didn't know how to do it in practice because in the other projects I did, I directly had access to datasets already in a suitable format for training.

Moreover, I later added data augmentation in order to better generalize. Indeed, all the training pictures I had were very close from each other. Data augmentation was a nice way to simulate the kind of errors the users could do with this app, such as not center the painting or rotate the camera, but also environment problems such as different ambient light. This improved my results as I will show in the "Results" part.

## Model training

I decided to use the fine-tuning strategy, by using pre-trained networks on other databases, which consists in training only the last layers of the deep learning model to adapt it to your own data, because the basic patterns of a picture are already contained in the first layers of the model. It allows to have much better performance and therefore to reduce training time which can take a lot of time on image databases. In addition, keeping in mind my final idea of deployment on a mobile app, I chose to use a pre-trained Mobilenet V2 network, particularly suitable for deployment on embedded systems. I chose to use a classification on the image given as input, each of the 55 paintings representing one of the possible classes.

## Cloud computing

My personal GPU is not sufficiently powerful, this is why I decided to use cloud computing through Google's servers, the Colab service. Indeed, this service is precisely adapted to carry out school or educational projects by using the performance of the GPUs made available by Google. However, this service is not adapted if you have confidential data for example that should in no way end up on Google's servers. This is why I directly used powerful enough computers for the training during my internships. In addition, the use of Colab servers is limited to 12 consecutive hours in the case of a free account, even if there are tips to stop training every 12 hours and resume it directly at the point where it has stopped. By linking Google Colab to its Google Drive account, I was able to directly download all the training data to my Drive and access it from the Jupyter Notebook launched on the Colab service.

## Results

After comparing the expected results with the predicted results by my model on the test data and the data augmentation played a role. 

By "top 1" I only consider the class having the highest probability, and by "top 3" I consider the 3 classes having the highest probabilities.

### Without data augmentation 
 
Top 1 prediction: 24/72 (33.3% accuracy)

Top 3 prediction: 39/72 (54.2% accuracy)

### With data augmentation
 
Top 1 prediction: 35/72 (48.6% accuracy)

Top 3 prediction: 45/72 (62.5% accuracy)
 
## Mobile app

Coming soon

## Sources

For this project, my code was inspired of other projects or articles, which are listed below:

* Aryan Pegwar's article on Medium, especially for the visualization of the results and the transfer learning: 
https://medium.com/analytics-vidhya/how-to-do-image-classification-on-custom-dataset-using-tensorflow-52309666498e
* Vikas Gupta's and Anastasia Murzova's article, especially for the data augmentation:  
https://www.learnopencv.com/image-classification-using-convolutional-neural-networks-in-keras/
