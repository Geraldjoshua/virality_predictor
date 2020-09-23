import DataClean as dc
import BuildModal as bm


def main():
    dc.clean_data()
    modal = bm.build_modal()

    # modal,X_train,X_test,y_train,y_test
    # if beedly wants to pass in new articles to predict chances of what articles will go viral
    # get input from the platform of new articles and passing that to this method
    # further coding
    # bm.get_predictions(modal, newarticledata)


if __name__ == "__main__":
    main()
