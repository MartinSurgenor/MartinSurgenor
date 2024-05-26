# File: custom_module/models.py

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    employee_id = fields.Many2one('hr.employee', 'Employee')
    purchase_format_summary = fields.Text(string="Purchase Format of the product Summary")
    minimum_purchase_format_qty = fields.Float(string="Minimum Purchase Format Quantity")
    individual_minimum_purchase_qty = fields.Float(string="Quantity of the individual minimum purchase format")
    is_white_brand = fields.Boolean(string="Is White Brand")
    point_of_sale_fidelity = fields.Boolean(string="POS Fidelity")
    white_brand_name = fields.Char(string="White Brand Name")
    x_origen = fields.Text(string="Origin")
    certification_name = fields.Text(string="Certification Name")
    is_manufacture = fields.Boolean(string="Is Manufacture")
    pos_cross_sale = fields.Boolean(string="Point of Sale Cross Sale")
    web_cross_sales = fields.Boolean(string="WEB Cross Sales")
    pos_promotional_product = fields.Boolean(string="Point of Sale Promotional Product")
    web_promotional_product = fields.Boolean(string="WEB Promotional Product")
    point_of_sale_promotional_product = fields.Boolean(string="POS Promotional Product")
    pos_fidelity = fields.Boolean(string="Point of Sale Fidelity")
    web_fidelity = fields.Boolean(string="WEB Fidelity")
    profit = fields.Float(string="Profit")
    x_studio_tipo = fields.Text(string="Type")
    x_studio_estado = fields.Text(string="State")
    x_studio_protein = fields.Text(string="Protein")
    x_studio_gluten = fields.Text(string="Gluten")
    x_studio_lactose = fields.Text(string="Lactose")
    x_studio_sugar = fields.Text(string="Sugar")
    x_studio_edamam = fields.Text(string="Edamam")
    available_in_pos = fields.Boolean(string="Available in POS")
    x_studio_web = fields.Boolean(string="Sell on Web")
    warehouse_letter = fields.Char(string='Letter of the Warehouse')
    warehouse_number = fields.Char(string='Number of the Warehouse')
    company_brand = fields.Char(string="Company Brand")
    reordering_min_qty = fields.Float(string="Reordering Minimum Quantity")
    reordering_max_qty = fields.Float(string="Reordering Maximum Quantity")
    requested_qty = fields.Float(string='Requested Point')
    cross_sale_image_1 = fields.Binary(string='Cross Sale Image 1')
    cross_sale_image_2 = fields.Binary(string='Cross Sale Image 2')
    cross_sale_image_3 = fields.Binary(string='Cross Sale Image 3')
    image_1 = fields.Binary(string='Image 1')
    image_2 = fields.Binary(string='Image 2')
    image_3 = fields.Binary(string='Image 3')
    image_4 = fields.Binary(string='Image 4')
    official_source_url_1 = fields.Char(string='Official Source URL 1')
    a_beta_caroteno = fields.Char(string='A (Beta caroteno)')
    b1_tiamina = fields.Char(string='B1 (Tiamina)')
    b2_riboflamina = fields.Char(string='B2 (Riboflamina)')
    b3_niacina = fields.Char(string='B3 (Niacina)')
    b5_acido_pantotenico = fields.Char(string='B5 (Ácido Pantoténico)')
    b6_piridoxina = fields.Char(string='B6 (Piridoxina)')
    b8_biotina = fields.Char(string='B8 (Biotina)')
    b9_acido_folico = fields.Char(string='B9 (Ácido Fólico)')
    b12_cobalaminas = fields.Char(string='B12 (Cobalaminas)')
    c_acido_ascorbico = fields.Char(string='C (Ácido Ascórbico)')
    x_field_d = fields.Char(string='D')
    x_field_e = fields.Char(string='E')
    x_field_k = fields.Char(string='K')
    calcio = fields.Char(string='Calcio')
    cobre = fields.Char(string='Cobre')
    cromo = fields.Char(string='Cromo')
    fluor = fields.Char(string='Fluor')
    fosforo = fields.Char(string='Fosforo')
    hierro = fields.Char(string='Hierro')
    magnesio = fields.Char(string='Magnesio')
    potasio = fields.Char(string='Potasio')
    selenio = fields.Char(string='Selenio')
    yodo = fields.Char(string='Yodo')
    zinc = fields.Char(string='Zinc')
    energia = fields.Char(string='Energia')
    proteinas = fields.Char(string='Proteinas')
    fibra = fields.Char(string='Fibra')
    beneficios = fields.Text(string='Beneficios')
    beneficios_1 = fields.Text(string='Beneficios 1')
    beneficios_2 = fields.Text(string='Beneficios 2')
    beneficios_3 = fields.Text(string='Beneficios 3')
    beneficios_4 = fields.Text(string='Beneficios 4')
    beneficios_5 = fields.Text(string='Beneficios 5')
    beneficios_6 = fields.Text(string='Beneficios 6')
    beneficios_7 = fields.Text(string='Beneficios 7')
    official_source_url_2 = fields.Char(string='Official Source URL 2')
    x_studio_english_name = fields.Char('English Name')
    x_studio_pos_name = fields.Char('POS Name')
    x_studio_requested = fields.Float('Requested')
    point_of_sale_cross_sale = fields.Boolean('POS Cross Sale')