# -*- coding: utf-8 -*-
from django.template.defaultfilters import slugify
from .data import get
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

    def make(self, cf):
        cf2 = cf.clone_()
        gi = self.global_index_years(cf2)
        cf.restore()
        self.indexes_years(cf, gi)


charts = Chart()
