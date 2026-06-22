import os
import json
import time
import csv
import requests
from datetime import datetime

API_KEY = "acd0425c5565a86f23a5711207dbcbf0a15e26a29c1c0c009dde115ed46e69e0"
DATA_FOLDER = "tracking_data"
RESULTS_FILE = f"{DATA_FOLDER}/rankings.json"
CSV_FILE = f"{DATA_FOLDER}/rankings.csv"

def print_header():
    print("\n" + "="*70)
    print("SERP RANK TRACKER - Track Your Client Keywords")
    print("="*70 + "\n")

def create_data_folder():
    os.makedirs(DATA_FOLDER, exist_ok=True)

def load_data():
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(RESULTS_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def search_keyword(keyword, domain, location="United States"):
    try:
        print(f"   Searching: {keyword}...", end=" ", flush=True)
        
        url = "https://serpapi.com/search"
        params = {
            "q": keyword,
            "location": location,
            "api_key": API_KEY,
            "num": 100
        }
        
        response = requests.get(url, params=params)
        results = response.json().get('organic_results', [])
        
        for idx, result in enumerate(results, 1):
            if domain.lower() in result.get('link', '').lower():
                print(f"RANK #{idx}")
                return idx, result['link']
        
        print(f"NOT RANKED")
        return None, None
    except Exception as e:
        print(f"ERROR: {str(e)[:50]}")
        return None, None

def main():
    print_header()
    create_data_folder()
    data = load_data()
    
    while True:
        print("\n" + "="*70)
        print("MAIN MENU")
        print("="*70)
        print("1. Add New Project")
        print("2. Track Rankings")
        print("3. View Rankings")
        print("4. Export to Excel")
        print("5. Delete Project")
        print("0. Exit")
        print("="*70)
        
        choice = input("Choose (0-5): ").strip()
        
        if choice == "1":
            print("\n" + "="*70)
            print("ADD PROJECT")
            print("="*70)
            
            name = input("Project name: ").strip()
            if not name or name in data:
                print("Invalid!")
                continue
            
            domain = input("Domain (e.g., example.com): ").strip()
            if not domain:
                print("Domain required!")
                continue
            
            keywords = []
            print("\nAdd keywords:")
            while True:
                kw = input(f"Keyword #{len(keywords)+1} (or ENTER to finish): ").strip()
                if not kw:
                    if keywords:
                        break
                    print("Add at least 1!")
                    continue
                keywords.append({"keyword": kw, "current_rank": None})
                print(f"   Added: {kw}")
            
            data[name] = {
                "domain": domain,
                "keywords": keywords,
                "created_at": datetime.now().isoformat()
            }
            save_data(data)
            print(f"\nProject created!")
        
        elif choice == "2":
            if not data:
                print("Add a project first!")
                continue
            
            print("\n" + "="*70)
            print("TRACK RANKINGS")
            print("="*70)
            print("\nProjects:")
            projects = list(data.keys())
            for i, p in enumerate(projects, 1):
                print(f"  {i}. {p}")
            
            try:
                idx = int(input("\nSelect (number): ")) - 1
                project_name = projects[idx]
            except:
                print("Invalid!")
                continue
            
            project = data[project_name]
            print(f"\nTracking: {project_name}")
            print(f"Domain: {project['domain']}\n")
            
            for kw_data in project["keywords"]:
                keyword = kw_data["keyword"]
                domain = project["domain"]
                rank, url = search_keyword(keyword, domain)
                kw_data["previous_rank"] = kw_data.get("current_rank")
                kw_data["current_rank"] = rank
                kw_data["url"] = url
                kw_data["timestamp"] = datetime.now().isoformat()
                time.sleep(1)
            
            save_data(data)
            print(f"\nDone!")
        
        elif choice == "3":
            if not data:
                print("No data!")
                continue
            
            print("\nProjects:")
            projects = list(data.keys())
            for i, p in enumerate(projects, 1):
                print(f"  {i}. {p}")
            
            try:
                idx = int(input("\nSelect (number): ")) - 1
                project_name = projects[idx]
            except:
                print("Invalid!")
                continue
            
            project = data[project_name]
            print(f"\n" + "="*70)
            print(f"Rankings: {project_name}")
            print("="*70)
            print(f"{'Keyword':<30} {'Rank':<12} {'Status':<20}")
            print("="*70)
            
            for kw in project["keywords"]:
                keyword = kw["keyword"][:29]
                rank = kw.get("current_rank", "?")
                
                if isinstance(rank, int):
                    if rank <= 10:
                        status = "TOP 10"
                    else:
                        status = "OTHER"
                else:
                    status = "NOT RANKED"
                
                rank_str = f"#{rank}" if isinstance(rank, int) else str(rank)
                print(f"{keyword:<30} {rank_str:<12} {status:<20}")
            
            print("="*70)
            input("\nPress ENTER...")
        
        elif choice == "4":
            if not data:
                print("No data!")
                continue
            
            with open(CSV_FILE, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Project', 'Keyword', 'Rank', 'Status'])
                
                for project_name, project in data.items():
                    for kw in project["keywords"]:
                        rank = kw.get("current_rank", "Not Ranked")
                        status = "TOP 10" if isinstance(rank, int) and rank <= 10 else "Other"
                        writer.writerow([project_name, kw["keyword"], rank, status])
            
            print(f"\nExported to: {CSV_FILE}")
            input("Press ENTER...")
        
        elif choice == "5":
            if not data:
                print("No projects!")
                continue
            
            print("\nProjects:")
            projects = list(data.keys())
            for i, p in enumerate(projects, 1):
                print(f"  {i}. {p}")
            
            try:
                idx = int(input("\nSelect to delete (number): ")) - 1
                project_name = projects[idx]
                confirm = input(f"Delete '{project_name}'? (yes/no): ").strip().lower()
                if confirm == "yes":
                    del data[project_name]
                    save_data(data)
                    print("Deleted!")
            except:
                print("Invalid!")
        
        elif choice == "0":
            print("\nGoodbye!")
            break
        
        else:
            print("Invalid!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nStopped!")
    except Exception as e:
        print(f"\nError: {e}")
