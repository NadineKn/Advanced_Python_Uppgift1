import logging

from order_report.config import Config
from order_report.loading import load_data
from order_report.processing import process_data
from order_report.reporting import (
    create_overview,
    sales_by_category,
    sales_by_region,
    returns_by_category,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)

logger = logging.getLogger(__name__)


def main() -> None:
    config = Config()
    config.output_path.mkdir(parents=True, exist_ok=True)
    
    data = load_data(config.input_path)

    logger.info("Läste in %s rader", len(data))

    data = process_data(data)

    overview = create_overview(data)

    overview.to_csv(
    config.output_path / "overview.csv",
    index=False,
    )

    category_report = sales_by_category(data)

    category_report.to_csv(
    config.output_path / "sales_by_category.csv",
    index=False,
    )

    region_report = sales_by_region(data)

    region_report.to_csv(
    config.output_path / "sales_by_region.csv",
    index=False,
)

    returns_report = returns_by_category(data)

    returns_report.to_csv(
    config.output_path / "returns_by_category.csv",
    index=False,
    )

if __name__ == "__main__":
    main()