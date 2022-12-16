from odoo import models, fields,api
from odoo.exceptions import ValidationError
def return_before_expiredate(borrow):
    try:
        return borrow.expiredate > borrow.give_back_day
    except:
        return False
class customer(models.Model):
    _name = "customer"
    
    name = fields.Char(string="Tên",required=True,help="Tên của độc giả",index=True)
    image = fields.Image(string="Ảnh",max_width=128,max_height=128)
    birthday = fields.Datetime(string="Ngày sinh")
    cmt = fields.Char(string="Số CMT",required = True)
    address = fields.Text(string="Địa chỉ")
    expiredate=fields.Datetime(string=" Ngày hết hạn thẻ",required = True)
    number_rented = fields.Integer(string="Tổng số lần đã mượn sách",compute='number_rented_cal')
    number_return_before_expiredate = fields.Integer(string="Tổng số lần trả sách đúng hạn",compute='number_return_before_expiredate_cal')
    borrow_ids = fields.One2many("borrow","id_customer",string = "Các lần mượn sách")

    @api.constrains('cmt')
    def check_cmt_format(self):
        if not self.cmt.isdigit():
            raise ValidationError("Vui lòng chỉ nhập số") 
    
    @api.depends('borrow_ids')
    def number_rented_cal(self):
        for customer_r in self:
            customer_r.number_rented = len(customer_r.borrow_ids)

    @api.depends('borrow_ids')
    def number_return_before_expiredate_cal(self):
        for customer_r in self:
            customer_r.number_return_before_expiredate = len(customer_r.borrow_ids.filtered(return_before_expiredate))
      

