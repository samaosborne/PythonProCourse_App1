from filestack import Client

from webbrowser import open as pdf_open

from fpdf import FPDF

from os import chdir as change_folder


class PdfReport:
    """
    Creates a pdf report that contains data about the flatmates such as their names,
    their due amounts and the period of their bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def produce(self, flatmate_list, bill, open=False):
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        pdf.image("files/house.png", w=30, h=30)

        col_width = [100, 150]
        row_height = [80, 40, 30]

        pdf.set_font(family="Arial", size=24, style="B")
        pdf.cell(w=0, h=row_height[0], txt="Flatmate's Bill", align="C", ln=1)

        pdf.set_font_size(16)
        pdf.cell(w=col_width[0], h=row_height[1], txt="Period:")
        pdf.cell(w=col_width[1], h=row_height[1], txt=bill.period, ln=1)

        pdf.set_font(family="Arial", size=14, style="")
        for flatmate in flatmate_list:
            pdf.cell(w=col_width[0], h=row_height[2], txt=flatmate.name)
            bill_share = round(flatmate.pays(flatmate_list, bill=bill), 2)  # rounding may affect total
            pdf.cell(w=col_width[1], h=row_height[2], txt=f"{bill.unit}{bill_share}", ln=1)

        change_folder("files")
        pdf.output(self.filename)
        if open:
            pdf_open(self.filename)


class FileSharer:
    """
    Uploads a file and creates a link to it, allowing the user to access and save the file
    """

    def __init__(self, filepath, api_key="AHk11Y2BMS2W8398bYhI0z"):
        self.api_key = api_key
        self.filepath = filepath

    def share(self):
        client = Client(self.api_key)
        file_link = client.upload(filepath=self.filepath)
        return file_link.url
