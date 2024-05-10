def one_hot_encode(data, column):
    return pd.get_dummies(data, columns=[column])
