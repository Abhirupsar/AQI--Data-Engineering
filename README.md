# AQI--Data-Engineering. 

This project takes input pickles models created in the Air quality index projects. The regression_model refers to the random-forest created and optimised in the project.

The regression1_model refers to the KNN model which is created and optimised in the project. Random forest and KNN model have been selected as part modelling process in the frontend. 

The Randomforest has better accuracy and hence is the best fit for the AQI data. The KNN model was also chosen to use in the frontend since it's output had better variablility. Better variability helped me figure out if the models were working well in the frontend with changing model. 

The working library was set up in my local git and then extracted to github. The frontend used are Flask and HTML. Docker containers were made for the project. 
The requirement files which initially worked during Heroku deployment with Procfile had some version compatibility issues when creating docker image. So I made the docker image and container using an updated requirements file 'Requirements1' and deployed it in Heroku later. 

The project was successfully tested and all it's functionality ran well. The output deployment images is shown in the output folder. 
