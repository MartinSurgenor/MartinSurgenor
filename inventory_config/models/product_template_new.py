import base64
import xlrd
from odoo import models, fields, api
from odoo.exceptions import UserError


class ProductImportWizard(models.TransientModel):
    _name = 'product.import.wizard'
    _description = 'Product Import Wizard'

    file = fields.Binary('File', required=True)
    filename = fields.Char('Filename')

    def import_products(self):
        self.ensure_one()
        if not self.file:
            raise UserError('No file uploaded!')

        # Decode the file data
        file_data = base64.b64decode(self.file)
        wb = xlrd.open_workbook(file_contents=file_data)
        sheet = wb.sheet_by_index(0)

        # Get the headers
        headers = [sheet.cell_value(0, col) for col in range(sheet.ncols)]

        # Define the data mapping dictionary
        data = {
            'priority': 'priority',
            'responsible_id': 'responsible_id',
            'employee': 'Employee',
            'barcode': 'barcode',
            'barcode_ids': 'barcode_ids',
            'default_code': 'default_code',
            'name': 'name',
            'purchase_format_summary': 'Purchase Format of the product Summary',
            'minimum_purchase_format_qty': 'Minimun Purchase Format Quantity',
            'individual_minimum_purchase_qty': 'Quantity of the individual minimum purchase format',
            'is_white_brand': 'is_white_brand',
            'white_brand_name': 'white_brand_name',
            'x_origen': 'Origin',
            'certification_name': 'certification_name',
            'is_manufacture': 'is_manufacture',
            'pos_cross_sale': 'pos_cross_sale',
            'web_cross_sales': 'web_cross_sales',
            'pos_promotional_product': 'pos_promotional_product',
            'web_promotional_product': 'web_promotional_product',
            'pos_fidelity': 'pos_fidelity',
            'web_fidelity': 'web_fidelity',
            'profit': 'profit',
            'x_studio_tipo': 'Type',
            'x_studio_estado': 'State',
            'x_studio_protein': 'Protein',
            'x_studio_gluten': 'Gluten',
            'x_studio_lactose': 'Lactose',
            'x_studio_sugar': 'Sugar',
            'x_studio_edamam': 'Edamam',
            'available_in_pos': 'available_in_pos',
            'x_studio_web': 'Sell on Web',
            'warehouse_letter': 'Letter of the Warehouse',
            'warehouse_number': 'Number of the Warehouse',
            'company_brand': 'Company Brand',
            'reordering_min_qty': 'Reordering Minimum Quantity',
            'reordering_max_qty': 'Reordering Maximum Quantity',
            'requested_qty': 'Requested Point',
            'cross_sale_image_1': 'Cross Sale Image 1',
            'cross_sale_image_2': 'Cross Sale Image 2',
            'cross_sale_image_3': 'Cross Sale Image 3',
            'image_1': 'Image 1',
            'image_2': 'Image 2',
            'image_3': 'Image 3',
            'image_4': 'Image 4',
            'official_source_url_1': 'Official Source URL',
            'a_beta_caroteno': 'A (Beta caroteno)',
            'b1_tiamina': 'B1 (Tiamina)',
            'b2_riboflamina': 'B2 (Riboflamina)',
            'b3_niacina': 'B3 (Niacina)',
            'b5_acido_pantotenico': 'B5 (Ácido Pantoténico)',
            'b6_piridoxina': 'B6 (Piridoxina)',
            'b8_biotina': 'B8 (Biotina)',
            'b9_acido_folico': 'B9 (Ácido Fólico)',
            'b12_cobalaminas': 'B12 (Cobalaminas)',
            'c_acido_ascorbico': 'C (Ácido Ascórbico)',
            'x_field_d': 'D',
            'x_field_e': 'E',
            'x_field_k': 'K',
            'calcio': 'Calcio',
            'cobre': 'Cobre',
            'cromo': 'Cromo',
            'fluor': 'Fluor',
            'fosforo': 'Fosforo',
            'hierro': 'Hierro',
            'magnesio': 'Magnesio',
            'potasio': 'Potasio',
            'selenio': 'Selenio',
            'yodo': 'Yodo',
            'zinc': 'Zinc',
            'energia': 'Energia',
            'proteinas': 'Proteinas',
            'fibra': 'Fibra',
            'beneficios': 'Beneficios',
            'beneficios_1': 'Beneficios 1',
            'beneficios_2': 'Beneficios 2',
            'beneficios_3': 'Beneficios 3',
            'beneficios_4': 'Beneficios 4',
            'beneficios_5': 'Beneficios 5',
            'beneficios_6': 'Beneficios 6',
            'beneficios_7': 'Beneficios 7',
            'official_source_url_2': 'Official Source URL 2'
        }

        # Map the columns to the fields and create/update products
        Product = self.env['product.template']
        for row_idx in range(1, sheet.nrows):
            values = {}
            for col_idx, header in enumerate(headers):
                field_name = data.get(header)
                if field_name:
                    values[field_name] = sheet.cell_value(row_idx, col_idx)

            # Handle many2one and many2many fields if any
            for field, value in values.items():
                if field.endswith('_id') and isinstance(value, str):
                    related_model = field[:-3]
                    related_record = self.env[related_model].search([('name', '=', value)], limit=1)
                    if not related_record:
                        related_record = self.env[related_model].create({'name': value})
                    values[field] = related_record.id

                elif field.endswith('_ids') and isinstance(value, str):
                    related_model = field[:-4]
                    related_records = self.env[related_model].search(
                        [('name', 'in', [v.strip() for v in value.split(',')])])
                    if not related_records:
                        related_records = self.env[related_model].create(
                            [{'name': v.strip()} for v in value.split(',')])
                    values[field] = [(6, 0, related_records.ids)]

            # Check if the product already exists
            product = Product.search([('default_code', '=', values.get('default_code'))], limit=1)
            if product:
                product.write(values)
            else:
                Product.create(values)

        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }
