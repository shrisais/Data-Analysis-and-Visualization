library(sp)
library(twitteR)
library(plyr) 
library(data.table)
library(twitteR)
api_key<-"cbpTT7WVfKTJ5LwE5jDP8dDMP"
api_secret<-"TP98KNkfEzSCiTPMy0k56YAd08Ggr1yRPD8bBTjkCeyuHJu9O0"
acess_token<-"927608605322498051-v5kal4PUsJKIWJJa6whCRTbLTd0F1Nk"
access_token_secret<-"Nn9XnzAte7KIDMwz7000d8GxhZbHNhq5C7yl0nc7YiJds"
setup_twitter_oauth(api_key,api_secret,acess_token,access_token_secret)

tweets2 <- searchTwitter('#marketing',n=10000)
tw<-strip_retweets(tweets2)
final.df<-do.call("rbind",lapply(tw, as.data.frame))
write(final.df$text, file = "F:/Tweetsmarketing.txt")