# fingrid_api.py (separate file)

import urllib.request, json
from datetime import datetime, timedelta, timezone

def get_fingrid_data(api_key, dataset_id, start_time, end_time):
    """
    Fetches data from Fingrid's API for a given dataset and time range.

    Args:
        api_key (str): The API key for accessing the Fingrid API.
        dataset_id (int): The ID of the dataset to retrieve.
        start_time (datetime): The start time for the data retrieval.
        end_time (datetime): The end time for the data retrieval.

    Returns:
        list: A list of data dictionaries, or None if an error occurs.
    """
    try:
        url = f"https://data.fingrid.fi/api/datasets/{dataset_id}/data?startTime={start_time.isoformat()}Z&endTime={end_time.isoformat()}Z&format=json&locale=en"

        hdr = {
            'Cache-Control': 'no-cache',
            'x-api-key': api_key,
        }

        req = urllib.request.Request(url, headers=hdr)
        req.get_method = lambda: 'GET'
        response = urllib.request.urlopen(req)

        json_string = response.read()
        data_dict = json.loads(json_string.decode('utf-8'))
        dataset_data = data_dict.get("data", [])

        return dataset_data

    except urllib.error.HTTPError as e:
        print(f"HTTP Error for dataset {dataset_id}: {e.code} - {e.reason}")
        return None
    except urllib.error.URLError as e:
        print(f"URL Error for dataset {dataset_id}: {e.reason}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error for dataset {dataset_id}: {e}")
        return None
    except Exception as e:
        print(f"Unexpected Error for dataset {dataset_id}: {e}")
        return None