# -*- encoding: utf-8 -*-
import tweepy
import csv
import sys
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import operator
import re
from textblob import TextBlob

consumer_key = ''
consumer_secret = ''

access_token = ''
access_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

keyword = sys.argv[1]
print("execute script"+keyword)
fetch_tweets = tweepy.Cursor(api.search, keyword).items(100)

def clean_tweet(tweet):
    '''
    Utility function to clean tweet text by removing links, special characters
    using simple regex statements.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])| (\w +:\ / \ / \S +)", " ", tweet).split())

def get_tweet_sentiment(tweet):
    '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
    analysis = TextBlob(clean_tweet(tweet))
        # set sentiment
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 1
    else:
        return 0



with open('./public/tweets.csv', mode='w', newline = '', encoding='UTF-8') as my_file:
    my_writer= csv.writer(my_file, delimiter=',')
    
    my_writer.writerow(['Tweet_ID' , 'Tweet_Text', 'sentiment'])
    
    for i in fetch_tweets:
        Tweet_ID = str(i.id)
        Tweet_Text = str(i.text.replace('\n', ' ').replace(',',' ').replace('?',' '))
        sentiment = get_tweet_sentiment(Tweet_Text.replace('\n', ' ').replace(',',' ').replace('?',' '))
        my_writer.writerow([Tweet_ID , Tweet_Text, sentiment])

print("csv saved")
        
#df = pd.read_csv('tweets.csv')
#bool = df.loc[:,'sentiment'] == 1
#list1 = list(df[bool].index)

#Word Count
        
final_dictionary = {}
final_dictionary1 = {}

#if i in list1 :
with open('./public/tweets.csv', mode='r', encoding='UTF-8') as my_file:
    csv_reader = csv.reader(my_file, delimiter=',')
    line_count = 0
        
    for row in csv_reader:

        if row[2] == '1':
            
            if line_count == 1:
                line_count = line_count + 1
            else:
                line_count = line_count + 1
                txt = row[1]
                    
                final_txt = txt.lower()
                stop_words = set(stopwords.words('English'))
                tokenizer = RegexpTokenizer('r\W+|\w+')
                word_tokens = tokenizer.tokenize(final_txt)
                filtered_sentence = [w for w in word_tokens if not w in stop_words]

                filt = ['https', 'rt', 'co']
                for w in filtered_sentence:
                    if w not in filt:
                        if w not in final_dictionary:
                            final_dictionary[w] = 1
                        else:
                            final_dictionary[w] = final_dictionary[w] + 1
        else:
            if line_count == 1:
                line_count = line_count + 1
            else:
                line_count = line_count + 1
                txt1 = row[1]
                    
                final_txt1 = txt1.lower()
                stop_words1 = set(stopwords.words('English'))
                tokenizer1 = RegexpTokenizer('r\W+|\w+')
                word_tokens1 = tokenizer1.tokenize(final_txt1)
                filtered_sentence1 = [w for w in word_tokens1 if not w in stop_words1]

                filt = ['https', 'rt', 'co', 'tweet_text']
                for w in filtered_sentence1:
                    if w not in filt:
                        if w not in final_dictionary1:
                            final_dictionary1[w] = 1
                        else:
                            final_dictionary1[w] = final_dictionary1[w] + 1
            
                            
sorted_d = sorted(final_dictionary.items(), key=operator.itemgetter(1), reverse=True)[:30]
sorted_d2 = sorted(final_dictionary1.items(), key=operator.itemgetter(1), reverse=True)[:30]
# print(sorted_d)

#saving word count to a csv file
with open('./public/wordCount.csv', mode='w', newline = '', encoding='UTF-8') as my_file:
    my_writer = csv.writer(my_file, delimiter=',')
    
    my_writer.writerow(['text', 'frequency'])
    
    for key in sorted_d:
        current_Word = str(key[0])
        current_Count = int(key[1])
        
        my_writer.writerow([current_Word, current_Count])
        
with open('./public/wordCount1.csv', mode='w', newline = '', encoding='UTF-8') as my_file:
    my_writer = csv.writer(my_file, delimiter=',')
    
    my_writer.writerow(['text', 'frequency'])
    
    for key in sorted_d2:
        current_Word = str(key[0])
        current_Count = int(key[1])
        
        my_writer.writerow([current_Word, current_Count])        




        
