"""
==============================================================
Day 10 Lab: Build Your First Automated ETL Pipeline
==============================================================
Student ID: AI20K-2A202600027  (<-- Thay XXXX bang ma so cua ban)
Name: Đặng Văn Minh

Nhiem vu:
   1. Extract:   Doc du lieu tu file JSON
   2. Validate:  Kiem tra & loai bo du lieu khong hop le
   3. Transform: Chuan hoa category + tinh gia giam 10%
   4. Load:      Luu ket qua ra file CSV

Cham diem tu dong:
   - Script phai chay KHONG LOI (20d)
   - Validation: loai record gia <= 0, category rong (10d)
   - Transform: discounted_price + category Title Case (10d)
   - Logging: in so record processed/dropped (10d)
   - Timestamp: them cot processed_at (10d)
==============================================================
"""

import json
import pandas as pd
import os
import datetime

# --- CONFIGURATION ---
SOURCE_FILE = 'raw_data.json'
OUTPUT_FILE = 'processed_data.csv'


def extract(file_path):
    """
    Task 1: Doc du lieu JSON tu file.

    Returns:
        list: Danh sach cac records (dictionaries)
    """
    print(f"Extracting data from {file_path}...")
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} does not exist.")
        
        with open(file_path, 'r') as f:
            data = json.load(f)
            if not isinstance(data, list):
                raise ValueError("JSON file must contain a list of records.")
        return data
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON. Ensure the file is properly formatted.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return []


def validate(data):
    """
    Task 2: Kiem tra chat luong du lieu.

    Returns:
        list: Danh sach cac records hop le
    """
    valid_records = []
    error_count = 0

    for record in data:
        try:
            price = record.get('price', 0)
            category = record.get('category', '').strip()

            if price <= 0 or not category:
                raise ValueError("Invalid record: price must be > 0 and category must not be empty.")

            valid_records.append(record)
        except ValueError as e:
            error_count += 1
            print(f"Validation error: {e} - Record: {record}")
        except Exception as e:
            error_count += 1
            print(f"Unexpected error during validation: {e} - Record: {record}")

    print(f"Validation complete. Valid: {len(valid_records)}, Errors: {error_count}")
    return valid_records


def transform(data):
    """
    Task 3: Ap dung business logic.

    Returns:
        pd.DataFrame: DataFrame da duoc transform
    """
    try:
        df = pd.DataFrame(data)

        if 'price' not in df.columns or 'category' not in df.columns:
            raise KeyError("Missing required columns 'price' or 'category' in data.")

        df['discounted_price'] = df['price'] * 0.9
        df['category'] = df['category'].str.title()
        df['processed_at'] = datetime.datetime.now().isoformat()

        return df
    except KeyError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error during transformation: {e}")
    return None


def load(df, output_path):
    """
    Task 4: Luu DataFrame ra file CSV.
    """
    try:
        df.to_csv(output_path, index=False)
        print(f"Data saved to {output_path}")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")


# ============================================================
# MAIN PIPELINE
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("ETL Pipeline Started...")
    print("=" * 50)

    # 1. Extract
    raw_data = extract(SOURCE_FILE)

    if raw_data:
        # 2. Validate
        clean_data = validate(raw_data)

        # 3. Transform
        final_df = transform(clean_data)

        # 4. Load
        if final_df is not None:
            load(final_df, OUTPUT_FILE)
            print(f"\nPipeline completed! {len(final_df)} records saved.")
        else:
            print("\nTransform returned None. Check your transform() function.")
    else:
        print("\nPipeline aborted: No data extracted.")
