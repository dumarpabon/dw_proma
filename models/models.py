# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class dw_proma(models.Model):
#     _name = 'dw_proma.dw_proma'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class persona(models.Model):
    _name = 'dw_proma.persona'

    nombres = fields.Char(string="Nombres y Apellidos")
    documento = fields.Char(string="Documento de Identidad")
    rh = fields.Char(string="Grupo Sangineo")
    cargo = fields.Char(string="Cargo")
    celular = fields.Char(string="Celular")
    email = fields.Char(string="Correo")





class certificacion(models.Model):
    _name = 'dw_proma.certificacion'

    tipo_certificado = fields.Char(string="Tipo de Certificado")
    numero_certificado = fields.Char(string="Numero del Certificado")
    fecha_expedicion = fields.Date(string="Fecha de Expedicion")
    fecha_vencimiento = fields.Date(string="Fecha de Vencimiento")
    d = fecha_vencimiento.split('/')
    fecha_a_calcular = datetime.strptime(d[2] + d[1] + d[0],'%Y%m%d').date()
    calcdate = datetime.now().date() - fecha_a_calcular
    remanente = calcdate.days / 365
    archivo = fields.Char(string="Archivo")
    personal_id = fields.Many2one('dw_proma.empleado', string="Empleado")
    observaciones = fields.Text(string="Observaciones")
    vencimiento = fields.Boolean(string="Esta vencido?");

class aeronave(models.Model):
    _name = 'dw_proma.aeronave'

class helice(models.Model):
    _name = 'dw_proma.helice'

class motor(models.Model):
    _name = 'dw_proma.motor'

class alerta(models.Model):
    _name = 'dw_proma.alerta'
