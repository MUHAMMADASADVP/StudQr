import pytest
from project import validate,is_argument,BarcodeReaderImg

def test_validate():

    assert validate("20b051")== True
    assert validate("20b555")==False
    assert validate("207628") == False

def test_is_argument():

    assert is_argument("-f") == False
    assert is_argument("-v") == True
    assert is_argument("-man") == True

def test_BarcodeReaderImg():

    assert BarcodeReaderImg("img.jpeg") == '20b051'
    with pytest.raises(FileNotFoundError):
         BarcodeReaderImg("img1.jpeg") == '20b000'
