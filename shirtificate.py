from fpdf import FPDF

class Shirtificate(FPDF):
	def __init__(self, name):
		super().__init__()
		self.add_page()
		self.set_font("helvetica", "B", 50)
		self.cell(
            190,
            9,
            "CS50 Shirtificate",
            border=1,
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
            fill=False
        )
		self.image("shirtificate.png", w=self.epw)
		self.set_font_size(30)
		self.set_text_color(255, 255, 255)
		self.text(x=47.5, y=140, txt=f"{name.title()} took CS50")


shirtificate = Shirtificate(input("Name: "))
shirtificate.output("shirtificate.pdf")