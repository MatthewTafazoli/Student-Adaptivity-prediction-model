from flask import Flask, request
from flask_restful import Api, reqparse

import joblib
import numpy as np

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('query')

@app.route('/json-example', methods=['POST'])
def json_pred():
    request_data = request.get_json()

    Gender = None
    Age = None
    Education_Level = None
    Institution_Type = None
    IT_Student = None
    Location = None
    Load_shedding = None
    Financial_Condition = None
    Internet_Type = None
    Network_Type = None 
    Class_Duration = None
    Self_LMS = None
    Device = None 

    query_values = []

    if request_data:
        if 'Gender' in request_data:
            if request_data['Gender'] == "Girl":
                Gender = 0
            elif request_data['Gender'] == "Boy":
                Gender = 1
            query_values.append(Gender)
        
        if 'Age' in request_data:
            if request_data['Age'] == "21-25":
                Age = 0
            if request_data['Age'] == "1-5":
                Age = 1
            if request_data['Age'] == "6-10":
                Age = 2
            if request_data['Age'] == "11-15":
                Age = 3
            if request_data['Age'] == "16-20":
                Age = 4
            if request_data['Age'] == "26-30":
                Age = 5
            query_values.append(Age)
        
        if 'Education Level' in request_data:
            if request_data['Education Level'] == "College":
                Education_Level = 2
            if request_data['Education Level'] == "School":
                Education_Level = 1
            if request_data['Education Level'] == "University":
                Education_Level = 0
            query_values.append(Education_Level)

        if 'Institution Type' in request_data:
            if request_data['Institution Type'] == "Government":
                Institution_Type = 0
            if request_data['Institution Type'] == "Non Government":
                Institution_Type = 1
            query_values.append(Institution_Type)

        if 'IT Student' in request_data:
            if request_data['IT Student'] == "No":
                IT_Student = 0
            if request_data['IT Student'] == "Yes":
                IT_Student = 1
            query_values.append(IT_Student)
        
        if 'Location' in request_data:
            if request_data['Location'] == "No":
                Location = 0
            if request_data['Location'] == "Yes":
                Location = 1
            query_values.append(Location)

        if 'Load-shedding' in request_data:
            if request_data['Load-shedding'] == "Low":
                Load_shedding = 1
            if request_data['Load-shedding'] == "High":
                Load_shedding = 0
            query_values.append(Load_shedding)

        if 'Financial Condition' in request_data:
            if request_data['Financial Condition'] == "Mid":
                Financial_Condition = 1
            if request_data['Financial Condition'] == "Poor":
                Financial_Condition = 2
            if request_data['Financial Condition'] == "Rich":
                Financial_Condition = 0
            query_values.append(Financial_Condition)

        if 'Internet Type' in request_data:
            if request_data['Internet Type'] == "Wifi":
                Internet_Type = 0
            if request_data['Internet Type'] == "Mobile Data":
                Internet_Type = 1
            query_values.append(Internet_Type)

        if 'Network Type' in request_data:
            if request_data['Network Type'] == "2G":
                Network_Type = 2
            if request_data['Network Type'] == "3G":
                Network_Type = 0
            if request_data['Network Type'] == "4G":
                Network_Type = 1
            query_values.append(Network_Type)

        if 'Class Duration' in request_data:
            if request_data['Class Duration'] == "1-3":
                Class_Duration = 1
            if request_data['Class Duration'] == "3-6":
                Class_Duration = 0
            if request_data['Class Duration'] == "0":
                Class_Duration = 2
            query_values.append(Class_Duration)
        
        if 'Self Lms' in request_data:
            if request_data['Self Lms'] == "No":
                Self_LMS = 0
            if request_data['Self Lms'] == "Yes":
                Self_LMS = 1
            query_values.append(Self_LMS)

        if 'Device' in request_data:
            if request_data['Device'] == "Computer":
                Device = 1
            if request_data['Device'] == "Tab":
                Device = 0
            if request_data['Device'] == "Mobile":
                Device = 2
            query_values.append(Device)

    else: 
        return "Error: No Request data given"

    def check_values(values):
        if None in values:
            for i, value in enumerate(values):
                if value == None:
                    yield f"Spelling/Case/Value problem with index #{i}" + "\n"
        else:
            loaded_model = joblib.load('Riiid_model.sav')
            query = np.reshape(query_values, (-1, 1)).T
            prediction = loaded_model.predict(query)
            if prediction[0] == 0:
                Adaptivity_Level = "Moderate"
            if prediction[0] == 1:
                Adaptivity_Level = "High"
            if prediction[0] == 2:
                Adaptivity_Level = "Low"
            yield Adaptivity_Level

    return check_values(query_values)

if __name__ == '__main__':
    app.run(debug=True)