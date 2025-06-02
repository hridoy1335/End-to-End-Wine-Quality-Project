from src.wine.logger import logging
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report



def model_evaluation(X_train,X_test,y_train,y_test,model):
    model.fit(X_train,y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    confu_matrix = confusion_matrix(y_test,y_pred)
    report = classification_report(y_test,y_pred)
    
    logging.info(f"accuracy score is {accuracy}")
            