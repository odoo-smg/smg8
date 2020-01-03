# -*- coding: utf-8 -*-

from odoo import fields, models, exceptions


class Smgproduct(models.Model):
    _inherit = 'product.template'
    _check_company_auto = True

    # Change description and set it as mandatory
    default_code = fields.Char(string="Product Code", required=True)

    # constraints to validate code and description to be unique
    _sql_constraints = [
        ('default_code_name_check_smg',
         'CHECK(name != default_code)',
         "The Name of the product should not be the product code"),

        ('default_code_unique_smg',
         'UNIQUE(default_code)',
         "The Product Code must be unique"),

        ('name_unique_smg',
         'UNIQUE(name)',
         "The Product name must be unique"),
    ]
