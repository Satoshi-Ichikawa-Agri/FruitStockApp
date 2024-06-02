import csv
import re
from datetime import datetime


datetime_pattern = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$")


def validate_datetime(datetime_str):
    if datetime_pattern.match(datetime_str):
        try:
            # datetimeに変換できるかチェック
            datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
            return True
        except ValueError:
            return False
    return False


def insert_sales_csv(file, sales_model, fruit_model):
    """CSV Insert処理"""
    decoded_file = file.read().decode("utf-8").splitlines()
    reader = csv.reader(decoded_file)

    # 手動でヘッダーを指定
    headers = ["fruit_name", "sales_volume", "total_price", "sales_date"]

    for row in reader:
        data = dict(zip(headers, row))
        # バリデーション
        try:
            fruit_name = data["fruit_name"]
            sales_volume = int(data["sales_volume"])
            total_price = int(data["total_price"])
            sales_date = data["sales_date"]

            if not validate_datetime(sales_date):
                raise ValueError(f"日付形式が正しくありません: {sales_date}")

            if not fruit_model.objects.filter(fruit_name=fruit_name).exists():
                raise ValueError(
                    f"{fruit_name} はFruitMasterModelに存在しません。"
                )

            fruit = fruit_model.objects.get(fruit_name=fruit_name)
            sales_model.objects.create(
                fruit_id=fruit.fruit_id,
                fruit_name=fruit_name,
                price=fruit.price,
                sales_volume=sales_volume,
                total_price=total_price,
                sales_date=sales_date,
            )
        except ValueError as e:
            # バリデーションに失敗した場合、その行をスキップ
            print(f"バリデーションエラー: {e}")
            continue
