def explicar(modelo):

    if hasattr(modelo, "coef__"):
        return modelo.coef_.tolist()

    if hasattr(modelo, "feature_importances_"):
        return modelo.feature_importances_tolist()

    return []