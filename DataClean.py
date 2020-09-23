# Load the Pandas libraries with alias 'pd'
import pandas as pd


def clean_data():
    # Read data the intend files from the file directory
    # picking the columns we need to analyzed
    data = pd.read_csv("files/shared_articles.csv", usecols=['contentId', 'url', 'title', 'text', 'lang'])
    dfarticles = pd.DataFrame(data)
    data2 = pd.read_csv("files/users_interactions.csv", usecols=['contentId', 'eventType'])
    dfusers = pd.DataFrame(data2)
    view = []
    bookmark = []
    like = []
    follows = []
    commentcreated = []
    for article in dfarticles.itertuples():
        views = 0
        bookmarks = 0
        likes = 0
        follow = 0
        comment_created = 0
        for user in dfusers.itertuples():
            if article.contentId == user.contentId:
                if user.eventType == "VIEW":
                    views += 1
                elif user.eventType == "FOLLOW":
                    follow += 1
                elif user.eventType == "BOOKMARK":
                    bookmarks += 1
                elif user.eventType == "LIKE":
                    likes += 1
                elif user.eventType == "COMMENT CREATED":
                    comment_created += 1
        view.append(views)
        bookmark.append(bookmarks)
        like.append(likes)
        follows.append(follow)
        commentcreated.append(comment_created)

    # add new columns t0 the pddataframe of the cleaned data csv
    dfarticles['views'] = view
    dfarticles['bookmarks'] = bookmark
    dfarticles['likes'] = like
    dfarticles['follow'] = follows
    dfarticles['commentcreated'] = commentcreated

    virality = []
    viralchances = []

    # create a column showing the result of the virality equation given
    for article in dfarticles.itertuples():
        viral = (1 * int(article.views)) + (4 * int(article.bookmarks)) + (10 * int(article.likes)) + (
                25 * int(article.follow)) + (100 * int(article.commentcreated))
        virality.append(viral)
        viralchances.append("High") if viral >= 500 else viralchances.append("Low")

    dfarticles['virality'] = virality
    dfarticles['viralchances'] = viralchances

    dfarticles.to_csv('files/cleaneddata.csv', index=False, encoding='utf-8')
