from django.contrib import admin
from .models import Turista
from .models import Vuelo
from .models import Hotel
from .models import Sucursal
# Register your models here.
admin.site.register(Turista)
admin.site.register(Vuelo)
admin.site.register(Sucursal)
admin.site.register(Hotel)
