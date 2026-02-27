logs = ["INFO", "ERROR", "WARNING", "ERROR"]

# Count the number of errors in the logs
error_count = 0
for error in  logs:
    if error == "ERROR":
        error_count += 1
print("Number of errors in the logs:", error_count)