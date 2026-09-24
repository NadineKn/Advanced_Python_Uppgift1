from pathlib import Path

import pandas as pd

from order_report.validation import validate_required_columns



def load_data(input_path: Path) -> pd.DataFrame:
    try:
        data = pd.read_csv(input_path)
    except FileNotFoundError as error:
        raise FileNotFoundError(
            f"Kunde inte hitta datafilen: {input_path}"
        ) from error

    return validate_required_columns(data)