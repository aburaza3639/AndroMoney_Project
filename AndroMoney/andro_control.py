from AndroMoney import andro_writer
from AndroMoney import andro_data


def start_andro(start_date, end_date):
    try:
        am = andro_data.AndroDataMoney(start_date = start_date, end_date = end_date)
        pivot_fx = am.andro_pivot_get_fx()
        df = am.andro_rawdata_get()
        andro_writer.andro_pivotwriter(pivot_fx, df)
        #andro_writer.andro_excelwriter(pivot_fx, start_date=start_date)
    except Exception as ex:
        print("{}".format(ex))