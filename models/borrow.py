from odoo import models, fields,api

class borrow(models.Model):
    _name = "borrow"

    
    borrow_day = fields.Datetime(string="Ngày mượn",required=True)
    give_back_day = fields.Datetime(string="Ngày trả",required=True)
    expiredate = fields.Datetime(string="Ngày hết hạn",required=True)
    
    id_customer = fields.Many2one("customer",string = "khách hàng",required=True)
    customer_name = fields.Char(related='id_customer.name',string='Khách thuê')
    id_books = fields.Many2many("book")
    # id_books = fields.One2many("book","id_borrow")
    # id_books = fields.Many2one("book")
    @api.depends('id_customer.name','borrow_day')
    def create_name(self):
        # print("AnhDaiDo","create_name")
        self.name = self.id_customer.name+" "+str(self.borrow_day.date())

    name = fields.Char(compute = 'create_name',store=True,readonly=True)

    @api.depends('id_books')
    def total_price_cal(self):
        total_price = 0
        for book in self.id_books:
            total_price += book.rent_price
        self.total_price = total_price
    total_price = fields.Float(string="Tổng giá thuê",compute='total_price_cal',readonly=True,store = True)
