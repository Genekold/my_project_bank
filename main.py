from src.widget import card_account, data_view
from src.processing import sort_list_by_key

if __name__ == '__main__':
    print(card_account('Visa Gold 5999414228426353'))
    print(data_view('2018-07-11T02:26:18.671407'))
    print(sort_list_by_key([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
