import pandas as pd

def extract_metadata(file_path):
    """
    Extract metadata from a CSV file.
    """
    df = pd.read_csv(file_path)
    metadata = {
        "row_count": len(df),
        "column_count": len(df.columns),
        "column_names": df.columns.tolist(),
    }
    return metadata
