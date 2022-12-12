from odoo import models, fields,api
from odoo.exceptions import ValidationError

class customer(models.Model):
    _name = "customer"
    
    name = fields.Char(string="Tên",required=True)
    image = fields.Image(string="Ảnh",max_width=128,max_height=128)
    birthday = fields.Datetime(string="Ngày sinh")
    cmt = fields.Char(string="Số CMT",required = True)
    address = fields.Text(string="Địa chỉ")
    expiredate=fields.Datetime(string=" Ngày hết hạn thẻ",required = True)

    id_borrows = fields.One2many("borrow","id_customer",string = "Các lần mượn sách")

    @api.constrains('cmt')
    def check_cmt_format(self):
        if not self.cmt.isdigit():
            raise ValidationError("Vui lòng chỉ nhập số") 

