"""This module is responsible for feature selection in machine learning models."""


import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2


def chi_square(X, y):
    best_features = SelectKBest(score_func=chi2, k=10)
    fit = bestfeatures.fit(X, y)
    df_scores = pd.DataFrame(fit.scores_)
    df_columns = pd.DataFrame(X.columns)
    feature_scores = pd.concat([df_columns, df_scores], axis=1)
    feature_scores.columns = ['Specs', 'Score']
    print(feature_scores.nlargest(10, 'Score'))


def correlation(dataset, target):
    corr_mat = dataset.corr()
    top_corr_features = corr_mat.index
    plt.figure(figsize=(20, 20))
    g = sns.heatmap(dataset[top_corr_features].corr(), annot=True, cmap='RdYlGn')


def mutual_info(X, y):
    mutual_info = mutual_info_classif(X, y)
    mutual_data = pd.Series(mutual_info, index=X.columns)
    mutual_data.sort_values(ascending=False)
    print(mutual_data)


def recursive_elimination(X, y):
    from sklearn.feature_selection import RFE
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression()
    rfe = RFE(model, 7)
    fit = rfe.fit(X, y)
    print('Num Features: %d' % fit.n_features_)
    print('Selected Features: %s' % fit.support_)
    print('Feature Ranking: %s' % fit.ranking_)


def pca(X):
    from sklearn.decomposition import PCA
    pca = PCA(n_components=10)
    fit = pca.fit(X)
    print('Explained Variance: %s' % fit.explained_variance_ratio_)
    print(fit.components_)


def feature_importance(X, y):
    from sklearn.ensemble import ExtraTreesClassifier
    model = ExtraTreesClassifier()
    model.fit(X, y)
    print(model.feature_importances_)
    feat_importances = pd.Series(model.feature_importances_, index=X.columns)
    feat_importances.nlargest(10).plot(kind='barh')
    plt.show()