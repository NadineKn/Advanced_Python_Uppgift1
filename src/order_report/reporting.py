import pandas as pd


def create_overview(data: pd.DataFrame) -> pd.DataFrame:
    total_sales = round(data["discounted_value"].sum(), 2)
    number_of_orders = data["order_id"].nunique()
    number_of_returns = int(data["returned"].sum())

    overview = pd.DataFrame(
        {
            "metric": [
                "total_sales",
                "order_count",
                "return_count",
            ],
            "value": [
                total_sales,
                number_of_orders,
                number_of_returns,
            ],
        }
    )

    return overview


def sales_by_group(
    data: pd.DataFrame,
    group_column: str,
) -> pd.DataFrame:
    result = (
        data.groupby(
            group_column,
            as_index=False,
        )
        .agg(
            order_count=("order_id", "nunique"),
            total_sales=("discounted_value", "sum"),
            returns=("returned", "sum"),
        )
    )

    result["total_sales"] = result["total_sales"].round(2)

    result["return_rate"] = (
        result["returns"] / result["order_count"]
    ).round(3)

    result = (
        result
        .sort_values(
            "total_sales",
            ascending=False,
        )
        .reset_index(drop=True)
    )

    return result



def sales_by_category(data: pd.DataFrame) -> pd.DataFrame:
    return sales_by_group(data, "product_category")


def sales_by_region(data: pd.DataFrame) -> pd.DataFrame:
    return sales_by_group(data, "region")


def returns_by_category(data: pd.DataFrame) -> pd.DataFrame:
    result = (
        data.groupby(
            "product_category",
            as_index=False,
        )
        .agg(
            order_count=("order_id", "nunique"),
            returns=("returned", "sum"),
        )
    )

    result["return_rate"] = (
        result["returns"] / result["order_count"]
    ).round(3)

    result = (
        result
        .sort_values(
            "return_rate",
            ascending=False,
        )
        .reset_index(drop=True)
    )

    return result