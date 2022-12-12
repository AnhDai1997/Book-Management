from odoo import models, fields,api
from odoo.exceptions import ValidationError
class book(models.Model):
    _name = "book"
    
    name = fields.Char(string="Tên sách",required = True)
    author_name = fields.Char(string="Tên tác giả",required = True)
    publishing_company = fields.Char(string="Tên nhà xuất bản",required = True)
    publish_year = fields.Char(string="Năm xuất bản")
    
    book_type_list = [("khoahoc","Khoa Học"),("lichsu","Lịch sử"),("hoihoa","Hội hoạ"),("kithuat","Kĩ Thuật")]
    book_type = fields.Selection(book_type_list,default = book_type_list[0][0],required = True,string="Loại sách")

    currency_id = fields.Many2one('res.currency', string='Currency')
    rent_price = fields.Monetary(string="Giá thuê",required = True,currency_field='currency_id')

    id_borrow = fields.Many2one("borrow", string = "Mã sách")
    # id_borrow = fields.One2many("borrow","id_books")
    
    @api.depends('id_borrow.id_books')
    def rented_check(self):
        print("AnhDaiDo",self.id_borrow.id_books,type(self.id_borrow.id_books))
        if self.id_borrow.id_books:
            self.rented = True
        else:
            self.rented = False

    rented = fields.Boolean(string="Đã thuê",readonly = True,default=False,compute='rented_check',store=True)
