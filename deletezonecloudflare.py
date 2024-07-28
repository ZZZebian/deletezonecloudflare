import requests

def get_zone_id(email, api_key, domain):
    url = f"https://api.cloudflare.com/client/v4/zones?name={domain}"
    headers = {
        "X-Auth-Email": email,
        "X-Auth-Key": api_key,
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    
    if data["success"]:
        zone_id = data["result"][0]["id"]
        return zone_id
    else:
        print(f"Error retrieving Zone ID: {data['errors']}")
        return None

def delete_zone(email, api_key, zone_id):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}"
    headers = {
        "X-Auth-Email": email,
        "X-Auth-Key": api_key,
        "Content-Type": "application/json"
    }
    response = requests.delete(url, headers=headers)
    data = response.json()
    
    if data["success"]:
        print("Zone deleted successfully.")
    else:
        print(f"Failed to delete the zone. Error message: {data['errors'][0]['message']}")

def main():
    email = input("Enter your Cloudflare email: ")
    api_key = input("Enter your Cloudflare API key: ")
    domain = input("Enter the domain name (e.g., domain.com): ")
    
    zone_id = get_zone_id(email, api_key, domain)
    
    if zone_id:
        print(f"Zone ID for {domain} is {zone_id}.")
        confirm = input("Do you want to delete this zone? (yes/no): ").strip().lower()
        
        if confirm == "yes":
            delete_zone(email, api_key, zone_id)
        else:
            print("Zone deletion cancelled.")

if __name__ == "__main__":
    main()
