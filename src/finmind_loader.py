import pandas as pd

from FinMind.data import DataLoader

class FinMindLoader:
    '''
    主要串接FinMind API
    - api_token: 從 FinMind 網站獲取 api 
    '''
    def __init__(self, api_token: str):
        self.api = DataLoader()
        self.api.login_by_token(api_token=api_token)
        # Later: try-except

    def get_income_statement(self, stock_id: str, start_date: str) -> pd.DataFrame:
        try:
            return self.api.taiwan_stock_financial_statement(
                stock_id=stock_id,
                start_date=start_date,
            )
        except Exception as e:
            raise RuntimeError(f"Failed to fetch income statement for {stock_id}: {e}")
    
    def get_balance_sheet(self, stock_id: str, start_date: str) -> pd.DataFrame:
        try:
            return self.api.taiwan_stock_balance_sheet(
                stock_id=stock_id,
                start_date=start_date,
            )
        except Exception as e:
            raise RuntimeError(f"Failed to fetch balance sheet for {stock_id}: {e}")

    def get_dividend(self, stock_id: str, start_date: str) -> pd.DataFrame:
        try:
            return self.api.taiwan_stock_dividend(
                stock_id=stock_id,
                start_date=start_date,
            )
        except Exception as e:
            raise RuntimeError(f"Failed to fetch stock dividend policy for {stock_id}: {e}")

    def get_monthly_revenue(self, stock_id: str, start_date: str) -> pd.DataFrame:
        try:
            return self.api.taiwan_stock_month_revenue(
                stock_id=stock_id,
                start_date=start_date,
            )
        except Exception as e:
            raise RuntimeError(f"Failed to fetch stock dividend policy for {stock_id}: {e}")