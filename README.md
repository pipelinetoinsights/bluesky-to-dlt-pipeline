# Bluesky-API-dlt-S3
this is a gitrepo for dlt series here :
for complete instruction please check the post 
## Prerequisites

This project requires the following:

- **Python 3.8 or higher**: Ensure Python is installed on your system.
- **pip package manager**: For dependency installation.
- **Virtual Environment**: It is highly recommended to use a virtual environment to manage dependencies effectively. Refer to the [dlt installation guide](https://dlthub.com/docs) for detailed instructions.
- **AWS S3 Setup**: Ensure your AWS account is configured with S3. Have your access key and secret key ready. For guidance, check the [AWS S3 Getting Started Guide](https://docs.aws.amazon.com/AmazonS3/latest/gsg/).

---

## Installation

### 1. Installing dlt

To get started, install the `dlt` library and its required extras for working with the Local Filesystem destination:

```bash
pip install "dlt[filesystem]"
pip install -r requirements.txt
pip install "dlt[parquet]"
```

---

## Running the Pipeline

Run the Bluesky pipeline using the following command:

```bash
python bluesky_posts_pipeline.py
```

---

## Orchestrating the dlt Pipeline with Dagster

If you want to orchestrate your pipeline using **Dagster**, follow these steps:

1. **Install Dagster**
   ```bash
   pip install dagster dagster-embedded-elt
   pip install -e "[dev]"
   ```

2. **Start the Dagster Development Server**
   ```bash
   dagster dev
   ```

You can now orchestrate and monitor your pipeline using Dagster's UI.

---


