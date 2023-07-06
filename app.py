from flask import Flask, render_template, request, make_response, session
import pickle
import numpy as np
import pandas as pd

from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, black



app = Flask(__name__)
app.secret_key = 'mysecretkey'
model = pickle.load(open('ckd.pkl', 'rb'))

@app.route('/',methods=['GET', 'POST'])

def index():
    
    if(request.method == 'POST'):

        data0 = request.form['name']
        data1 = request.form['age']
        data2 = request.form['bp']
        data3 = request.form['sg']
        data4 = request.form['al']
        data5 = request.form['su']
        data6 = request.form['rbc']
        data7 = request.form['pc']
        data8 = request.form['pcc']
        data9 = request.form['ba']
        data10 = request.form['bgr']
        data11 = request.form['bu']
        data12 = request.form['sc']
        data13 = request.form['sod']
        data14 = request.form['pot']
        data15 = request.form['hemo']
        data16 = request.form['pcv']
        data17 = request.form['wc']
        data18 = request.form['rc']
        data19 = request.form['htn']
        data20 = request.form['dm']
        data21 = request.form['cad']
        data22 = request.form['appet']
        data23 = request.form['pe']
        data24 = request.form['ane']
        
        session['data0'] = (data0)
        session['data1'] = float(data1)
        session['data2'] = float(data2)
        session['data3'] = float(data3)
        session['data4'] = float(data4)
        session['data5'] = float(data5)
        session['data6'] = float(data6)
        session['data7'] = float(data7)
        session['data8'] = float(data8)
        session['data9'] = float(data9)
        session['data10'] = float(data10)
        session['data11'] = float(data11)
        session['data12'] = float(data12)
        session['data13'] = float(data13)
        session['data14'] = float(data14)
        session['data15'] = float(data15)
        session['data16'] = float(data16)
        session['data17'] = float(data17)
        session['data18'] = float(data18)
        session['data19'] = float(data19)
        session['data20'] = float(data20)
        session['data21'] = float(data21)
        session['data22'] = float(data22)
        session['data23'] = float(data23)
        session['data24'] = float(data24)
        



        
        arr = np.array([[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data15,data16,data17,data18,data19,data20,data21,data22,data23,data24]])
        arr = arr.astype(float)
        pred = model.predict(arr)
        
        
        if(pred):
            return render_template("resultp.html")
        return render_template("resultn.html")


    return render_template("index.html")

@app.route('/download')
def download():

    data0 = session.get('data0', None)
    data1 = session.get('data1', None)
    data2 = session.get('data2', None)
    data3 = session.get('data3', None)
    data4 = session.get('data4', None)
    data5 = session.get('data5', None)
    data6 = session.get('data6', None)
    data7 = session.get('data7', None)
    data8 = session.get('data8', None)
    data9 = session.get('data9', None)
    data10 = session.get('data10', None)
    data11 = session.get('data11', None)
    data12 = session.get('data12', None)
    data13 = session.get('data13', None)
    data14 = session.get('data14', None)
    data15 = session.get('data15', None)
    data16 = session.get('data16', None)
    data17 = session.get('data17', None)
    data18 = session.get('data18', None)
    data19 = session.get('data19', None)
    data20 = session.get('data20', None)
    data21 = session.get('data21', None)
    data22 = session.get('data22', None)
    data23 = session.get('data23', None)
    data24 = session.get('data24', None)

    if(data6 == 0.0):
        data6 = 'normal'
    else:
        data6 = 'abnormal'
    if(data7 == 0.0):
        data7 = 'normal'
    else:
        data7 = 'abnormal'
    if(data8 == 0.0):
        data8 = 'notpresent'
    else:
        data8 = 'present'
    if(data9 == 0.0):
        data9 = 'notpresent'
    else:
        data9 = 'present'
    if(data19 == 0.0):
        data19 = 'no'
    else:
        data19 = 'yes'
    if(data20 == 0.0):
        data20 = 'no'
    else:
        data20 = 'yes'
    if(data21 == 0.0):
        data21 = 'no'
    else:
        data21 = 'yes'
    if(data22 == 0.0):
        data22 = 'good'
    else:
        data22 = 'poor' 
    if(data23 == 0.0):
        data23 = 'no'
    else:
        data23 = 'yes'
    if(data24 == 0.0):
        data24 = 'no'
    else:
        data24 = 'yes'   

    # Create a new PDF file
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)

    # Draw on the PDF
    pdf.drawImage("static\img\logo1.png", 50, 760, 35, 25)
    blue = HexColor("#153564")
    pdf.setFillColor(blue)
    pdf.setFont("Helvetica-Bold", 26)
    pdf.drawString(90, 760, f"CKD PREDICTION")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 720, f"Patient's Name: {data0}")
    pdf.drawString(50, 700, f"age: {data1}")
    pdf.drawString(50, 680, f"blood pressure: {data2}")
    pdf.drawString(50, 660, f"specific gravity: {data3}")
    pdf.drawString(50, 640, f"albumin: {data4}")
    pdf.drawString(50, 620, f"sugar: {data5}")
    pdf.drawString(50, 600, f"red blood cells: {data6}")
    pdf.drawString(50, 580, f"pus cell: {data7}")
    pdf.drawString(50, 560, f"pus cell clumps: {data8}")
    pdf.drawString(50, 540, f"bacteria: {data9}")
    pdf.drawString(50, 520, f"blood glucose random: {data10}")
    pdf.drawString(50, 500, f"blood urea: {data11}")
    pdf.drawString(50, 480, f"serum creatinine: {data12}")
    pdf.drawString(50, 460, f"sodium: {data13}")
    pdf.drawString(50, 440, f"potassium: {data14}")
    pdf.drawString(50, 420, f"hemoglobin: {data15}")
    pdf.drawString(50, 400, f"packed cell volume: {data16}")
    pdf.drawString(50, 380, f"white blood cell count: {data17}")
    pdf.drawString(50, 360, f"red blood cell count: {data18}")
    pdf.drawString(50, 340, f"hypertension: {data19}")
    pdf.drawString(50, 320, f"diabetes mellitus: {data20}")
    pdf.drawString(50, 300, f"coronary artery disease: {data21}")
    pdf.drawString(50, 280, f"appetite: {data22}")
    pdf.drawString(50, 260, f"pedal edema: {data23}")
    pdf.drawString(50, 240, f"anemia: {data24}")
    pdf.setFillColorRGB(255, 0, 0)
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, 220, f"CKD: Positive")
    pdf.drawString(50, 200, f"According to prediction based on patient's data, Patient have Chronic Kidney Disease.")
    pdf.save()

    # Set up the response
    response = make_response(buffer.getvalue())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=Report.pdf'

    return response


if __name__ == "__main__":
    app.run(debug=True)