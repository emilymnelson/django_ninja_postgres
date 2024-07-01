from ninja import NinjaAPI, Query
from .models import CME
from typing import List
import logging

api = NinjaAPI()


logger = logging.getLogger(__name__)

@api.get("/cme/")
def get_cme_data(request):
    data = CME.objects.all().values('year', 'specialty', 'hospital', 'credits')
    logger.debug(f"Retrieved data: {list(data)}")
    return list(data)

specific_records = CME.objects.filter(year=2003).values('year', 'specialty', 'hospital', 'credits')

@api.get("/cme/filter_by_year/")
def get_cme_data(request, year: int = Query(...)):
    filtered_data = CME.objects.filter(year=year).values('year', 'specialty', 'hospital', 'credits')
    return list(filtered_data)
