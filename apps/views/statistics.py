from datetime import datetime, timedelta
from collections import defaultdict

from django.utils.timezone import make_aware


def statistics_summary(sales):
    """販売Summary処理"""
    # 集計用データ構造の初期化
    statistics = {
        "total_sales": 0,
        "monthly_sales": defaultdict(
            lambda: {
                "total": 0,
                "details": defaultdict(lambda: {"volume": 0, "amount": 0}),
            }
        ),
        "daily_sales": defaultdict(
            lambda: {
                "total": 0,
                "details": defaultdict(lambda: {"volume": 0, "amount": 0}),
            }
        ),
    }

    # 現在の日付
    now = datetime.now()

    # 過去3ヶ月と3日の日付範囲
    past_3_months = make_aware(now - timedelta(days=90))
    past_3_days = make_aware(now - timedelta(days=3))

    # 集計処理
    for sale in sales:
        statistics["total_sales"] += sale.total_price

        # 月別集計
        if sale.sales_date >= past_3_months:
            month_key = sale.sales_date.strftime("%Y/%m")
            statistics["monthly_sales"][month_key]["total"] += sale.total_price
            statistics["monthly_sales"][month_key]["details"][sale.fruit_name][
                "volume"
            ] += sale.sales_volume
            statistics["monthly_sales"][month_key]["details"][sale.fruit_name][
                "amount"
            ] += sale.total_price

        # 日別集計
        if sale.sales_date >= past_3_days:
            day_key = sale.sales_date.strftime("%Y/%m/%d")
            statistics["daily_sales"][day_key]["total"] += sale.total_price
            statistics["daily_sales"][day_key]["details"][sale.fruit_name][
                "volume"
            ] += sale.sales_volume
            statistics["daily_sales"][day_key]["details"][sale.fruit_name][
                "amount"
            ] += sale.total_price

    # テンプレート用に辞書をリストに変換
    monthly_sales_list = [
        {
            "month": month,
            "total": data["total"],
            "details": list(data["details"].items()),
        }
        for month, data in statistics["monthly_sales"].items()
    ]
    daily_sales_list = [
        {
            "day": day,
            "total": data["total"],
            "details": list(data["details"].items()),
        }
        for day, data in statistics["daily_sales"].items()
    ]

    context = {
        "statistics": {
            "total_sales": statistics["total_sales"],
            "monthly_sales": monthly_sales_list,
            "daily_sales": daily_sales_list,
        }
    }

    return context
