import pytest
from src.ans import calculate_directory_size


class TestDirectorySizeCalculator:
    def test_calculate_directory_size(self):
        size = calculate_directory_size("test_folder")
        expected_size = 12579  # size with the auto created ds.store; this may not work on windows/linux
        assert size == expected_size

    def test_calculate_directory_size_nonexistent(self):
        with pytest.raises(FileNotFoundError):
            calculate_directory_size("nonexistent_dir")

# ADD additional test cases as part of this question!


if __name__ == '__main__':
    pytest.main()
