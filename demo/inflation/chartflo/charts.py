# -*- coding: utf-8 -*-
from django.template.defaultfilters import slugify
from .data import get
from .layouts import layout_year
from .sequence import seq


class Chart():

    def global_index_years(self, cf):
        cf.title("Processing global index")
        index = "Global index"
        gi = get.index_years(cf, index=index)
        gi.chart("Date", "Value")
        gi.opts(dict(tools=["hover"]))
        colors = dict(point="orange", line="green")
        gi.opts(dict(tools=["hover"]))
        gi.size(10)
        gi.width(1040)
        c = gi.line_point_(colors=colors)
        gi.stack("global_index", c)
        gi.to_files("charts")
        # generate the sequence with the data
        seq.process(index, gi)
        return gi

    def index_year(self, cf, index, gi):
        cf.subtitle("Processing index "+index)
        gi.chart("Date", "Value")
        gi.style(dict(line_dash="dashed"))
        gi.color("grey")
        c = gi.line_("Global index")
        cf = get.index_years(cf, index=index)
        cf.chart("Date", "Value")
        cf.style(dict(line_dash=""))
        cf.size(10)
        cf.opts(dict(tools=["hover"], legend_position="top_left"))
        colors = dict(line="green", point="orange")
        c2 = cf.line_point_(index, colors=colors)
        # generate the sequence with the data
        seq.process(index, cf)
        return c*c2

    def indexes_years(self, cf, gi):
        indexes = list(cf.unique_("index").df["index"])
        indexes = indexes[1:]
        cf.title("Processing indexes "+", ".join(indexes))
        for index in indexes:
            c = self.index_year(cf, index, gi)
            cf.restore()
            cf.stack(slugify(index), c)
            cf.to_files("charts/indexes")

    def year_detail(self, cf):
        prevyear = 1996
        maxyear = 2016
        cf.title("Processing years details")
        while prevyear < maxyear:
            year = prevyear + 1
            cf.subtitle("Processing year "+str(year))
            y = cf.daterange_("Date", str(prevyear)+"-12-31",
                              "+", years=1)
            inds = y.split_("index")
            gi = inds["Global index"]
            inds.pop("Global index")
            # chart global index
            colors = dict(line="orange", point="green")
            gi.chart("Month", "Value")
            gi.width(1040)
            gi.height(350)
            gi.opts(dict(xrotation=0))
            c = gi.line_point_(colors=colors)
            cf.stack("global-index", c)
            cf.to_files("charts/years/"+str(year))
            # generate diff sequence for the year
            seq.year(year, gi)
            # chart other index
            layout_year(year, inds)
            prevyear += 1

    def index_home(self, cf):
        cf.title("Generating index for home")
        inds = cf.split_("index")
        inds.pop("Global index")
        charts = []
        for index in inds:
            cf.subtitle("Generating index "+index)
            ind = inds[index]
            ind.dateindex("Date")
            ind.chart("Date", "Value")
            ind.rmean("1AS", index_col="Date")
            ind.date("Date", precision="Y")
            ind.color(cf.color_())
            ind.opts(dict(xrotation=45))
            ind.width(500)
            ind.height(250)
            c = ind.line_(index)
            charts.append(c)
        c = cf.layout_(charts, cols=2)
        cf.stack("index_home", c)
        cf.to_files()

    def make(self, cf):
        cf2 = cf.clone_()
        gi = self.global_index_years(cf2)
        cf.restore()
        self.index_home(cf)
        self.indexes_years(cf, gi)
        self.year_detail(cf)


charts = Chart()
