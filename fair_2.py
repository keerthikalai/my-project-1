from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error


class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")
        #self.root.configure(background="#98c1d9")

        self.Nameoftablets=StringVar()
        self.ref=StringVar ()
        self.Dose=StringVar ()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose= StringVar()
        self.sideEfect=StringVar()
        self.FurtherInformation=StringVar ()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar ()
        self.PatientAddress=StringVar()

        lbltitle=Label(self.root, bd=10,relief=RIDGE, text = "WELL BEING - MANAGEMENT SYSTEM", bg="#ee6c4d", fg="white", font=("times new roman", 50, "bold"))
        lbltitle.pack (side=TOP, fill=X)
        
        # ======Dataframe============================= ======= =====================
        
        Dataframe = Frame(self.root, bd=10,relief=RIDGE, bg="#293241")
        Dataframe.place(x=0, y= 100,width=1530, height=550)

        DataframeLeft = LabelFrame(Dataframe, bd=10, padx=10, relief=RIDGE,font=("arial", 12, "bold"),text="Patient Information", bg="#293241", fg="white")
        DataframeLeft.place (x=0, y=3, width=900, height=400)
        DataframeRight = LabelFrame(Dataframe, bd=10, padx=5, relief=RIDGE,font=("arial", 12, "bold"), text="Prescription", bg="#293241", fg="white")
        DataframeRight.place(x=920, y=3, width=400, height=400)

        # ======Buttonframe============================= ======= =====================

        Buttonframe = Frame(self.root,bd=10,relief=RIDGE)
        Buttonframe.place(x=0,y=450,width=1530,height=70)

        # ======Detailsframe============================= ======= =====================

        Detailsframe = Frame(self.root,bd=10,relief=RIDGE,bg="#eff6e0")
        Detailsframe.place(x=0,y=500,width=1530,height=195)

        # ======Dataframeleft============================= ======= =====================

        lblNameTablet=Label (DataframeLeft, font=("arial", 10, "bold"), text="Name Of Tablets", padx=2, pady=6, bg="#293241", fg="white")
        lblNameTablet.grid (row=0, column=0, sticky=W)
        
        comNameTablet=ttk.Combobox(DataframeLeft,textvariable=self.Nameoftablets, state="readonly",font=("arial", 10, "bold"), width=33)
        comNameTablet['value'] =("Nice", "Corona Vacacine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan")
        comNameTablet.current (0)
        comNameTablet.grid (row=0, column=1)
        
        lblref=Label (DataframeLeft, font=("arial", 10, "bold"), text="Refence No: ", padx=2, bg="#293241", fg="white")
        lblref.grid (row=1, column=0, sticky=W)
        txtref=Entry (DataframeLeft, font=("arial", 13), textvariable= self.ref,  width=35)
        txtref.grid (row=1, column=1)
        
        lblDose=Label (DataframeLeft, font= ("arial", 10, "bold"), text="Dose: ", padx=2, pady=4, bg="#293241", fg="white")
        lblDose.grid (row=2, column=0, sticky=W)
        txtDose=Entry (DataframeLeft, font=("arial", 13), textvariable= self.Dose, width=35)
        txtDose.grid(row=2, column=1)
        
        lblNoOftablets=Label (DataframeLeft, font=("arial", 10, "bold"), text="No Of Tablets::", padx=2, pady=6, bg="#293241", fg="white")
        lblNoOftablets.grid(row=3, column=0, sticky=W)
        txtNoOftablets=Entry (DataframeLeft, font=("arial", 13), textvariable= self.NumberofTablets,  width=35)
        txtNoOftablets.grid(row=3, column=1)

        lblLot=Label (DataframeLeft, font=("arial", 10, "bold"), text="Lot:", padx=2, pady=6, bg="#293241", fg="white")
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot=Entry (DataframeLeft, font=("arial", 13), textvariable=self.Lot ,  width=35)
        txtLot.grid(row=4, column=1)

        lblissueDate=Label (DataframeLeft, font=("arial", 10, "bold"), text="Issue Date:", padx=2, pady=6, bg="#293241", fg="white")
        lblissueDate.grid(row=5, column=0, sticky=W)
        txtissueDate=Entry (DataframeLeft, font=("arial", 13), textvariable=self.Issuedate ,  width=35)
        txtissueDate.grid(row=5, column=1)

        lblExpDate=Label (DataframeLeft, font=("arial", 10, "bold"), text="Exp Date:", padx=2, pady=6,bg="#293241", fg="white")
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate=Entry (DataframeLeft, font=("arial", 13), textvariable=self.ExpDate ,  width=35)
        txtExpDate.grid(row=6, column=1)

        lblDailyDose=Label (DataframeLeft, font=("arial", 10, "bold"), text="Daily Dose:", padx=2, pady=6, bg="#293241", fg="white")
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose=Entry (DataframeLeft, font=("arial", 13), textvariable=self.DailyDose ,  width=35)
        txtDailyDose.grid(row=7, column=1)

        lblSideeffect=Label (DataframeLeft, font=("arial", 10, "bold"), text="Side Effect:", padx=2, pady=6, bg="#293241", fg="white")
        lblSideeffect.grid(row=8, column=0, sticky=W)
        txtSideeffect=Entry (DataframeLeft, font=("arial", 13), textvariable=self.sideEfect ,  width=35)
        txtSideeffect.grid(row=8, column=1)
