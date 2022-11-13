import pandas as pd
import numpy as np
import AndroMoney_Project.AndroMoney.andro_fx
import AndroMoney_Project.AndroMoney.settings


class AndroData(object):

    def __init__(self, xlsx_file=None, start_date=None, end_date=None):

        if not xlsx_file:
            self.xlsx_file = self.get_xlsx_file_path()
        self.start_date = start_date
        self.end_date = end_date

    @staticmethod
    def get_xlsx_file_path():

        xlsx_file_path = AndroMoney_Project.AndroMoney.settings.xlsx_FILE_PATH
        return xlsx_file_path


class AndroDataMoney(AndroData):

    def andro_rawdata_get(self):
        df = pd.read_excel(self.xlsx_file, index_col=0, header=1)
        # 条件にマッチしたIndexを取得
        drop_index = df.index[df['日付'] == 10100101]
        # 条件にマッチしたIndexを削除
        df = df.drop(drop_index)
        df['日付'] = pd.to_datetime(df['日付'].astype(str))
        return df

    def andro_data_get(self):
        df = self.andro_rawdata_get()
        df1 = df.query("@self.end_date>=日付>=@self.start_date")
        return df1

    def andro_pivot_get(self):
        lst = ['住居費', '食料品', '光熱費', '通信費', '保険', '年金', '日常生活', '医療関連', '教育関連', '交通関係',
               'アパレル', '人間関係', 'レジャー・娯楽', '電子製品・モバイル', '自動車・バイク', '奨学金', '仕送り', 'その他', 'Business Expense']
        pivot_andromoney = pd.pivot_table(self.andro_data_get(), index=['カテゴリ'], columns='通貨', values='金額',
                                          aggfunc=np.sum, fill_value=0)
        pivot_andromoney = pivot_andromoney.reindex(lst, axis='index', fill_value=0)
        return pivot_andromoney

    def andro_pivot_get_fx(self):
        pivot_andromoney = self.andro_pivot_get()
        fx = AndroMoney_Project.AndroMoney.andro_fx.return_fx(self.start_date, self.end_date)
        pivot_andromoney['sum'] = pivot_andromoney['HKD'] / fx[1] + pivot_andromoney['JPY'] / fx[0] + pivot_andromoney[
            'SGD']
        pivot_andromoney = pivot_andromoney.round(2)
        print(pivot_andromoney)
        return pivot_andromoney
