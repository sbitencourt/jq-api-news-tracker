import json
import shutil
import sys
from pymongo.errors import PyMongoError
from init_db import get_db_client
from utils import get_raw_data_path, get_processed_data_path

RAW_FOLDER = get_raw_data_path()
PROCESSED_FOLDER = get_processed_data_path()

def ingest_data():

    # 1. Create the Client
    client = get_db_client()
    db = client['news_datalake'] 
    bronze_col = db['news_bronze']

    # 2. Iterate through the files (one by one)
    json_files = list(RAW_FOLDER.glob('*.json'))
    
    if not json_files:
        print("Nothing new file to process.")
        return

    print(f"Starting the ingestion of {len(json_files)} files...")

    for file_path in json_files:
        try:
            # A. Read the file
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                data_articles = data.get('articles')

            # Validation: Only insert if it is a list or it is not empty
            if isinstance(data_articles, list) and data_articles:
                # B. Insert in MongoDB (Batch)
                bronze_col.insert_many(data_articles)
                print(f"Inserted {len(data)} documents from file: {file_path.name}")
            else:
                print(f"Empty file or invalid format: {file_path.name}")

            # C. Move to Processed (Success)
            destination = PROCESSED_FOLDER / file_path.name
            shutil.move(str(file_path), str(destination))

        except json.JSONDecodeError:
            print(f"Error by decoding JSON: {file_path.name}. Corrupted file?")
        except PyMongoError as e:
            print(f"Database error while processing {file_path.name}: {e}")
        except Exception as e:
            print(f"Unexpected error in {file_path.name}: {e}")

    print("Ingestion process completed.")

if __name__ == "__main__":
    ingest_data()