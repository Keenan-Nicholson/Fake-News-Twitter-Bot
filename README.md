# Fake-News-Twitter-Bot
@author Keenan Nicholson
@version 1.2
A silly twitter bot that receives tweets from one source and inserts them between tweets with quotation marks from a reputable source. This is my first attempt at a Twitter bot and was created in 2017 with the intent of learning the basics of Tweepy therefore it is unlikely to be updated any further.

To run:
  - insert consumer info and access key
  - insert user name of account with tweets to be inserted into the 'reputable source's' tweets as well as the reputable sources user name
  - pick a time to tweet (check Twitter guidelines beforehand as you will be banned for tweeting too often
  - NOTE: do not change the code to use @ mentions, you will be banned as bots can not mention accounts

Example output:
  - Receives tweet from user "not_a_reputable_source"
  - Receives tweet with quotation marks from "reputable source"
  - output: "Today president X released a statement from the whitehouse: "foo" "
