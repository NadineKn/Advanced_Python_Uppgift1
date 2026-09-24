import pandas as pd
import pytest

from order_report.validation import validate_required_columns

from order_report.reporting import (
    create_overview,
    sales_by_category,
    sales_by_region,
)

def test_create_overview():
    data = pd.DataFrame(
        {
            "order_id": [1, 2, 3],
            "discounted_value": [100.0, 200.0, 50.0],
            "returned": [False, True, False],
        }
    )

    result = create_overview(data)

    assert result.loc[
        result["metric"] == "total_sales", "value"
    ].iloc[0] == 350.0

    assert result.loc[
        result["metric"] == "order_count", "value"
    ].iloc[0] == 3.0

    assert result.loc[
        result["metric"] == "return_count", "value"
    ].iloc[0] == 1.0


def test_validate_required_columns_raises_when_column_is_missing():
    data = pd.DataFrame(
        {
            "order_id": [1],
            "order_date": ["2025-01-01"],
        }
    )

    with pytest.raises(ValueError, match="Missing required columns"):
        validate_required_columns(data)


def test_sales_by_category():
    data = pd.DataFrame(
        {
            "order_id": [1, 2, 3],
            "product_category": ["Books", "Books", "Sports"],
            "discounted_value": [100.0, 150.0, 200.0],
            "returned": [False, True, False],
        }
    )

    result = sales_by_category(data)

    books = result[result["product_category"] == "Books"].iloc[0]

    assert books["order_count"] == 2
    assert books["total_sales"] == 250.0
    assert books["returns"] == 1
    assert books["return_rate"] == 0.5


def test_sales_by_region():
    data = pd.DataFrame(
        {
            "order_id": [1, 2, 3],
            "region": ["North", "North", "South"],
            "discounted_value": [100.0, 150.0, 200.0],
            "returned": [False, True, False],
        }
    )

    result = sales_by_region(data)

    north = result[result["region"] == "North"].iloc[0]

    assert north["order_count"] == 2
    assert north["total_sales"] == 250.0
    assert north["returns"] == 1
    assert north["return_rate"] == 0.5