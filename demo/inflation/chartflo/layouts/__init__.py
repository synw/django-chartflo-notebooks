# -*- coding: utf-8 -*-
from django.template.defaultfilters import slugify


def layout_index(cf):
    cf.title("Building layouts")
    dss = cf.split_("index")
    years = list(range(1997, 2017))
    i = 1
    for indname in dss:
        charts = []
        cf.reports = []
        cf.subtitle("Building layout for index "+indname)
        for year in years:
            ds2 = dss[indname]
            ds2.report_path = cf.report_path
            ds3 = ds2.daterange_("Date", str(year)+"-01", "+", months=11)
            ds3.sort("Date")
            ds3.chart("Month", "Value")
            ds3.width(300)
            ds3.height(250)
            ds3.color("royalblue")
            ds3.opts(dict(xrotation=45))
            c = ds3.line_(str(year))
            charts.append(c)
        c = cf.layout_(charts)
        cf.stack(slugify(indname), c)
        cf.to_files("layouts_months")
        i += 1
