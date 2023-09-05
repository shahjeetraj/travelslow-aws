from fpdf import FPDF

class Shirtificate(FPDF):
	def __init__(self, name):
		super().__init__()
		self.add_page()
		self.set_font("helvetica", "B", 20)
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
		self.image("shirtificate.png", x=0, y=50)
		self.set_font_size(30)
		self.set_text_color(255, 255, 255)
		self.text(190-(len(f"{name.title()} took CS50")*6.7),130, txt=f"{name.title()} took CS50")


shirtificate = Shirtificate(input("Name: "))
shirtificate.output("shirtificate.pdf")