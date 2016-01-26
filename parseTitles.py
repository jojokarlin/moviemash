
import pandas as pd
import numpy as np
import os

rawMovies=pd.read_csv(filepath_or_buffer='movietitles.txt',
                      sep=';')
                      
rawMoviesList=rawMovies.values.tolist()

allTitles=[]
allReleaseYears=[]
allReviewYears=[]
for outIndex,outvalue in enumerate(rawMoviesList):
    joText=outvalue[0]

    joTitleCandidate=[]
    joReleaseYear=[]
    joReviewYear=[]
    wordsInParen=False
    foundLeft=False

    joSplit=joText.split(' ')

    for index,value in enumerate(joSplit):
        if ('(' not in value) and not foundLeft and not wordsInParen:
            joTitleCandidate.append(value)
        else:
            foundLeft==True
            if ')' in value:
                if (value[1:(len(value)-1)].isdigit()):
                    joReleaseYear.append(float(value[1:(len(value)-1)]))
                    joReviewYear.append(float(value[1:(len(value)-1)]))
                else:
                    joTitleCandidate.append(value)
                    foundLeft=False
            else:
                yearAndReview=joSplit[index:]
                releaseCan=yearAndReview[0][1:-1]
                reviewCan=yearAndReview[len(yearAndReview)-1][:-1]
                if not wordsInParen:
                    if (releaseCan.isdigit()):
                        joReleaseYear.append(float(releaseCan))
                        wordsInParen=True
                    if (reviewCan.isdigit()):
                        joReviewYear.append(float(reviewCan))
                        wordsInParen=True
        if (index==(len(joSplit)-1)):
            if(foundLeft==False) and joReleaseYear==[]:
                joReleaseYear=[np.nan]
                joReviewYear=[np.nan]
    joTitle=(' ').join(joTitleCandidate)
    print("Title=%s" % joTitle)
    print("Release year=%f" % joReleaseYear[0])
    print("Review year=%f" % joReviewYear[0])
    allTitles.append(joTitle)
    allReleaseYears.append(joReleaseYear[0])
    allReviewYears.append(joReviewYear[0])

allTitlesSeries=pd.Series(data=allTitles,name='Titles')
allReleaseYearsSeries=pd.Series(data=allReleaseYears,name='ReleaseYear')
allReviewYearsSeries=pd.Series(data=allReviewYears,name='ReviewYear')

movie=pd.DataFrame(allTitlesSeries)
movie['releaseYear']=allReleaseYearsSeries
movie['reviewYear']=allReviewYearsSeries









