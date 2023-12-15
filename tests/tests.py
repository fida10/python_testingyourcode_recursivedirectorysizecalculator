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

    def test_single_file_in_folder(self):
        size = calculate_directory_size("test_folder_one_file")
        expected_size = 66
        assert size == expected_size
        
    def test_empty_folder(self):
        size = calculate_directory_size("test_empty_folder")
        #empty folders are not pushed by git
        #if running this, will need to create this folder in test directory manually
        expected_size = 0
        assert size == expected_size
    
    def test_folder_files_with_different_extensions(self):
        size = calculate_directory_size("test_files_of_different_types")
        # size with the auto created ds.store; this may not work on windows/linux
        expected_size = 245
        assert size == expected_size

    def test_directory_inside_a_directory(self):
        size = calculate_directory_size(
            "test_folder/other_file_two/other_file_three")
        # size with the auto created ds.store; this may not work on windows/linux
        expected_size = 46
        assert size == expected_size


if __name__ == '__main__':
    pytest.main()
