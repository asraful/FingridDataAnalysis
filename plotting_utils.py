# plotting_utils.py (separate file)

import pandas as pd
import matplotlib.pyplot as plt

def combine_and_plot(datasets):
    """
    Combines data from multiple datasets into a pandas DataFrame and plots it.

    Args:
        datasets (list of dicts): A list of dictionaries, where each dictionary represents a dataset.
    """
    try:
        df = pd.DataFrame(datasets)
        df["startTime"] = pd.to_datetime(df["startTime"])
        df = df.sort_values(by="startTime")

        plt.figure(figsize=(10, 5))
        for dataset_id in df["datasetId"].unique():
            subset = df[df["datasetId"] == dataset_id]
            plt.plot(subset["startTime"], subset["value"], marker='o', linestyle='-', label=f"Dataset {dataset_id}")

        plt.xlabel("Time")
        plt.ylabel("MW")
        plt.title("Time Series Data Plot")
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid()
        plt.show()

    except KeyError as e:
        print(f"Key Error in plotting: {e}. Ensure 'startTime', 'datasetId', and 'value' keys are present.")
    except ValueError as e:
        print(f"Value Error in plotting: {e}. Check data types.")
    except Exception as e:
        print(f"Error during plotting: {e}")
