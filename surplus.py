from trytond.model import ModelView, ModelSQL, fields
from trytond.pyson import Equal, Eval, Id
from trytond.transaction import Transaction
from trytond.pool import Pool

__all__ = ['Surplus']

class Surplus(ModelSQL, ModelView):
	"cooperative_ar"
	__name__ = "cooperative.surplus"
	date_surplus = fields.Date('Fecha de reparto')	
	cash = fields.Float('$')

	@classmethod
	def create(cls, values):
		id_surplus = super(Surplus, cls).create(values)
		Mod_Asociados = Pool().get('cooperative.partner')
		Psurplus = Pool().get('cooperative.partner.surplus')
		asociados = Mod_Asociados.search([('company', '=', 1),])
		for asociado in asociados:
			nombre = str(asociado.first_name + ' ' + asociado.last_name)
			valores = [
			{
				'id_surplus' : id_surplus[0].id,
			    'date_surplus': values[0]['date_surplus'], 
			    'partner': nombre ,
			    'cash': (float(asociado.proportional_gain) /100 * values[0]['cash']),
			    'proportional' : asociado.proportional_gain
			}]
			Psurplus.create(valores)
		return id_surplus