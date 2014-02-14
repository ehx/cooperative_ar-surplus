from trytond.pool import Pool
from .partner import *
from .meeting import *
from .vacation import *
from .partnermeeting import *
from .sanction import *
from .surplus import *
from .partnersurplus import *


def register():
    Pool.register(Partner,
                  Meeting,
                  Vacation,
                  PartnerMeeting,
                  Sanction,
                  Surplus,
                  PartnerSurplus,
                  module='cooperative_ar', type_='model'
                  )
