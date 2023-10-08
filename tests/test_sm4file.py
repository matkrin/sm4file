import pytest
from datetime import datetime
from pathlib import Path

from sm4file import Sm4, RhkPageType, RhkLineType


testfiles_path = Path(__file__).parent / "test_files"

TEST_STM_10_CH = testfiles_path / "test_stm_10ch.SM4"
TEST_IV = testfiles_path / "test_iv.SM4"


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
