import sys
from stats import parse_record, warmest_city, average_by_city

def main():
    raw_lines = sys.stdin.read().splitlines()
    
    valid_records = []
    error_count = 0
    
    for line in raw_lines:
        if not line.strip():
            continue
            
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            error_count += 1
            
    parsed_count = len(valid_records)
    
    if parsed_count > 0:
        hottest = warmest_city(valid_records)
        avgs = average_by_city(valid_records)
        max_temp = avgs[hottest]
        
        print(parsed_count)
        print(error_count)
        print(f"{max_temp:.1f}")
    else:
        print(0)
        print(error_count)
        print("0.0")


if __name__ == "__main__":
    main()
