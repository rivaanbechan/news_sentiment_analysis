import feedparser as fp
from textblob import TextBlob as tb
import re

# feed from CNN
worldNews = fp.parse('http://rss.cnn.com/rss/edition_world.rss')

# number of stories
numStories = len(worldNews['entries'])

# list to contain polarity of stories
final = []

for i in range(0,numStories):
    # initial description
    descInit = worldNews['entries'][i]['summary_detail']['value']
    # cleaning out the img tag
    descClean = re.sub('\<img.*$', '', descInit)
    # final description
    desc = tb(descClean)
    # title of the entry
    title = tb(worldNews['entries'][i]['title'])
    # final string which contains description and headline to get a better polarity result
    completeString = title + desc
    # appending story headline and descrition polarity to final list
    final.append(completeString.sentiment.polarity)

# polarity calculations
finalPolarity = sum(final)/len(final)
worstPolarity = final.index(min(final))
bestPolarity = final.index(max(final))

# display output of worst story
print(worldNews['entries'][worstPolarity]['title'], "-- Worst Story :(")
worstDesc = worldNews['entries'][worstPolarity]['summary_detail']['value']
worstDesc = re.sub('\<img.*$', '', worstDesc)
print(worstDesc)

print('\n')

# display output of best story
print(worldNews['entries'][bestPolarity]['title'], "-- Best Story :)")
bestDesc = worldNews['entries'][bestPolarity]['summary_detail']['value']
bestDesc = re.sub('\<img.*$', '', bestDesc)
print(bestDesc)

# overall polarity of news headlines. 50% is used as a starting baseline.
print('\nOverall Positivity: ', 50 - round(finalPolarity*100),"%")
