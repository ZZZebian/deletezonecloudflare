# deletezonecloudflare
A Python script to manage Cloudflare zones. The script allows users to retrieve the Zone ID for a specified domain and delete the zone if needed.

## Features

- Retrieve Zone ID for a specified domain.
- Delete a zone after confirmation.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ZZZebian/deletezonecloudflare.git
    cd deletezonecloudflare
    ```

2. Install the required Python library:
    ```bash
    pip install requests
    ```

## Usage

1. Run the script:
    ```bash
    python deletezonecloudflare.py
    ```

2. Follow the prompts to enter your Cloudflare email, API key, and domain name.

3. The script will retrieve the Zone ID for the specified domain and ask for confirmation before deleting the zone.

## Example

```bash
Enter your Cloudflare email: your-email@example.com
Enter your Cloudflare API key: your-api-key
Enter the domain name (e.g., domain.com): domain.com
Zone ID for domain.com is xxxxxxxxxxxxxxxxxxxxxxx.
Do you want to delete this zone? (yes/no): yes
Zone deleted successfully.

