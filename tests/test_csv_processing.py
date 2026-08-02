from csv_processor import read_csv_applications, process_csv_applications


SAMPLE_CSV_FILE = "data/sample_applications.csv"


# Test 1: Check that CSV file can be read
def test_csv_file_can_be_read():
    rows = read_csv_applications(SAMPLE_CSV_FILE)

    assert len(rows) == 5
    assert rows[0]["row_number"] == 2


# Test 2: Check that batch processing returns all CSV rows
def test_csv_batch_processing_returns_all_rows():
    results = process_csv_applications(SAMPLE_CSV_FILE)

    assert len(results) == 5


# Test 3: Check that valid CSV rows are processed
def test_valid_csv_rows_are_processed():
    results = process_csv_applications(SAMPLE_CSV_FILE)

    assert results[0]["status"] == "processed"
    assert results[1]["status"] == "processed"
    assert results[0]["decision_result"]["decision"] == "Approved"


# Test 4: Check missing value detection
def test_csv_detects_missing_monthly_income():
    results = process_csv_applications(SAMPLE_CSV_FILE)

    assert results[2]["status"] == "validation_error"
    assert "monthly_income is missing" in results[2]["errors"]


# Test 5: Check unrealistic value detection
def test_csv_detects_unrealistic_age():
    results = process_csv_applications(SAMPLE_CSV_FILE)

    assert results[3]["status"] == "validation_error"
    assert "age must be between 18 and 100" in results[3]["errors"]


# Test 6: Check duplicate application detection
def test_csv_detects_duplicate_application():
    results = process_csv_applications(SAMPLE_CSV_FILE)

    assert results[4]["status"] == "validation_error"
    assert "duplicate application found" in results[4]["errors"]