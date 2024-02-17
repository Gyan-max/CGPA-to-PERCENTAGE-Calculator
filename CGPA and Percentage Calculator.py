def check(CPI):
  if CPI>=9.5:
    print("Your Corresponding CGPA to CPI is : 10")
  elif CPI<=9.45 and CPI>=9.00:
    print("Your corresponding CGPA to CPI : 9.5")
  elif CPI<=8.99 and CPI>=8.50:
    print("Your corresponding CGPA to CPI is : 9")
  elif CPI<=8.45 and CPI>=8.00:
    print("Your corresponding CGPA to CPI is : 8.5")
  elif CPI<=7.99 and CPI>=7.50:
    print("Your corresponding CGPA to CPI is : 8")
  elif CPI<=7.49 and CPI>=7.00:
    print("Your corresponding CGPA to CPI is : 7.5")
  elif CPI<=6.99 and CPI>=6.00:
    print("Your corresponding CGPA to CPI is : 7")                  
  elif CPI<=5.99 and CPI>=5.50:
    print("Your corresponding CGPA to CPi is : 6.5")
  elif CPI<=5.49 and CPI>=5.00:
    print("Your corresponding CGPA to CPI is : 6")
  else:
    print("CPI below 5.0 is considered as FAIL!!")
    

CPI=float(input("Enter your CPI here....   "))
check(CPI)

def percentage_marks(CGPA):
  print((CGPA-0.5)*10)

CGPA=float(input("Enter your CGPA/CPI here....    "))
percentage_marks(CGPA)  



                # ..................Author: Gyan....................