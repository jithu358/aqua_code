from django.contrib import admin

# Register your models here.
from .models import users
admin.site.register(users)

from .models import drivers
admin.site.register(drivers)

from .models import collab
admin.site.register(collab)

from .models import shop
admin.site.register(shop)

from .models import cart
admin.site.register(cart)

from .models import orders
admin.site.register(orders)

from .models import payments
admin.site.register(payments)

from .models import contact
admin.site.register(contact)

from .models import complaint
admin.site.register(complaint)

