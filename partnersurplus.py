from trytond.model import ModelView, ModelSQL, fields

__all__ = ['PartnerSurplus']

class PartnerSurplus(ModelSQL , ModelView):
    "cooperative_ar"
    __name__ = "cooperative.partner.surplus"
    id_surplus = fields.Many2One('cooperative.surplus', 'id', ondelete="CASCADE")
    date_surplus = fields.Date('Fecha de reparto')	
    partner = fields.Char('Asociado')
    proportional = fields.Integer('Proporcional de ganancia')
    cash = fields.Float('Plata del reparto')