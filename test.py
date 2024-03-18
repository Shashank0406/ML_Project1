test = {'RandomForestRegressor': 0.8554945374769651, 'DecisionTreeRegressor': 0.7238447087146785, 'GradientBoostingRegressor': 0.8685176742230858, 'LinearRegression': 0.8695892052044775, 'KNeighborsRegressor': 0.4863503553155929, 'XGBRegressor': 0.8303876366808685, 'CatBoostRegressor': 0.8517542216500651, 'AdaBoostRegressor': 0.8368653818820684}

print(max(sorted(test.keys())))
          
best_model_score = max(sorted(test.keys()))
            
print(best_model_score)

x = list(test.keys())[
    list(test.values()).index(best_model_score)
]
print(x)

