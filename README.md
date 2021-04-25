# Tweeter_Tweet_analysis

Tweeter Analysis Approach:

There are many tweets in the json file in fact more than 40 thousands.
Initially, I have convert it into csv file, So I could use it smoothly. Tried to find number of Keys, tweet_author and   tweet_text Therefore I got an idea about dataset.      
_key            43347
tweet_author    43347
tweet_text      43347

# Preprocessing

We can see in above tweet column in both data sets Training & Testing tweets are unstructured, for better analysis we first need to structure the tweets, remove the unwanted words, replace the misspelled words with the correct ones, replace the abbreviations with full words. 

Steps for preprocessing 

•	Converting html entities
•	Removing "@user" from all the tweets
•	Changing all the tweets into lowercase
•	Replacing Special Characters with space
•	Replacing Numbers (integers) with space
•	Removing words whom length is 1

Stemming : Stemming refers to the removal of suffices, like “ing”, “ly”, “s”, etc. 
Lemmatization: Lemmatization is the process of converting a word to its base form.
Will see the most commonly used words for both the columns.


    		
After that we have to analyze that our Author Tweet is Positive, Negative Or Neutral. There are many ways to predict sentiment. 
We haven’t any prior data which suggest positive or Negative tweet. That’s why we could not use any prediction model otherwise ML model perform well on that situation. 
I have chosen Text blob for prediction which gives positive, negative and both scenario in our tweets. 
