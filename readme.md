![Sklearn logo](http://downloadforpc.net/Metis/fle/Twitch_Purple_RGB.png)

### Table of Contents
[1. Project Overview](#section-a)  
[2. Tools Used](#section-b)  
[3. Data Collection](#section-b2)  
[4. Modeling: Vectorize Data](#section-c)    
[5. Unsupervised: Generate Topics with NMF](#section-c)     
[6. Supervised: Coef Analysis of Topics Generated](#section-c2) 
[7. Future Plans](#section-e)  
[8. Flask App](#section-end)  
[9. Github Repo - Link](https://github.com/smeetvikani/Twitch_Comments_Analysis_NLP)


---

### <a name="section-a"></a>1.  Project Overview
Twitch is a online streaming platform with 100+ Million active monthly users. People around the world sign on to watch their favorite player play their favorite game. 

Designed an app that will enhance Twitch user experience for navigating saved replays. Specifically for game Fortnite, average length of a saved video is 5+ hours long. 

##### The 3 goals for this project are:
1.  Capture crowd reaction in terms of chat messages. 
2.  Identify “Epic Moments” using message volume and discussion topics in the chat messages over the video timeline.
3.  Build An App that would allow the users to navigate 5 mins of valuable gameplay/highlights in a 5+ hour video. 


## App Preview: 
<iframe width="560" height="315" src="https://www.youtube.com/embed/zRjbD_r42iM" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
---

### <a name="section-b"></a>2.  Tools Used

###### Sklearn, TSNE, Word2Vec, Flask, D3, Python, Pandas, Matplotlib and Seaborn, Jupyter Notebook, HTML, CSS,

#### 3. Algorithms used: 
*   Tokenizer (TfidfVectorizer) 
*   NMF (Non-negative matrix factorization)
*   GLM Model (Poisson) 
*   Linear Regression (Supervised Learning) 
*   K - Means Clustering (cosine distance) 

---
### <a name="section-b2"></a>3.  Data Collection
Raw JSON data on user comments per video basis was collected from from the Twitch API.

Twitch-Chat-Downloader was used to extract 450k comments from different videos. 

---
### <a name="section-c"></a> Vectorize Data and Generate Topics
##### Phase 1: Vectorize Data enhance TFIDF Vectorizer: 
A total of 150 Features were extracted using this method. 
Parameters for the model were:

* min_df= 0.10, max_df=0.90
* max_df = 0.90 means "ignore terms that appear in more than 90% of the documents".
* min_df = 0.90 means "ignore terms that appear in less than 10% of the documents".

This TFIDF Matrix was then leveraged into NMF Model. Most of the topics extracted were emojis, due to the high frequency in the sample. 

We will be using these emojis to identify the "epic plays" 
![Sklearn logo](http://downloadforpc.net/Metis/fle/topics.png)



### <a name="section-c2"></a> K - Means Clustering
Used to find optimal number of topics in the data sample. 

###### K-Means Elbow Plot:
![Sklearn logo](http://downloadforpc.net/Metis/fle/kmeans.jpeg)

###### PCA for 32 Clusters: Note these are unlabeled clusters. 

![Sklearn logo](http://downloadforpc.net/Metis/fle/pca-3d.png)

### <a name="section-c3"></a> Coef Analysis: Used supervised GLM (Poisson) to find the best topics

In order to find the best topics from the 32 clusters that we would like to model on the video time. Used supervised learning to assess which topics highly correlated with increase in comment counts. 

* Dependent Variable(y): Comments Per 30s
* Independent Variable(x): Topic Weights from NMF Model

![Sklearn logo](http://downloadforpc.net/Metis/fle/coefs.png)


Below is an overview of how topics and Dependent of comments were linked to find insightful footage. 

1. First Graph is a Rolling Mean volume of comment volume. 
2. Second Graph is the Selected 4/32 topics plotted on the video timeline. 

![Sklearn logo](http://downloadforpc.net/Metis/fle/VideoTimeLine.jpeg)
graph

### <a name="section-e"></a> Future Plans: 

Facial Analysis of the Twitch Player to Record Emotions of the player. This would provide us with valuable insight on what is transpiring in the gameplay. 

Amazon Rekognition was able to detected that player looked surprised with 75% accuracy. This information would be very insightful, when linked with the app. 

![Sklearn logo](http://downloadforpc.net/Metis/fle/facial_analysis.jpeg)

### <a name="section-end"></a> Contact:
Thank you for visiting my blog, If you have any questions free to contact me at smeet.vikani@gmail.com
