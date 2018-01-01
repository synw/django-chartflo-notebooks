# -*- coding: utf-8 -*-


class Data():

    def index_years(self, cf, index):
        cf.info("Getting data from index "+index)
        cf = cf.split_("index")[index]
        cf.rmean("1AS", index_col="Date")
        cf.keep("Date", "Value")
        cf.date("Date", precision="Y")
        return cf


get = Data()
