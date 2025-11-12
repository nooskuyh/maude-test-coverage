def print_report(data):
    """
    Prints a pretty-formatted report for Maude test results.

    Args:
        data: A list of lists, where each inner list has the format:
              [name, num_equations, pass_equations, num_rewrites, pass_rewrites]
    """
    headers = ["Name", "Equation", "Rewrite", "Pass"]
    processed_rows = []

    # --- 1. Process all data rows and gather totals ---
    total_num_eq = 0
    total_pass_eq = 0
    total_num_rw = 0
    total_pass_rw = 0

    if not data:
        print("No data to display.")
        return

    for row in data:
        num_eq, pass_eq, num_rw, pass_rw, name = row

        # Aggregate for the TOTAL row
        total_num_eq += num_eq
        total_pass_eq += pass_eq
        total_num_rw += num_rw
        total_pass_rw += pass_rw

        # --- Calculate derived strings for this row ---
        equation_str = f"{pass_eq}/{num_eq}"
        rewrite_str = f"{pass_rw}/{num_rw}"

        total_items = num_eq + num_rw
        total_passed = pass_eq + pass_rw

        pass_percent = 0.0
        # Avoid division by zero if a file has 0 items
        if total_items > 0:
            pass_percent = (total_passed / total_items) * 100

        pass_str = f"{pass_percent:.1f}%"

        processed_rows.append((name, equation_str, rewrite_str, pass_str))

    # --- 2. Calculate TOTAL row strings ---
    total_eq_str = f"{total_pass_eq}/{total_num_eq}"
    total_rw_str = f"{total_pass_rw}/{total_num_rw}"

    total_items_all = total_num_eq + total_num_rw
    total_passed_all = total_pass_eq + total_pass_rw

    overall_pass_percent = 0.0
    if total_items_all > 0:
        overall_pass_percent = (total_passed_all / total_items_all) * 100

    total_pass_str = f"{overall_pass_percent:.1f}%"
    total_row_processed = ("TOTAL", total_eq_str, total_rw_str, total_pass_str)

    # --- 3. Determine column widths dynamically ---
    # Initialize widths with header lengths
    name_w = len(headers[0])
    eq_w = len(headers[1])
    rw_w = len(headers[2])
    pass_w = len(headers[3])

    # Check data rows for max widths
    for name, eq, rw, p_pass in processed_rows:
        name_w = max(name_w, len(name))
        eq_w = max(eq_w, len(eq))
        rw_w = max(rw_w, len(rw))
        pass_w = max(pass_w, len(p_pass))

    # Check TOTAL row for max widths
    name_w = max(name_w, len(total_row_processed[0]))
    eq_w = max(eq_w, len(total_row_processed[1]))
    rw_w = max(rw_w, len(total_row_processed[2]))
    pass_w = max(pass_w, len(total_row_processed[3]))

    # --- 4. Print the formatted table ---
    padding = "   "  # 3 spaces between columns

    # Print Header
    header_line = (
        f"{headers[0]:<{name_w}}{padding}"
        f"{headers[1]:>{eq_w}}{padding}"
        f"{headers[2]:>{rw_w}}{padding}"
        f"{headers[3]:>{pass_w}}"
    )
    print(header_line)

    # Print Separator
    total_width = name_w + eq_w + rw_w + pass_w + (len(padding) * (len(headers) - 1))
    print("-" * total_width)

    # Print Data Rows
    for name, eq_str, rw_str, pass_str in processed_rows:
        row_line = (
            f"{name:<{name_w}}{padding}"
            f"{eq_str:>{eq_w}}{padding}"
            f"{rw_str:>{rw_w}}{padding}"
            f"{pass_str:>{pass_w}}"
        )
        print(row_line)

    # Print TOTAL row separator and data
    print("-" * total_width)
    total_line = (
        f"{total_row_processed[0]:<{name_w}}{padding}"
        f"{total_row_processed[1]:>{eq_w}}{padding}"
        f"{total_row_processed[2]:>{rw_w}}{padding}"
        f"{total_row_processed[3]:>{pass_w}}"
    )
    print(total_line)

# --- Example Usage ---
if __name__ == "__main__":
    # Your input data
    report_data = [
        # [name, num_eq, pass_eq, num_rw, pass_rw]
        ['Test.maude', 50, 45, 13, 12],
        ['Another-Long-Test-File.maude', 120, 110, 80, 80],
        ['Simple.maude', 10, 10, 5, 5],
        ['Failing.maude', 25, 15, 10, 2]
    ]

    # Call the function
    print_maude_report(report_data)