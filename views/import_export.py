import json
from fpdf import FPDF

def import_recipe(file_path):
    with open(file_path, 'r') as file:
        recipe_data = json.load(file)
        save_recipe_to_db(recipe_data)

def export_recipe_to_pdf(recipe_id):
    recipe = get_recipe_by_id(recipe_id)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=recipe['title'], ln=True)
    pdf.multi_cell(0, 10, txt=recipe['instructions'])
    pdf.output(f"recipe_{recipe_id}.pdf")

def save_recipe_to_db(recipe_data):
    pass

def get_recipe_by_id(recipe_id):
    return {
        'title': 'Sample Recipe',
        'instructions': 'Sample instructions'
    }