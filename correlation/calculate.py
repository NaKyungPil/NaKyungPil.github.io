import FinanceDataReader as fdr
import pandas as pd
import datetime


def correlation():
    _Samsung = '005930'
    _LG_energy = '373220'  
    _SKHi = '000660'
    _Samsung_bio='207940'
    _LG_chemical='051910'
    _Samsung_SDI='006400'
    _Samsung_W='005935'
    _Hyundai='005385'
    _KIA_Co = '000270'
    _Naver = '035420'  

    start_date = '2022-06-03'
    end_date = '2023-06-03'

    samsung = fdr.DataReader(_Samsung, start_date, end_date)
    lg_energy = fdr.DataReader(_LG_energy, start_date, end_date)
    skhi = fdr.DataReader(_SKHi, start_date, end_date)
    samsung_bio = fdr.DataReader(_Samsung_bio, start_date, end_date)
    lg_chemical = fdr.DataReader(_LG_chemical, start_date, end_date)
    samsung_sdi = fdr.DataReader(_Samsung_SDI, start_date, end_date)
    samsung_w = fdr.DataReader(_Samsung_W, start_date, end_date)
    hyundai = fdr.DataReader(_Hyundai, start_date, end_date)
    kia = fdr.DataReader(_KIA_Co, start_date, end_date)
    naver = fdr.DataReader(_Naver, start_date, end_date)
    
    samsung_close = samsung['Close']
    lg_energy_close = lg_energy['Close']
    skhi_close = skhi['Close']
    samsung_bio_close = samsung_bio['Close']
    lg_chemical_close = lg_chemical['Close']
    samsung_sdi_close = samsung_sdi['Close']
    samsung_w_close = samsung_w['Close']
    hyundai_close = hyundai['Close']
    kia_close = kia['Close']
    naver_close = naver['Close']
    
    print(naver_close.corr(samsung_w_close))
    return None

def sharp():
    _Samsung = '005930'
    _LG_energy = '373220'  
    _SKHi = '000660'
    _Samsung_bio='207940'
    _LG_chemical='051910'
    _Samsung_SDI='006400'
    _Samsung_W='005935'
    _Hyundai='005385'
    _KIA_Co = '000270'
    _Naver = '035420'  
    
    start_date = '2022-06-03'
    end_date = '2023-06-03'

    df = fdr.DataReader(_Naver, start_date, end_date)
    #print(df)
    df['Daily Returns'] = df['Close'].pct_change()
    years = df['Daily Returns'].mean() * 252

    no_risk = 0.03
    sharp_ratio = (years - no_risk) / (df['Daily Returns'].std() * 252 ** 0.5)

    print(sharp_ratio)
    

    return None


def main():
    #correlation()
    sharp()
    
    return None

if __name__ == "__main__":
    main()
    
    


