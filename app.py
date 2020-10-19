from flask import Flask, request, render_template ,jsonify
from flask_cors import cross_origin
import csv
import sklearn
import pickle
import pandas as pd
from datetime import datetime
from dateutil import relativedelta
from datetime import date
import pandas as pd
import os
from uuid import uuid4
from sklearn.preprocessing import LabelEncoder, StandardScaler, normalize



APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
model = pickle.load(open("random_forest_regression_model.pkl", "rb"))


test_data = pd.DataFrame()    
output_data = pd.DataFrame()     
 
@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")



@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":


        #Customer Name : 
        Cust_Name = request.form['Cust_Name']
        print("Customer Name :"+Cust_Name)
        
        #Customer Address : 
        Cust_Addr = request.form['Cust_Addr']
        print("Customer Address : " + Cust_Addr)
        
        #Established_Date : 
        today=date.today()
        delta= relativedelta.relativedelta(today,pd.to_datetime(request.form['Established_Dt']).date())
        Established_Date=(round(delta.years+(delta.months/12),2))
        print("Established Date : " + str(Established_Date))


        #Tenure_Date
        today=date.today()
        delta= relativedelta.relativedelta(today,pd.to_datetime(request.form['Tenure_Dt']).date())
        Tenure_Date=(round((delta.years+(delta.months/12)), 2))
        print("Tenure Date : " + str(Tenure_Date))
          
        Turnover = float(request.form['Turnover'])
        print("Turnover : " + str(Turnover))
        
        NumOfProducts = int(request.form['NumOfProducts'])
        print("NumOfProducts : " + str(NumOfProducts))
        
        Liquidity = float(request.form["Liquidity"])
        Payments = float(request.form["Payments"])
        Lending_Loan = float(request.form["Lending_Loan"])
        Trade = float(request.form["Trade"])
        Insurance = float(request.form["Insurance"])
        Agg_Blnc=  float(request.form["Agg_Blnc"]) 
        NoOfTransactions=  int(request.form["NoOfTransactions"]) 
        NoOfComplains=  int(request.form['NoOfComplains']) 
        Payments_Dues=  int(request.form['Payments_Dues']) 
        Diff_Blc_Amt=  float(request.form['Diff_Blc_Amt']) 
        print("Liquidity :"+ str(Liquidity))
        print("Payments :" + str(Payments))
        print("Lending_Loan :"+ str(Lending_Loan))
        print("Trade:"+ str(Trade))
        print("Insurance :"+ str(Insurance))
        print("Arggregate Balance :"+ str(Agg_Blnc))
        print("No Of Transactions :"+ str(NoOfTransactions))
        print("No Of Complains :"+ str(NoOfComplains))
        print("No Payments After due date:"+ str(Payments_Dues))
        print('%  difference in balance amount for 6 Months :' + str(Diff_Blc_Amt) )
        
        
        Cancellations= int(request.form['Cncl_Bill']) +int(request.form['Cncl_Payments']) +int(request.form['Cncl_Adj']) +int(request.form['Cncl_D_Adj']) +int(request.form['Cncl_C_Adj']) 
        
        print("Cancellations :" +str(Cancellations))
        
        Distance_To_Residence=request.form['DistanceToResidence']
        if(Distance_To_Residence =='High_Proximity'):
            DistanceToResidence = 0                 
        elif (Distance_To_Residence=='Low_Proximity'):
            DistanceToResidence = 1
        elif (Distance_To_Residence=='Medium_Proximity'):
            DistanceToResidence = 2
        print("DistanceToResidence : " + str(DistanceToResidence))
        
        Credit_Rating = request.form['Credit_Rating']
        if (Credit_Rating == 'A'):
            CreditRating = 0
        elif (Credit_Rating == 'B'):
            CreditRating = 1
        elif (Credit_Rating == 'C'):
            CreditRating = 2
          
        print("CreditRating  :"+ str(CreditRating))
        
        Industry = request.form['Industry']
        if (Industry == 'Manufaturing'):
            Industry_NBFI = 0
            Industry_Services = 0
           
        elif (Industry == 'NBFI'):
            Industry_NBFI = 1
            Industry_Services = 0
        
        elif (Industry == 'Services'):
            Industry_NBFI = 0
            Industry_Services = 1
           
        print("Industry_NBFI  :"+ str(Industry_NBFI))
        print("Industry_Services  :"+ str(Industry_Services))

        CustomerSegment = request.form["CustomerSegment"]
        if (CustomerSegment == 'Large_Customer'):
            CustomerSegment_Mid_customer= 0
            CustomerSegment_Small_customer= 0
           
        elif (CustomerSegment == 'Medium_Customer'):
            CustomerSegment_Mid_customer= 1
            CustomerSegment_Small_customer= 0
        
        elif (CustomerSegment == 'Small_Customer'):
            CustomerSegment_Mid_customer= 0
            CustomerSegment_Small_customer= 1
            
        print("CustomerSegment_Small_customer  :"+ str(CustomerSegment_Small_customer))
        print("CustomerSegment_Mid_customer  :"+ str(CustomerSegment_Mid_customer))

        
        Industry = request.form['HasCrCard']
        if (Industry == 'Yes'):
            HasCrCard = 0
        else:
            HasCrCard = 1 
            
        print("HasCrCard :"+ str(HasCrCard))

           
        test_data=[[
            CreditRating,
            Turnover,
            DistanceToResidence,
			NumOfProducts,
			Liquidity,
			Payments,
			Lending_Loan,
			Trade,
			Insurance,
			HasCrCard,
			Agg_Blnc,
			NoOfTransactions,
			Diff_Blc_Amt,
			Payments_Dues,
			NoOfComplains,
			Established_Date,
			Tenure_Date,
			Industry_NBFI,
			Industry_Services,
			CustomerSegment_Mid_customer,
			CustomerSegment_Small_customer,
			Cancellations
        ]]
        print(test_data)
        print("Out Put")
        prediction=model.predict(test_data)
        
        if (prediction[0] == 0 ):
            output='RIA PAS Predicted that the Customer '+Cust_Name + ' will not leave the bank'
        else:
            output='RIA PAS Predicted that the Customer '+Cust_Name + ' will leave the bank'
            
        
        
        print("Out Put")
        print(output)
        return render_template('home.html',prediction_text=output)


    return render_template("home.html")



