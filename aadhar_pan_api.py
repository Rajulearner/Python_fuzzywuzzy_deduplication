# from datapreprocessing import Row_list
from flask import Flask, request, jsonify,Response,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flaskext.mysql import MySQL
from datapreprocessing import df
import pymysql
app = Flask(__name__)
new_df = df
@app.route('/api/aadhar/<aadhar>',methods=['GET'])
def aadhar_check(aadhar):
    try:
        if len(aadhar)<=11 or len(aadhar)>=13:
            # raise "Input_Error"
            return jsonify({aadhar:"Check the input and try again"})
        # Iterate over each row 
        for index, rows in df.iterrows():  
            if aadhar in (rows.aadharNumber):
                firstName = rows['firstName']
                lastName = rows['lastName']
                gender=rows['gender']
                dob=rows['dob']
                location=rows['location']
                clientType=rows['clientType']
                aadharNumber=rows['aadharNumber']
                panCard=rows['panCard']
                return ({"firstName":firstName,"lastName":lastName,"gender":gender,"dob":dob,"location":location,"clientType":clientType,"aadharNumber":aadharNumber,"panCard":panCard})
            return {aadhar:"User details not found"}
    except TypeError:
        print("No Details Found Please Check Again")
print(df['panCard'])
@app.route('/api/pan/<pancard>',methods=['GET'])
def pan_check(pancard):
    try:
        print("Checking with pan")
        if len(pancard)<=9 or len(pancard)>=11 :
            # raise "Input_Error"
            return jsonify({pancard:"Check the input and try again"})
        for index, rows in new_df.iterrows():
            if pancard in rows.panCard:
                # my_list =[rows.firstName, rows.lastName, rows.gender, rows.dob, rows.location, rows.clientType, rows.aadharNumber, rows.panCard]
                # list_rows.append(my_list)
                firstName = rows['firstName']
                lastName = rows['lastName']
                gender=rows['gender']
                dob=rows['dob']
                location=rows['location']
                clientType=rows['clientType']
                aadharNumber=rows['aadharNumber']
                panCard=rows['panCard']
                return ({"firstName":firstName,"lastName":lastName,"gender":gender,"dob":dob,"location":location,"clientType":clientType,"aadharNumber":aadharNumber,"panCard":panCard})
        return {panCard:"User details not Found"} 
    except TypeError:
        print("No Details Found Please Check Again")

# if __name__ == '__main__':
#   app.run(debug=True)