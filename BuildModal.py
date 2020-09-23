# Import Python libraries for data manipuation and visualization
import pandas as pd

# Import the Python machine learning libraries we need
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics


def build_modal():
    data = pd.read_csv("files/cleaneddata.csv")
    dfarticles = pd.DataFrame(data)

    # Splitting the dataset into input and output features
    # virality is the feature to predict
    # "views", "bookmarks", "likes", "follow", "commentcreated" are the feature to make the prediction
    y = dfarticles["virality"]
    X = dfarticles[["views", "bookmarks", "likes", "follow", "commentcreated"]]

    # building a model

    # splitting into training and test sets
    test_size = 0.33
    seed = 7
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=seed)

    # select an Algorithm and make the modal
    modal = RandomForestClassifier(n_estimators=1000, random_state=0)

    # Fit model to the data
    modal.fit(X_train, y_train)

    # Evaluate the model on the test data
    prediction = modal.predict(X_test)

    # Model Accuracy, how often is the classifier correct?
    print(confusion_matrix(y_test, prediction))
    print(classification_report(y_test, prediction))

    print("Accuracy:", metrics.accuracy_score(y_test, prediction))

    # depends on actual viraliity
    viralchances = []
    for x in y_test:
        viralchances.append("High") if x >= 500 else viralchances.append("Low")

    # depends on predicted viraliity
    predviralchances = []
    for x in prediction:
        predviralchances.append("High") if x >= 500 else predviralchances.append("Low")

    df = X_test.copy()
    df["Article_id"] = dfarticles["contentId"]
    df["Title"] = dfarticles["title"]
    df["lang"] = dfarticles["lang"]
    df['Actualvirality'] = y_test
    df['Actualviralchances'] = viralchances
    df['Predictionvirality'] = prediction
    df['Predictionviralchances'] = predviralchances
    df.to_csv('files/prediction.csv', index=False, encoding='utf-8')

    return modal


# further coding for the platform to use to run their new articles against the modal
# to predict viral articles
def get_predictions(modal, newArticleData):
    # use modal to find out which article will go viral
    prediction = modal.predict(newArticleData)
    # more to code