@app.route("/predict_from_file", methods = ["GET", "POST"])
@cross_origin()
def predict_from_file():
    if request.method == "POST":
        print('I am here , please validate');
        file = request.form['upload-file']
        data = pd.read_excel(file)
        return render_template('data.html', data=data.to_dict())
    return 




today = date.today()

def calculate_age(dtob):
    today=date.today()
    delta= relativedelta.relativedelta(today,dtob)
    return (round((delta.years+(delta.months/12)), 2))

def label_encoder(data_: test_data, columns_name_: list):
    le = LabelEncoder()
    for i in columns_name_:
        le.fit(data_[i])
        data_[i] = le.transform(data_[i])
    return data_
    
    
@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'test_data/')
    # target = os.path.join(APP_ROOT, 'static/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    destination=''
    
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        print(filename)
        destination = "".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)
    
    print(destination)
    file = r''+destination
    data = pd.read_excel(file)
    test_data = pd.DataFrame(data) 
    print(test_data)
    
    establish_age=test_data['Established Date'].dt.date
    Age = [0] * len(establish_age)
    for  i in range(0,len(establish_age)):
        Age[i]=calculate_age(establish_age[i])
    test_data['Age']= Age
    test_data=test_data.drop(['Established Date'], axis = 1)
    
    
    Tenure=test_data['Tenure'].dt.date
    Tenure_ = [0] * len(Tenure)
    for  i in range(0,len(Tenure)):
        Tenure_[i]=calculate_age(Tenure[i])
    test_data['Tenure_']=Tenure_
    test_data=test_data.drop(['Tenure'], axis = 1)
    
    
    test_data = label_encoder(test_data, ['CreditRating'])
    test_data = label_encoder(test_data, ['DistanceToResidence'])
    test_data = label_encoder(test_data, ['HasCrCard'])
    
    test_data=pd.get_dummies(test_data,columns=['Industry','CustomerSegment'],drop_first=True)
    #print(test_data.iloc[:, 16:20])
    
    test_data.loc[:,'Cancellations'] = test_data.iloc[:,16:22].sum(axis=1)
    
    test_data=test_data.drop(['# of cancelled Bills in last 6 Months','# of cancelled Paymnets in last 6 Months','# of credit adjustments in last 6 Months','# of debit adjustments in last 6 Months','# of reversed/cancelled adjustments in last 6 Months'], axis = 1)
    
    output_data['CustomerId']=test_data['CustomerId']

    #We removed Customer ID ,Customer Address
    test_data=test_data.drop(['Customer Address','CustomerId'], axis = 1)
    
    print("OutPut")
    
    output_data['Exited'] = model.predict(test_data)
    
    output_data['Exit'] = output_data['Exited'].apply(lambda x: 'Yes' if x ==1 else 'No')
    
    print(output_data) 
    
    
    
    html_data=output_data.to_html()
    
    
    file_nm='D:\\DS\\RIA_ML\\Code\\Bank_Customer_Churn\\templates\\complete.html'
    txt_file=open(file_nm, "w")
    txt_file.write(html_data)
    txt_file.close()
    
    # return send_from_directory("images", filename, as_attachment=True)
    return render_template("complete.html" ,data =  html_data)



if __name__ == "__main__":
    app.run(debug=True)
