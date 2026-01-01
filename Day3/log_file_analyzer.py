# Develop a log file analyzer that reads a text file line by line and counts occurrences of predefined keywords. 
# Generate a summary report of keyword frequencies and write the results to a new output file.

def file_analyzer():
    count = 0
    predefined_keywords = ["claim approved", "claim rejected", "claim pending", "invalid", "processed"]
    keyword_count = {}
    for word in predefined_keywords:
        keyword_count[word] = 0
    
    try:
        with open("Day3/data.txt", "r") as file:
            for line in file:
                line = line.lower()
                for word in predefined_keywords:
                    if word in line:
                        keyword_count[word] += 1
        
        with open("Day3/output.txt", "w") as output:
            output.write("Keyword Frequency Report \n")
            output.write("--------------------------\n")
            for word, count in keyword_count.items():
                output.write(f"{word.upper()}: {count}\n")

        print("Analysis Completed. Report written to output.txt")
                
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    file_analyzer()