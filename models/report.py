from odoo import models, fields,api
from datetime import datetime
from datetime import date
DEBUG_TAG = date.today().strftime("%Y/%m/%d") #2022/12/25
class report(models.Model):
    _name="report"
    month_list = [(str(i), str(i)) for i in range(1,13)]
    month = fields.Selection(month_list,default=str(date.today().month),string="Tháng")

    year_list = [(str(i),str(i)) for i in range(datetime.now().year -5,datetime.now().year +5)]
    year = fields.Selection(year_list,default=str(date.today().year),string="Năm")

    update_day = fields.Date(string="Ngày lập",default=datetime.now(),readonly=True)
    @api.model
    def set_default_currency(self):
        return self.env['res.currency'].search([('name','=','VND')],limit=1)
    currency_id = fields.Many2one('res.currency', string='Đơn vị tiền tệ',default= set_default_currency,readonly=True)

    @api.depends('month','year')
    def name_cal(self):
        for r in self:
            r.name = "Báo cáo "+str(r.month)+"/"+str(r.year)
    name = fields.Char(string="Báo cáo tháng",store =True,compute='name_cal')


    @api.depends('month','year')
    def summary(self):
        # time  = self.month+"/"+self.year
        for r in self:
            borrow_record_of_month = self.env['borrow'].search([]).filtered(lambda borrow_record: (borrow_record.borrow_day.month==int(r.month))and(borrow_record.borrow_day.year==int(r.year)))
            r.number_borrow = len(borrow_record_of_month)
            r.renvenue = sum(borrow_record_of_month.mapped('total_price'))
            # r.number_borrow = self.env['borrow'].search([('borrow_month','=',time)],count=True)

    number_borrow = fields.Integer(string="Số lượt thuê sách trong tháng",store=True,compute="summary")
    renvenue = fields.Monetary(string="Tổng doanh thu",currency_field='currency_id',compute='summary',store = True)


    def update_report(self):
        self.summary()
        self.update_day = datetime.now()