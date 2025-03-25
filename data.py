import requests
import pandas as pd

API_KEY = 'aa9ad9330ccf2262da567681d5ca1048'  

def get_fixtures():
    """Fetches past Premier League fixtures (Free plan only allows past matches)."""
    url = 'https://v3.football.api-sports.io/fixtures'
    params = {
        'league': 39,  
        'from': '2023-08-01',  
        'to': '2023-08-31'  
    }
    headers = {
        'x-apisports-key': 'aa9ad9330ccf2262da567681d5ca1048'
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        print("🔍 Full API Response:")
        print(data)

        if 'response' in data and data['response']:
            return data['response']
        else:
            print("❌ No fixtures data found in the API response.")
            return None

    except requests.RequestException as e:
        print(f"❌ Request failed: {e}")
        return None

def display_fixtures():
    """Fetches and displays past fixtures."""
    fixtures = get_fixtures()
    if fixtures is None:
        print("❌ No fixtures available.")
        return

    fixtures_data = []
    for match in fixtures:
        fixtures_data.append({
            'Date': match['fixture']['date'],
            'Home Team': match['teams']['home']['name'],
            'Away Team': match['teams']['away']['name'],
            'Venue': match['fixture']['venue']['name'],
            'City': match['fixture']['venue']['city']
        })

    df = pd.DataFrame(fixtures_data)
    
    print("\n📅 Past Premier League Fixtures:\n")
    print(df)

    df.to_csv('premier_league_fixtures.csv', index=False)
    print("\n📁 Fixtures saved to 'premier_league_fixtures.csv'.\n")

if __name__ == "__main__":
    display_fixtures()
