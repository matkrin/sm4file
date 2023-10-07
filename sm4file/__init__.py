from dataclasses import dataclass
from pathlib import Path
from typing import List
from datetime import datetime

import numpy as np
from numpy._typing import NDArray

from sm4file.page_types import StringData

from .sm4file import (
    Sm4File,
    RhkPageType,
    RhkLineType,
    RhkImageType,
    RhkScanType,
    Sm4PageHeaderDefault,
)


@dataclass()
class Sm4Channel:
    page_type: RhkPageType
    line_type: RhkLineType
    datetime: datetime
    xres: int
    yres: int
    image_type: RhkImageType
    scan_type: RhkScanType
    xsize: float
    ysize: float
    z_scale: float
    x_offset: float
    y_offset: float
    z_offset: float
    period: float
    bias: float
    current: float
    angle: float
    data: NDArray[np.float32]


class Sm4:
    def __init__(self, filepath: str):
        sm4file = Sm4File(filepath)
        self.prm_str = sm4file.file_header.prm.prm_data
        self.channels: List[Sm4Channel] = []
        for ch in sm4file.pages:
            if isinstance(ch.header, Sm4PageHeaderDefault):
                ch_datetime = None
                for i in ch.header.additional_page_objects:
                    if type(i) == StringData:
                        month, day, year = i.date.split("/")
                        year = "20" + year
                        month, day, year = int(month), int(day), int(year)
                        hour, min, sec = [int(x) for x in i.time.split(":")]
                        ch_datetime = datetime(year, month, day, hour, min, sec)

                # fallback to file stats
                if ch_datetime is None:
                        file_datetime = Path(filepath).stat().st_ctime
                        ch_datetime = datetime.fromtimestamp(file_datetime)

                self.channels.append(
                    Sm4Channel(
                        page_type=ch.header.page_type,
                        line_type=ch.header.line_type,
                        datetime=ch_datetime,
                        xres=ch.header.x_size,
                        yres=ch.header.y_size,
                        image_type=ch.header.image_type,
                        scan_type=ch.header.scan_type,
                        xsize=ch.header.x_scale * ch.header.x_size,
                        ysize=ch.header.y_scale * ch.header.y_size,
                        z_scale=ch.header.z_scale,
                        x_offset=ch.header.x_offset,
                        y_offset=ch.header.y_offset,
                        z_offset=ch.header.z_offset,
                        period=ch.header.period,
                        bias=ch.header.bias,
                        current=ch.header.current,
                        angle=ch.header.angle,
                        data=ch.data.data,
                    )
                )

    def __repr__(self):
        return repr(self.channels)

    def __getitem__(self, idx: int) -> Sm4Channel:
        return self.channels[idx]

    def __setitem__(self, idx: int, item: Sm4Channel) -> None:
        self.channels[idx] = item

    def __delitem__(self, idx: int) -> None:
        del self.channels[idx]

    def save_prm(self, out_file) -> None:
        with open(out_file, "w") as f:
            f.write(self.prm_str)

    def topography_channels(self) -> List[Sm4Channel]:
        return [ch for ch in self if ch.page_type == RhkPageType.RHK_PAGE_TOPOGRAPHIC]

    def current_channels(self) -> List[Sm4Channel]:
        return [ch for ch in self if ch.page_type == RhkPageType.RHK_PAGE_CURRENT]

