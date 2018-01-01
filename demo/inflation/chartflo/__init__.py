# -*- coding: utf-8 -*-
from chartflo.apps import cf
from inflation.models import Measurement
from .charts import charts


def run(**kwargs):
    print("Running inflation generator ...")
    q = Measurement.objects.all()
    cf.load_django(q, dateindex="date")
    cf.report_path = "templates/dashboards/inflation"
    cf.rename("date", "Date")
    cf.rename("value", "Value")
    cf.backup()
    charts.make(cf)
