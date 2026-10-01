from .reserva import Reserva
from .sala import Sala
from app.models.sala import Sala # 1
from app.models.reserva import Reserva# 2

__all__ = ["Sala", "Reserva"]
