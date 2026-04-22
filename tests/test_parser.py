def test_hex_to_bytes():

    hex_str = "01 02 03"
    result = bytes.fromhex(hex_str)

    assert result == b'\x01\x02\x03'
