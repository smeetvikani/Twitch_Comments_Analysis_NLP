![Sklearn logo](Twitch_Purple_RGB.png)

### Table of Contents
[1. Project Overview](#section-a)  
[2. Tools Used](#section-b)  
[3. Data Distribution](#section-b2)  
[4. Phase 1, Multivariate Classification Models](#section-c)    
[5. Phase 2, Binary Classification Model](#section-c2)   
[6. Phase 2, Establish Threshold](#section-c3)  
[7. Final Results](#section-e)  
[8. Flask App](#section-end)  
[9. Github Repo - Link](https://github.com/smeetvikani/AirBnB_User_Behavior_Classification)


---

### <a name="section-a"></a>1.  Project Overview
##### This project is a prototype enchancement to existing video replay feature on twitch. 
Twitch is a online streaming platform with 100+ Million active monthly users. People around the world sign on to watch their favorite player play their favorite game. 

* The 3 goals for this project are:
 * Capture crowd reaction in terms of chat messages. 
 * Identify “Epic Moments” using message volume and discussion topics in the chat messages over the video timeline.
 * Build An App that would allow the users to navigate 5 mins of valuable gameplay in a 6+ hour video. 

* Chat Data was collected using the scraper in the repo: Twitch-Chat-Downloader
	* Device Used
	* Signup Method
	* Age

* Dynamic User Data (Sessions) :
	* Active Session Time
	*  Buttons Clicked
	*  Active Browser type
* 10 Million User activity data points were used for the analysis. 
* A total of 190 Features were generated using these data points. 

#### Project Broken Down into two Phases: 
* Multiclass Classification
* Binary Classification 

---

### <a name="section-b"></a>2.  Tools Used

#### Sklearn, Postgres SQL, Flask, Plotly, D3, Python, Pandas, Matplotlib and Seaborn, Jupyter Notebook, HTML, CSS,.

#### 3. Algorithms used: 
*   Logistic Regression
*   KNN
*   SVM (Support Vector Machines)
*   Ensamble Random Forest Classifier 
*   Decision Tree Classifier
*   Tuning: Sklearn GridSearchCV

---
### <a name="section-b2"></a>3.  Data Distribution
Exploratory Data Analysis was performed on the age distribution of the target demographic. Below is a plot created using Seaborn, represents the histogram of average Air B%B user age.
![Map](http://downloadforpc.net/Metis/project4/plots/fig.jpeg)

---
### <a name="section-c"></a> Multivariate Classification Models

##### Phase 1: Choosing Algorithm

Tested Initial Data using Various Models: Each Model was Cross Validated Using Test Sets. Below is the test data model summary. 
![Map](http://downloadforpc.net/Metis/project4/plots/compare.jpeg)
Best Performing model was Random Forest Classifier. There results were not significat due to high class imbalance. 
![Map](http://downloadforpc.net/Metis/project4/plots/rfc_score.png)



### <a name="section-c2"></a> Phase 2, Binary Classification Model
Due to high class imbalance, we were unable to get significant results from multivariate classificaiton. In order to derive significant results from the data, I narrowed down the classes to find just users travelling in the States vs the rest of the world. 

As you can see below Logistic Regression, outperformed random forest classifier by a large margin. Scoring Metric was F1 Score, with a good balance of accuray and recall. 
![Map](http://downloadforpc.net/Metis/project4/plots/compare2.jpeg)


Listed below are the features with the highest impact on the model. R Squared of this model remained consistant with the test set, we can conclude there was no overfitting. 
![Map](http://downloadforpc.net/Metis/project4/plots/coef.jpeg)





### <a name="section-c3"></a> Phase 2, Establish Threshold

Challenge: Choosing the right threshold. How to determine that this is the most effective threshold?

* Solution 1, Precision Recall Curve: It helps determine a good balance between precision and recall.
* Solution 2, Create a custom Cost Function.  


##### Testing the threshold via custom cost function: 

* TP=Advertised Correctly. Gain 1.5$
* FN= Miss Opportunity. Loss  1/2$ 
* FP= Wrong Demographic. Loss 1/2$ 
* Best Threshold  .35
* Profit Margin of 4,000$ with this model and threshold.
![Map](http://downloadforpc.net/Metis/project4/plots/first_joint.jpeg)



### <a name="section-e"></a> Final Results: 

Best Performing model for the binary dataset was Logistic Regression. Model Accurately predicts 82% percent of us Customers, while minimizing loss on False Positives. 

Details on the model below: 

| Metric   |      Before TH      |  After TH |
|----------|:-------------:|------:|
| Recall |  .74 | .82 |
| Precision |  .47   |   .43 |
| F1 | .58  |    .57 |

![Map](http://downloadforpc.net/Metis/project4/plots/confusion.jpeg)


### <a name="section-end"></a> App:

<iframe width="560" height="315" src="https://www.youtube.com/embed/cy9QusUc8Is" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>



### <a name="section-end"></a> Contact:
Thank you for visiting the page, feel free to contact me at smeet.vikani@gmail.com
