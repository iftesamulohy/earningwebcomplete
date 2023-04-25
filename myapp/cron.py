from datetime import date
import logging


from myapp.models import PackageOrder
logger = logging.getLogger(__name__)
def update():
    logger.info("cron job works")
    packages = PackageOrder.objects.all()
    for pack in packages:
        if date.today()>=pack.expire_date:
            pack.status = "Expired"
            pack.save()
    
