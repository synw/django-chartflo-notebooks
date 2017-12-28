# -*- coding: utf-8 -*-


class Data():

    def index_years(self, cf, index):
        data = cf.split_("index")[index]
        data.rename("date", "Date")
        data.rename("value", "Value")
        data.dateindex("Date")
        data.rmean("1AS", index_col="Date")
        data.keep("Date", "Value")
        data.date("Date", precision="Y")
        return data


get = Data()
