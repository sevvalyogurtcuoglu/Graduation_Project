# Music Genre Classification and Recommendation System


Music is an art that most people use in their daily lives. Therefore, music services have become the primary means for people to listen to the music they love. Music services offer a personalized experience by looking at the actionsof the users. When similar music pieces are recommended to the user, the user can easily access the music he / she can love.

![image](https://user-images.githubusercontent.com/33968347/87854061-a05b7300-c917-11ea-8cba-76873cb25b00.png)

In this project developed the following steps have been implemented.

![image](https://user-images.githubusercontent.com/33968347/87854312-c41fb880-c919-11ea-8ab4-9325d81913ac.png)

## DATASET

The music data used in the project is [fma_medium.zip](https://github.com/mdeff/fma) data created by [FMA](https://freemusicarchive.org/search).

* When music files were downloaded, it was observed that there were unlabeled data, so first of all  the data was labelled.
* The data set consists of 25,000 tracks of mp3 and 16 genres, each 30 seconds long. 6 different genres (blues, classical, electronic, hip-hop, metal, punk) were selected for this project and a data set was created.

* **librosa** library was used for feature extraction in the processing . ( [**data_processing.py**](https://github.com/sevvalyogurtcuoglu/Graduation_Project/blob/master/data_processing.py) )
 *information: librosa library accepts music in wav format, data has been converted from mp3 to wav. ( [**conversion_format.py**](https://github.com/sevvalyogurtcuoglu/Graduation_Project/blob/master/conversion_format.py) )*
 
 ## Classification and Performance Evaluation
* While classifying, modeling was done with *knn, decision tree, random forest and naive bayes*.
* Hyperparameter tuning processing were performed to obtain the best performance results. ( [**classification.py**](https://github.com/sevvalyogurtcuoglu/Graduation_Project/blob/master/classification.py) )
* Comparison of classification algorithms for accuracy values
![image](https://user-images.githubusercontent.com/33968347/87861662-fdbfe600-c950-11ea-9089-d378b1e8db11.png)

* The model trained with Random forest for use in the recommendation system was saved ( [**train.py**](https://github.com/sevvalyogurtcuoglu/Graduation_Project/blob/master/train.py) ). Model registration was carried out with the **joblib** module ( [**modell.pkl**](https://github.com/sevvalyogurtcuoglu/Graduation_Project/blob/master/modell.pkl) ).

## Recommendation System
In this project, content based filtering was used because only the music information was available.

![image](https://user-images.githubusercontent.com/33968347/87862108-3cf03600-c955-11ea-9f64-ac67f1341844.png)

* **The cosine similarty** function was used to understand the relationship between the selected music and the attribute values of other music.

### Cosine Similarty
![image](https://user-images.githubusercontent.com/33968347/87862156-b851e780-c955-11ea-9b9c-0831c2bb6402.png)![image](https://user-images.githubusercontent.com/33968347/87862159-bf78f580-c955-11ea-9fad-9a895301bd0c.png)

* The similarity ratio of the music uploaded to the system with other music is listed from high to low.
* Top 5 music names on the list are taken.

![image](https://user-images.githubusercontent.com/33968347/87862357-d6b8e280-c957-11ea-8a15-b4b0784932f2.png)
![image](https://user-images.githubusercontent.com/33968347/87862359-db7d9680-c957-11ea-8dec-7e892629ba1a.png)

## Graphical User Interface ( GUI )

