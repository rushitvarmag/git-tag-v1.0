import argparse
import sys
import requests
import json

def download_data(page):
    '''It downloads data from the FBI API '''
    url = f"https://api.fbi.gov/wanted/v1/list?page={page}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        sys.stderr.write(f"HTTP error occurred: {err}\n")
        return None
    except Exception as err:
        sys.stderr.write(f"Other error occurred: {err}\n")
        return None


def load_from_file(file_path):
    '''It loads data from the file'''
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as err:
        sys.stderr.write(f"Error reading file: {err}\n")
        return None



def parse_data(data):
    '''It parses the downloaded or loaded data'''
    results = []
    if "items" not in data:
        return results

    for item in data['items']:
        title = item.get('title', '')
        subjects = ','.join(item.get('subjects', []))
        field_offices = item.get('field_offices', [])
        
        if not isinstance(field_offices, list):
            field_offices = []  
        field_offices_str = ','.join(field_offices)
        results.append(f"{title}þ{subjects}þ{field_offices_str}")

    return results



def print_data(thorn_separated_data):
    '''prints the thorn_seperated_data'''
    for record in thorn_separated_data:
        print(record)


def main(page=None, file=None):
    '''It process the command line arguments'''
    data = None

    if page is not None:
        data = download_data(page)
    elif file is not None:
        data = load_from_file(file)

    if data:
        parsed_data = parse_data(data)
        print_data(parsed_data)
    else:
        sys.stderr.write("No data available or an error occurred.\n")


if __name__ == '__main__':
    '''Script start'''
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, required=False, help="Path to a JSON file.")
    parser.add_argument("--page", type=int, required=False, help="Page number from FBI API.")
     
    args = parser.parse_args()
    
    if args.page is not None:
        main(page=args.page)
    elif args.file is not None:
        main(file=args.file)
    else:
        parser.print_help(sys.stderr)
