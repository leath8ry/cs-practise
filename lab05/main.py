import sys
from logstats import count_levels, top_errors, format_report

def main():
    input_line = sys.stdin.readline().strip()
    if not input_line:
        return
        
    filename = input_line

    with open(filename, encoding="utf-8") as f:
        levels_counts = count_levels(f)
        
    with open(filename, encoding="utf-8") as f:
        errors_list = top_errors(f, 3)
        
    total_parsed = sum(levels_counts.values())
    
    error_count = levels_counts.get("ERROR", 0)
    broken_count = levels_counts.get("BROKEN", 0)
    
    print(total_parsed)
    print(error_count)
    print(broken_count)
    
    
    report_text = format_report(levels_counts, errors_list)
    
    with open("report.txt", "w", encoding="utf-8") as out:
        out.write(report_text)


if __name__ == "__main__":
    main()
