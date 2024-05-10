def tune_knn_model(X_train, y_train):
    parameters = {'n_neighbors': range(1, 10)}
    knn = KNeighborsClassifier()
    clf = GridSearchCV(knn, parameters)
    clf.fit(X_train, y_train)

    return clf
