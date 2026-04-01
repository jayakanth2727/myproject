import json
import pandas as pd


with open("TEST DATA.json") as f:
    Data=json.load(f)

itr= Data["ITR"] ["ITR1"]
results_rows=[["Name", itr["PersonalInfo"]["AssesseeName"]["SurNameOrOrgName"]],
        ["PAN", itr["PersonalInfo"]["PAN"]],
         ["EmailId", itr["PersonalInfo"]["Address"]["EmailAddress"]],
         ["City", itr["CreationInfo"]["IntermediaryCity"]],
         ["Date of Birth", itr["PersonalInfo"]["DOB"]],
         ["Father's Name", itr["Verification"]["Declaration"]["FatherName"]],
         ["Aadhar Number", itr["PersonalInfo"]["AadhaarCardNo"]],
         ["Registered Address", itr["PersonalInfo"]["Address"]["LocalityOrArea"]],
         ["Contact Number", itr["PersonalInfo"]["Address"]["MobileNo"]],
         ["Number of House Properties", itr["PersonalInfo"]["Address"]["ResidenceNo"]],
         ["Resdential Status (Resident/Non-Resident)", itr["PersonalInfo"]["Address"]["RoadOrStreet"]],
         ["Taxpayer Identification Number of the Country", itr["PersonalInfo"]["Address"]["CountryCode"]],
         ["Original Return Filling Date", itr["FilingStatus"]["ItrFilingDueDate"]],
         ["Revised Return Filling Date", itr["FilingStatus"]["ReturnFileSec"]],
         ["Status","Individual"],
         ["Date of Incorporation","Not Aplicable"],
         ["Date of Commencement of Business","Not Aplicable"],
         ["CIN/LLPIN","Not Aplicable"],
         ["Is Company/Firm Domestic? (Y/N)","Not Aplicable"]				

]
df=pd.DataFrame(results_rows, columns=["Description", "Details"])
bank_lists=itr["Refund"]["BankAccountDtls"]["AddtnlBankDetails"]

bank_rows= []
for bank in bank_lists:
    bank_rows.append({"Bankname":bank["BankName"], "BankAccountNo":bank["BankAccountNo"], "BankFSCCode":bank["IFSCCode"]})
bank_=pd.DataFrame(bank_rows)
          




with pd.ExcelWriter("Final_ITR_Report.xlsx") as writer:
    df.to_excel(writer, sheet_name="Summary", index=False)
    bank_.to_excel(writer, sheet_name="Bank Details", index=False)
# df.to_excel("Final_ITR_Report.xlsx", index=False)
# df.to_excel("Final_ITR_Report.xlsx", index=False)


print("Excel file created successfully!")
