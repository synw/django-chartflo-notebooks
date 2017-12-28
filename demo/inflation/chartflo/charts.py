# -*- coding: utf-8 -*-
from slugify import slugify
from .data import get


class Chart():

    def global_index_years(self, data):
        data.title("Processing global index")
        data = get.index_years(data, index="Global index")
        data.chart("Date", "Value")
        data.opts(dict(tools=["hover"]))
        colors = dict(point="orange", line="green")
        data.opts(dict(tools=["hover"], legend_position="top_left"))
        data.size(10)
        data.width(1040)
        c = data.line_point_("Global index", colors=colors)
        data.stack("global_index", c)
        data.to_files("charts")

    def index_year(self, data, index, gi):
        data.subtitle("Processing index "+index)
        gi.chart("Date", "Value")
        gi.style(dict(line_dash="dashed"))
        gi.color("grey")
        c = gi.line_("Global index")
        data = get.index_years(data, index=index)
        data.chart("Date", "Value")
        data.style(dict(line_dash=""))
        data.size(10)
        data.opts(dict(legend_position="top_left"))
        colors = dict(line="green", point="orange")
        c2 = data.line_point_(index, colors=colors)
        return c*c2

    def indexes_years(self, data):
        indexes = list(data.unique_("index").df["index"])
        gi = get.index_years(data, indexes[0])
        data.title("Processing indexes "+", ".join(indexes))
        for index in indexes:
            c = self.index_year(data, index, gi)
            data.stack(slugify(index), c)
            data.to_files("charts/indexes")

    def make(self, cf):
        # self.global_index_years(cf)
        self.indexes_years(cf)


charts = Chart()
