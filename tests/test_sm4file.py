import pytest
from datetime import datetime
from pathlib import Path

from sm4file import Sm4, RhkPageType, RhkLineType
from sm4file.sm4_file import RhkImageType, RhkScanType


testfiles_path = Path(__file__).parent / "test_files"

TEST_STM_10_CH = testfiles_path / "test_stm_10ch.SM4"
TEST_IV = testfiles_path / "test_iv.SM4"
TEST_STM_4_CH = testfiles_path / "test_stm_4ch.SM4"


def test_stm_10ch():
    s = Sm4(str(TEST_STM_10_CH))
    assert len(s) == 10
    topo = s.topography_channels()
    assert len(topo) == 2
    curr = s.current_channels()
    assert len(curr) == 2
    for ch in s:
        assert round(ch.current * 1e10, 3) == 1.997
        assert round(ch.bias, 3) == -0.171
        assert round(ch.xsize * 1e9, 3) == 300.0
        assert round(ch.ysize * 1e9, 3) == 300.0
        assert ch.xres == 512
        assert ch.yres == 512
        assert round(ch.period, 4) == 0.0003
        assert ch.angle == 116.0
        assert ch.datetime == datetime(2020, 1, 8, 14, 13, 11)


def test_iv():
    s = Sm4(str(TEST_IV))
    print(s)
    assert len(s) == 5
    assert len(s.topography_channels()) == 0
    assert len(s.current_channels()) == 0
    for ch in s:
        assert ch.page_type == RhkPageType.RHK_PAGE_RAMP_SPECTROSCOPY_RP
        assert ch.line_type == RhkLineType.RHK_LINE_IV_SPECTRUM
        assert ch.datetime == datetime(2023, 6, 17, 11, 12, 42)
        assert ch.xres == 299
        assert ch.yres == 5
        assert ch.scan_type == RhkScanType.RHK_SCAN_RIGHT
        assert round(ch.period, 5) == 0.00250
        assert round(ch.bias, 5) == 0.99411
        assert round(ch.current * 1e11, 5) == 4.31244
        assert ch.angle == 0.0


def test_stm_4ch():
    s = Sm4(str(TEST_STM_4_CH))
    assert len(s) == 4
    topo = s.topography_channels()
    assert len(topo) == 2
    curr = s.current_channels()
    assert len(curr) == 2
    for i, ch in enumerate(s):
        print(s)
        assert ch.datetime == datetime(2023, 7, 18, 13, 30, 24)
        assert ch.xres == 512
        assert ch.yres == 512
        assert ch.image_type == RhkImageType.RHK_IMAGE_NORMAL
        if i % 2 == 0:
            assert ch.scan_type == RhkScanType.RHK_SCAN_RIGHT
        else:
            assert ch.scan_type == RhkScanType.RHK_SCAN_LEFT
        assert round(ch.xsize * 1e8) == 8
        assert round(ch.ysize * 1e8) == 8
        assert round(ch.period * 1e5, 4) == 9.7650
        assert round(ch.bias, 5) == 0.50808
        assert round(ch.current * 1e10, 5) == 9.96017
        assert ch.angle == 42.0
