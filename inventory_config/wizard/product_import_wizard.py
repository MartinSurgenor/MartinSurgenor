import base64
import xlrd
from odoo import models, fields, api
from odoo.exceptions import UserError

relation_model_mapping = {
    'responsible_id': 'res.users',
    'uom_id': 'uom.uom',
    'categ_id': 'product.category',
    'pos_categ_ids': 'pos.category'
}


class ProductImportWizard(models.TransientModel):
    _name = 'product.import.wizard'
    _description = 'Product Import Wizard'

    file = fields.Binary('File', required=True)
    filename = fields.Char('Filename')

    def import_file(self):
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
            'employee': 'employee',
            'barcode': 'barcode',
            'default_code': 'default_code',
            'name': 'name',
            'uom_id': 'uom_id',
            'purchase_format_summary': 'purchase_format_summary',
            'minimum_purchase_format_qty': 'minimum_purchase_format_qty',
            'individual_minimum_purchase_qty': 'individual_minimum_purchase_qty',
            'is_white_brand': 'is_white_brand',
            'white_brand_name': 'white_brand_name',
            'x_origen': 'x_origen',
            'certification_name': 'certification_name',
            'is_manufacture': 'is_manufacture',
            'pos_cross_sale': 'pos_cross_sale',
            'web_cross_sales': 'web_cross_sales',
            'pos_promotional_product': 'pos_promotional_product',
            'web_promotional_product': 'web_promotional_product',
            'pos_fidelity': 'pos_fidelity',
            'web_fidelity': 'web_fidelity',
            'profit': 'profit',
            'x_studio_tipo': 'x_studio_tipo',
            'x_studio_estado': 'x_studio_estado',
            'x_studio_protein': 'x_studio_protein',
            'x_studio_gluten': 'x_studio_gluten',
            'x_studio_lactose': 'x_studio_lactose',
            'x_studio_sugar': 'x_studio_sugar',
            'x_studio_edamam': 'x_studio_edamam',
            'available_in_pos': 'available_in_pos',
            'x_studio_web': 'x_studio_web',
            'warehouse_letter': 'warehouse_letter',
            'warehouse_number': 'warehouse_number',
            'company_brand': 'company_brand',
            'reordering_min_qty': 'reordering_min_qty',
            'reordering_max_qty': 'reordering_max_qty',
            'requested_qty': 'requested_qty',
            'cross_sale_image_1': 'cross_sale_image_1',
            'cross_sale_image_2': 'cross_sale_image_2',
            'cross_sale_image_3': 'cross_sale_image_3',
            'image_1': 'image_1',
            'image_2': 'image_2',
            'image_3': 'image_3',
            'image_4': 'image_4',
            'categ_id': 'categ_id',
            'official_source_url_1': 'official_source_url_1',
            'a_beta_caroteno': 'a_beta_caroteno',
            'b1_tiamina': 'b1_tiamina',
            'b2_riboflamina': 'b2_riboflamina',
            'b3_niacina': 'b3_niacina',
            'b5_acido_pantotenico': 'b5_acido_pantotenico',
            'b6_piridoxina': 'b6_piridoxina',
            'b8_biotina': 'b8_biotina',
            'b9_acido_folico': 'b9_acido_folico',
            'b12_cobalaminas': 'b12_cobalaminas',
            'c_acido_ascorbico': 'c_acido_ascorbico',
            'x_field_d': 'x_field_d',
            'x_field_e': 'x_field_e',
            'x_field_k': 'x_field_k',
            'calcio': 'calcio',
            'cobre': 'cobre',
            'cromo': 'cromo',
            'fluor': 'fluor',
            'fosforo': 'fosforo',
            'hierro': 'hierro',
            'magnesio': 'magnesio',
            'potasio': 'potasio',
            'selenio': 'selenio',
            'yodo': 'yodo',
            'zinc': 'zinc',
            'energia': 'energia',
            'proteinas': 'proteinas',
            'fibra': 'fibra',
            'beneficios': 'beneficios',
            'beneficios_1': 'beneficios_1',
            'beneficios_2': 'beneficios_2',
            'beneficios_3': 'beneficios_3',
            'beneficios_4': 'beneficios_4',
            'beneficios_5': 'beneficios_5',
            'beneficios_6': 'beneficios_6',
            'beneficios_7': 'beneficios_7',
            'official_source_url_2': 'official_source_url_2',
            'x_studio_regla_precios_escalonados': 'x_studio_regla_precios_escalonados',
            'x_studio_english_name': 'x_studio_english_name',
            'x_studio_pos_name': 'x_studio_pos_name',
            'x_studio_requested': 'x_studio_requested'
        }

        def get_or_create_category(category_path):
            category_names = category_path.split('/')
            parent_category = None
            for category_name in category_names:
                category = self.env['product.category'].search([('name', '=', category_name), ('parent_id', '=', parent_category.id if parent_category else False)], limit=1)
                if not category:
                    category = self.env['product.category'].create({
                        'name': category_name,
                        'parent_id': parent_category.id if parent_category else False
                    })
                parent_category = category
            return parent_category.id

        def get_or_create_pos_categories(category_paths):
            category_ids = []
            for category_path in category_paths.split(','):
                category_names = category_path.strip().split('/')
                parent_category = None
                for category_name in category_names:
                    category = self.env['pos.category'].search([('name', '=', category_name), ('parent_id', '=', parent_category.id if parent_category else False)], limit=1)
                    if not category:
                        category = self.env['pos.category'].create({
                            'name': category_name,
                            'parent_id': parent_category.id if parent_category else False
                        })
                    parent_category = category
                category_ids.append(parent_category.id)
            return [(6, 0, category_ids)]

        def get_or_create_taxes(tax_names):
            tax_ids = []
            for tax_name in tax_names.split(','):
                tax_name = tax_name.strip()
                tax_rate = float(''.join(filter(str.isdigit, tax_name)))
                tax = self.env['account.tax'].search([('name', '=', tax_name)], limit=1)
                if not tax:
                    tax = self.env['account.tax'].create({
                        'name': tax_name,
                        'amount': tax_rate,
                        'type_tax_use': 'sale',
                    })
                tax_ids.append(tax.id)
            return [(6, 0, tax_ids)]

        # Map the columns to the fields and create/update products
        Product = self.env['product.template']
        for row_idx in range(1, sheet.nrows):
            values = {}
            for col_idx, header in enumerate(headers):
                field_name = header

                if field_name in ['employee_id', 'responsible_id']:
                    continue

                if field_name in ['barcode', 'default_code']:
                    val = sheet.cell_value(row_idx, col_idx)
                    if val:
                        values[field_name] = str(int(val))
                    else:
                        values[field_name] = ''

                elif field_name == 'uom_id':
                    val = sheet.cell_value(row_idx, col_idx)
                    values['uom_po_id'] = val
                    values['uom_id'] = val

                elif field_name == 'categ_id':
                    val = sheet.cell_value(row_idx, col_idx)
                    values[field_name] = get_or_create_category(val)

                elif field_name == 'detailed_type':
                    val = sheet.cell_value(row_idx, col_idx)
                    detailed_types = {
                        'Almacenable': 'product',
                        'Servicio': 'service',
                        'Consumible': 'consu',
                    }
                    values[field_name] = detailed_types[val]

                elif field_name == 'product_tag_ids':
                    val = sheet.cell_value(row_idx, col_idx)
                    if val:
                        tag = self.env['product.tag'].search([('name', '=', val)], limit=1)
                        if not tag:
                            tag = self.env['product.tag'].create({'name': val})
                        values[field_name] = [(6, 0, [tag.id])]

                elif field_name == 'taxes_id':
                    val = sheet.cell_value(row_idx, col_idx)
                    if val:
                        values[field_name] = get_or_create_taxes(val)

                elif field_name == 'supplier_taxes_id':
                    val = sheet.cell_value(row_idx, col_idx)
                    if val:
                        values[field_name] = get_or_create_taxes(val)

                elif field_name == 'pos_categ_ids':
                    val = sheet.cell_value(row_idx, col_idx)
                    values[field_name] = get_or_create_pos_categories(val)

                elif field_name in ['priority']:
                    val = sheet.cell_value(row_idx, col_idx)
                    if val == 'Normal':
                        values[field_name] = '0'
                    else:
                        values[field_name] = '1'
                else:
                    values[field_name] = sheet.cell_value(row_idx, col_idx)

            # Handle many2one and many2many fields if any
            for field, value in values.items():
                if field in ['uom_id', 'uom_po_id']:
                    uom_category = self.env['uom.category'].search([('name', '=', value)], limit=1)
                    if not uom_category:
                        uom_category = self.env['uom.category'].create({'name': value})
                    uom = self.env['uom.uom'].search([('name', '=', value)], limit=1)
                    if not uom:
                        uom = self.env['uom.uom'].create({'name': value, 'category_id': uom_category.id})
                    values[field] = uom.id

                # if field.endswith('_id') and isinstance(value, str):
                #     if field == 'uom_id':
                #         uom_category = self.env['uom.category'].search([('name', '=', value)], limit=1)
                #         if not uom_category:
                #             uom_category = self.env['uom.category'].create({'name': value})
                #         uom = self.env['uom.uom'].search([('name', '=', value)], limit=1)
                #         if not uom:
                #             uom = self.env['uom.uom'].create({'name': value, 'category_id': uom_category.id})
                #         values[field] = uom.id
                #
                #     else:
                #         related_model = relation_model_mapping[field]
                #         related_record = self.env[related_model].search([('name', '=', value)], limit=1)
                #         if not related_record:
                #             related_record = self.env[related_model].create({'name': value})
                #         values[field] = related_record.id
                #
                # elif field.endswith('_ids') and isinstance(value, str):
                #     related_model = relation_model_mapping[field]
                #     related_records = self.env[related_model].search(
                #         [('name', 'in', [v.strip() for v in value.split(',')])])
                #     if not related_records:
                #         related_records = self.env[related_model].create(
                #             [{'name': v.strip()} for v in value.split(',')])
                #     values[field] = [(6, 0, related_records.ids)]

            print(values)
            # Check if the product already exists
            product = Product.search([('default_code', '=', values.get('default_code'))], limit=1)
            if product:
                product.write(values)
            else:
                Product.create(values)

        return
        # return {
        #     'type': 'ir.actions.client',
        #     'tag': 'reload',
        # }
