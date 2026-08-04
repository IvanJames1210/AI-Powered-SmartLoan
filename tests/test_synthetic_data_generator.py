import random

from csv_processor import process_csv_applications
from synthetic_data_generator import (
    FIELDNAMES,
    create_synthetic_applications,
    save_synthetic_applications_to_csv,
)


def test_synthetic_applications_are_created():
    random.seed(1)

    applications = create_synthetic_applications(10)

    assert len(applications) == 10
    assert isinstance(applications, list)


def test_synthetic_applicant_has_required_fields():
    random.seed(1)

    applications = create_synthetic_applications(1)
    applicant = applications[0]

    for field in FIELDNAMES:
        assert field in applicant


def test_synthetic_csv_file_is_created(tmp_path):
    random.seed(1)

    file_path = tmp_path / "synthetic_test_applications.csv"

    total_created = save_synthetic_applications_to_csv(file_path, 10)

    assert total_created == 10
    assert file_path.exists()


def test_synthetic_csv_can_be_processed(tmp_path):
    random.seed(1)

    file_path = tmp_path / "synthetic_test_applications.csv"

    save_synthetic_applications_to_csv(file_path, 10)
    results = process_csv_applications(file_path)

    assert len(results) == 10
    assert results[0]["status"] == "processed"