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
