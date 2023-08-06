import AndroMoney.andro_control

"""
parser = argparse.ArgumentParser(description='Input money diary')
parser.add_argument('start', metavar="start", type=str, help='start date of money diary input')
parser.add_argument('end', metavar="end", type=str, help='end date of money diary input')
args = parser.parse_args()
start_date = args.start
end_date = args.end
"""

start_date= "20230701"
end_date= "20230731"


def func(start_date, end_date):

    AndroMoney.andro_control.start_andro(start_date, end_date)


if __name__ == '__main__':
    func(start_date, end_date)