#=========
        lblBloodPressure=Label (DataframeLeft, font=("arial", 10, "bold"), text="Blood Pressure:", padx=2, pady=6, bg="#293241", fg="white")
        lblBloodPressure.grid(row=1, column=2, sticky=W)
        txtBloodPressure=Entry (DataframeLeft, font=("arial", 13), textvariable=self.DrivingUsingMachine ,  width=35)
        txtBloodPressure.grid(row=1, column=3)

        lblStorageAdvise=Label (DataframeLeft, font=("arial", 10, "bold"), text="Storage Advise:", padx=2, pady=6, bg="#293241", fg="white")
        lblStorageAdvise.grid(row=2, column=2, sticky=W)
        txtStorageAdvise=Entry (DataframeLeft, font=("arial", 13), textvariable=self.StorageAdvice ,  width=35)
        txtStorageAdvise.grid(row=2, column=3)

        lblMedication=Label (DataframeLeft, font=("arial", 10, "bold"), text="Medication:", padx=2, pady=6, bg="#293241", fg="white")
        lblMedication.grid(row=3, column=2, sticky=W)
        txtMedication=Entry (DataframeLeft, font=("arial", 13), textvariable=self.HowToUseMedication ,  width=35)
        txtMedication.grid(row=3, column=3)

        lblPatientID=Label (DataframeLeft, font=("arial", 10, "bold"), text="Patient ID:", padx=2, pady=6, bg="#293241", fg="white")
        lblPatientID.grid(row=4, column=2, sticky=W)
        txtPatientID=Entry (DataframeLeft, font=("arial", 13), textvariable=self.PatientId ,  width=35)
        txtPatientID.grid(row=4, column=3)

        lblNHSNumber=Label (DataframeLeft, font=("arial", 10, "bold"), text="NHS Number:", padx=2, pady=6, bg="#293241", fg="white")
        lblNHSNumber.grid(row=5, column=2, sticky=W)
        txtNHSNumber=Entry (DataframeLeft, font=("arial", 13), textvariable=self.nhsNumber ,  width=35)
        txtNHSNumber.grid(row=5, column=3)

        lblPatientName=Label (DataframeLeft, font=("arial", 10, "bold"), text="Patient Name:", padx=2, pady=6, bg="#293241", fg="white")
        lblPatientName.grid(row=6, column=2, sticky=W)
        txtPatientName=Entry (DataframeLeft, font=("arial", 13), textvariable=self.PatientName ,  width=35)
        txtPatientName.grid(row=6, column=3)

        lblDateOfBirth=Label (DataframeLeft, font=("arial", 10, "bold"), text="Date Of Birth:", padx=2, pady=6, bg="#293241", fg="white")
        lblDateOfBirth.grid(row=7, column=2, sticky=W)
        txtDateOfBirth=Entry (DataframeLeft, font=("arial", 13), textvariable=self.DateOfBirth ,  width=35)
        txtDateOfBirth.grid(row=7, column=3)

        lblPatientAddress=Label (DataframeLeft, font=("arial", 10, "bold"), text="Patient Address:", padx=2, pady=6, bg="#293241", fg="white")
        lblPatientAddress.grid(row=8, column=2, sticky=W)
        txtPatientAddress=Entry (DataframeLeft, font=("arial", 13), textvariable=self.PatientAddress ,  width=35)
        txtPatientAddress.grid(row=8, column=3)

        lblFurtherInfo=Label (DataframeLeft, font=("arial", 10, "bold"), text="Further Info:", padx=2, pady=6, bg="#293241", fg="white")
        lblFurtherInfo.grid(row=0, column=2, sticky=W)
        txtFurtherInfo=Entry (DataframeLeft, font=("arial", 13), textvariable=self.FurtherInformation ,  width=35)
        txtFurtherInfo.grid(row=0, column=3)

        #==========DataframeRight=====================================================================

        self.txtPrescription = Text(DataframeRight, font=("arial",12,"bold"),width=40,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        #==========Buttons=====================================================================

        btnPrescription=Button(Buttonframe, command=self.iPrectioption, text="Presciption", bg="#98c1d9", fg="black", font=("arial",12,"bold"), width=21, padx=2, pady=6)
        btnPrescription.grid (row=0, column=0)

        btnPrescriptionData=Button(Buttonframe,command=self.iPrescriptionData, text="Presciption Data",bg="#98c1d9", fg="black", font=("arial", 12, "bold"),width=23, padx=2, pady=6)
        btnPrescriptionData.grid (row=0, column=1)

        btnUpdate=Button (Buttonframe, command=self.update_data, text="Update", bg="#98c1d9", fg="black", font=( "arial", 12, "bold"),width=21, padx=2, pady=6)
        btnUpdate.grid (row=0, column=2)

        btnDelete=Button(Buttonframe, command=self.idelete, text="Delete", bg="#98c1d9", fg="black", font=("arial", 12, "bold"),width=21, padx=2, pady=6)
        btnDelete.grid(row=0, column=3)

        btnClear=Button (Buttonframe,command=self.clear, text="Clear", bg="#98c1d9", fg="black", font=("arial", 12, "bold"),width=21, padx=2, pady=6)
        btnClear.grid (row=0, column=4)

        btnExit=Button(Buttonframe,command=self.iExit, text="Exit", bg="#98c1d9", fg="black", font=("arial", 12, "bold"), width=21, padx=2, pady=6)
        btnExit.grid(row=0,column=5)

        #=============Table==============================================================
        #=============scroolbar==============================================================
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe, column=("nameoftable","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable",text="Name Of Tablets")
        self.hospital_table.heading("ref",text="Ref")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No Of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")

        self.hospital_table["show"]="headings"

        self.hospital_table.column("nameoftable",width=40)
        self.hospital_table.column("ref",width=10)
        self.hospital_table.column("dose",width=20)
        self.hospital_table.column("nooftablets",width=10)
        self.hospital_table.column("lot",width=10)
        self.hospital_table.column("issuedate",width=10)
        self.hospital_table.column("expdate",width=10)
        self.hospital_table.column("dailydose",width=20)
        self.hospital_table.column("storage",width=40)
        self.hospital_table.column("nhsnumber",width=20)
        self.hospital_table.column("pname",width=30)
        self.hospital_table.column("dob",width=20)
        self.hospital_table.column("address",width=10)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

       # =====================Functinality Declration=========== ===========
    def iPrescriptionData (self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root", password="Pass@1234",port="3306", database="student_db")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.Nameoftablets.get(),
                    self.ref.get(),
                    self.Dose.get(),
                    self.NumberofTablets.get(),
                    self.Lot.get(),
                    self.Issuedate.get(),
                    self.ExpDate.get(),
                    self.DailyDose.get(),
                    self.sideEfect.get(),
                    self.FurtherInformation.get(),
                    self.StorageAdvice.get(),
                    self.DrivingUsingMachine.get(),
                    self.HowToUseMedication.get(),
                    self.PatientId.get(),
                    self.nhsNumber.get(),
                    self.PatientName.get(),
                    self.DateOfBirth.get(),
                    self.PatientAddress.get()
                    ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Record has been inserted")
            except Error as e:
                messagebox.showerror("Error", f"Error inserting record: {e}")


    def update_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Pass@1234", port="3306", database="student_db")
        my_cursor = conn.cursor()
        my_cursor.execute("UPDATE hospital SET Name_of_tablets=%s, Reference_No=%s, dose=%s, Numbersoftablets=%s, lot=%s, issuedate=%s, expdate=%s, dailydose=%s, sideefect=%s, furtherinfo=%s, storage=%s, drivingusingmachine=%s, medication=%s, patientid=%s, nhsnumber=%s, patientname=%s, DOB=%s, patientaddress=%s WHERE Reference_No=%s",
                      (
                          self.Nameoftablets.get(),
                          self.ref.get(),
                          self.Dose.get(),
                          self.NumberofTablets.get(),
                          self.Lot.get(),
                          self.Issuedate.get(),
                          self.ExpDate.get(),
                          self.DailyDose.get(),
                          self.sideEfect.get(),
                          self.FurtherInformation.get(),
                          self.StorageAdvice.get(),
                          self.DrivingUsingMachine.get(),
                          self.HowToUseMedication.get(),
                          self.PatientId.get(),
                          self.nhsNumber.get(),
                          self.PatientName.get(),
                          self.DateOfBirth.get(),
                          self.PatientAddress.get(),
                          self.ref.get()  # Assuming Reference_No is the primary key for the hospital table
                      ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Record has been updated successfully")

    

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="Pass@1234",port="3306",database="student_db")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursor_row= self.hospital_table.focus ()
        content= self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row [1])
        self.Dose.set(row [2])
        self.NumberofTablets.set(row [3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row [7])
        self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row [9])
        self.PatientName.set(row [10])
        self.DateOfBirth.set(row [11])
        self.PatientAddress.set(row[12])


    def iPrectioption(self):
        self.txtPrescription.insert(END, "Name of Tablets: \t\t\t" + self.Nameoftablets.get() + "\n")
        self.txtPrescription.insert(END, "Reference No: \t\t\t" + self.ref.get() + "\n")
        self.txtPrescription.insert(END, "Dose: \t\t\t" + self.Dose.get() + "\n")
        self.txtPrescription.insert(END, "Number Of Tablets:\t\t\t" + self.NumberofTablets.get() + "\n")
        self.txtPrescription.insert(END, "Lot:\t\t\t" + self.Lot.get() + "\n")
        self.txtPrescription.insert(END, "Issue Date: \t\t\t" + self.Issuedate.get() + "\n")
        self.txtPrescription.insert(END, "Exp date: \t\t\t" + self.ExpDate.get() + "\n")
        self.txtPrescription.insert(END, "daily Dose: \t\t\t" + self.DailyDose.get() + "\n")
        self.txtPrescription.insert(END, "Side Effect: \t\t\t" + self.sideEfect.get() + "\n")
        self.txtPrescription.insert(END, "Further Information:\t\t\t" + self.FurtherInformation.get() + "\n")
        self.txtPrescription.insert(END, "StorageAdvice: \t\t\t" + self.StorageAdvice.get() + "\n")
        self.txtPrescription.insert(END, "DrivingUsing Machine: \t\t\t" + self.DrivingUsingMachine.get() + "\n")
        self.txtPrescription.insert(END, "PatientId: \t\t\t" + self.PatientId.get() + "\n")
        self.txtPrescription.insert(END, "NHSNumber: \t\t\t" + self.nhsNumber.get() + "\n")
        self.txtPrescription.insert(END, "PatientName: \t\t\t" + self.PatientName.get () + "\n")
        self.txtPrescription.insert(END, "DateOfBirth:\t\t\t" + self.DateOfBirth.get() + "\n")
        self.txtPrescription.insert(END, "PatientAddress:\t\t\t" + self.PatientAddress.get() + "\n")


    def idelete(self):
        conn=mysql.connector.connect(host='localhost', user='root', password='Pass@1234', port='3306', database='student_db')
        my_cursor=conn.cursor()
        query="delete from hospital where Reference_No=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","Patient has been deleted successfully")


    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.sideEfect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine. set ("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0", END)


    def iExit(self):
        iExit=messagebox.askyesno("Hospita Management System","Confirm you want to exit ?")
        if iExit>0:
            root.destroy()
            return

root = Tk()
ob = Hospital(root)
root.mainloop()





















