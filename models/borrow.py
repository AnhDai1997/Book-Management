from odoo import models, fields,api
from datetime import datetime,date
from odoo.exceptions import ValidationError
class borrow(models.Model):
    _name = "borrow"

    
    borrow_day = fields.Datetime(string="Ngày mượn",required=True,default = datetime.now())
    

    is_give_back = fields.Boolean(string="Đã trả sách")
    expiredate = fields.Datetime(string="Ngày hết hạn",required=True)
    
    id_customer = fields.Many2one("customer",string = "khách hàng",required=True)
    customer_name = fields.Char(related='id_customer.name',string='Khách thuê')
    customer_cmt = fields.Char(related='id_customer.cmt',string='Số CMT')
    book_ids = fields.Many2many("book",domain="[('rented','=',False)]")

    @api.depends('id_customer.name','borrow_day')
    def create_name(self):
        # print("AnhDaiDo","create_name")
        for r in self:
            r.name = r.id_customer.name+" "+str(r.borrow_day.date())

    name = fields.Char(compute = 'create_name',store=True,readonly=True)
    @api.model
    def set_default_currency(self):
        return self.env['res.currency'].search([('name','=','VND')],limit=1)
    currency_id = fields.Many2one('res.currency', string='Đơn vị tiền tệ',default= set_default_currency,readonly=True)


    @api.depends('book_ids')
    def total_price_cal(self):
        for r in self:
            total_price = 0
            for book in r.book_ids:
                total_price += book.rent_price
            r.total_price = total_price
    total_price = fields.Monetary(string="Tổng giá thuê",currency_field='currency_id',compute='total_price_cal',store = True)

    @api.depends('is_give_back')
    def give_back_day_compute(self):
        for borrow_r in self:
            if borrow_r.is_give_back:
                borrow_r.give_back_day = datetime.now()
                for r in borrow_r.book_ids:
                    r.rented = False
            else:
                borrow_r.give_back_day = None
                for r in borrow_r.book_ids:
                    r.rented = True
    give_back_day = fields.Datetime(string="Ngày trả", compute="give_back_day_compute",store=True)

    @api.depends('borrow_day')
    def borrow_month_cal(self):
        for r in self:
            r.borrow_month = str(r.borrow_day.month)+"/"+str(r.borrow_day.year)
    borrow_month = fields.Char(readonly=True, compute='borrow_month_cal',store=True,group_operator = 'count')

    def give_back_btn(self):
        self.is_give_back = True

    @api.constrains('expiredate')
    def check_expiredate(self):
        if self.expiredate < self.borrow_day:
            raise ValidationError("Ngày hết hạn phải lớn hơn ngày mượn sách")

    @api.constrains('id_customer')
    def check_customer_expiredate(self):
        if self.id_customer.expiredate < datetime.today():
            raise ValidationError("Thẻ thành viên đã hết hạn")
        elif self.id_customer.expiredate < self.expiredate: # thẻ thành viên hết hạn trước ngày trả sách
            raise ValidationError("Thẻ thành viên hết hạn trước ngày trả sách")