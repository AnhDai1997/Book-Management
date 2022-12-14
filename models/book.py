from odoo import models, fields,api
from odoo.exceptions import ValidationError
from datetime import date
DEBUG_TAG = date.today().strftime("%Y/%m/%d") #2022/12/25
class book(models.Model):
    _name = "book"
    
    name = fields.Char(string="Tên sách",required = True)
    author_name = fields.Char(string="Tên tác giả",required = True)
    publishing_company = fields.Char(string="Tên nhà xuất bản",required = True)
    publish_year = fields.Char(string="Năm xuất bản")
    
    book_type_list = [("khoahoc","Khoa Học"),("lichsu","Lịch sử"),("hoihoa","Hội hoạ"),("kithuat","Kĩ Thuật")]
    book_type = fields.Selection(book_type_list,default = book_type_list[0][0],required = True,string="Loại sách")

    
    rent_price = fields.Monetary(string="Giá thuê",required = True,currency_field='currency_id')

    # borrow_ids = fields.Many2one("borrow", string = "Mã sách")
    borrow_ids = fields.Many2many("borrow",string="Khách thuê")
    
    @api.depends('borrow_ids.book_ids')
    def rented_check(self):
        print(DEBUG_TAG,self.borrow_ids,type(self.borrow_ids),len(self.borrow_ids))
        for r in self:
            if not r.borrow_ids:
                r.rented = False
            else:
                r.rented = True
    rented = fields.Boolean(string="Đang cho thuê",default=False,compute='rented_check',store=True)

    @api.model
    def set_default_currency(self):
        return self.env['res.currency'].search([('name','=','VND')],limit=1)
    currency_id = fields.Many2one('res.currency', string='Đơn vị tiền tệ',default= set_default_currency,readonly=True)