from flat import Bill, Flatmate

from reports import PdfReport, FileSharer

bill_period = input("What is the period of the bill? eg. March 2021 ")
bill_amount = float(input("What is the amount of the bill? "))
the_bill = Bill(bill_amount, bill_period)

counter = 1
flatmates = []
while True:
    if counter == 3:
        print("When finished do not enter a name")
    flatmate_name = input(f"What is the name of flatmate {counter}? ")
    if flatmate_name == "":
        if counter <= 2:
            print("There must be at least 2 flatmates!")
            continue
        else:
            break
    flatmate_days = int(input(f"How many days of {the_bill.period} was {flatmate_name} in the flat? "))
    flatmates.append(Flatmate(flatmate_name, flatmate_days))
    counter += 1

pdf_report = PdfReport(f"Flatmate's Bill {the_bill.period}.pdf")
pdf_report.produce(flatmates, the_bill)

file_sharer = FileSharer(pdf_report.filename)
print(file_sharer.share())
