# Bluesky-to-S3-dlt-pipeline

A Python-based pipeline project designed to fetch data from the Bluesky API and load it into an S3 bucket. This repository includes two implementations: a manual DLT pipeline and a Dagster-managed pipeline.

**This tutorial is prepared by [Pipeline To Insights](https://pipeline2insights.substack.com/), a platform dedicated to sharing data engineering knowledge, tutorials, and insights.**

## Directory Structure

### 1. Manual DLT Pipeline
This directory contains the manual implementation of the pipeline using DLT.

- **`.dlt/`**: Includes `config.toml`.
- **`bluesky_posts_pipeline.py`**: The main pipeline script to be executed. 
- **`requirements.txt`**: Contains the required dependencies.
- **`rest_api_pipeline.py`**: Example code generated by dlt for REST API integration.

### 2. Dagster Pipeline
This directory includes the implementation of the pipeline using Dagster for orchestration.

- **`.dlt/`**: Includes `config.toml`.
- **`bluesky_posts/`**
  Contains Dagster-related scripts:
  - **`assets.py`**: Defines assets and the pipeline for Dagster.
  - **`bluesky_posts_dagster_pipeline.py`**: Includes the DLT source definition.
  - **`definitions.py`**: Dagster configuration and pipeline definitions

## **How to Use**

### **Prerequisites**
1. Install Python 3.8 or higher on your machine.
2. Set up an S3 bucket and obtain the necessary credentials:
   - AWS Access Key ID
   - AWS Secret Access Key
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
### **Running the Manual dlt Pipeline**
1. Navigate to the **`bluesky_api_pipeline/`** directory
2. Create `secrets.toml` file in the `.dlt/` directory and add your S3 credentials:
```toml
  [destination.filesystem]
  bucket_url = "s3:[Bucket_name]" 

  [destination.filesystem.credentials]
  aws_access_key_id = "Access_key_id"
  aws_secret_access_key = "Secret_access_key"```
```
3. Run the pipeline scripts:
```bash
python bluesky_posts_pipeline.py
```
4. Check your S3 bucket to confirm that the data has been successfully ingested.

### **Running the Dagster dlt Pipeline**
For detailed steps to run the Dagster pipeline, refer to the README.md file located in the dagster_bluesky_posts/bluesky_posts directory.