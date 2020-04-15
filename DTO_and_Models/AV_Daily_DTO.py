class DTO_Daily_Value:
    def __init__(self,date,**kargs):
        self._date = date
        self._open = kargs['1. open']
        self._high = kargs['2. high']
        self._low = kargs['3. low']
        self._close = kargs['4. close']
        self._volume = kargs['5. volume']

