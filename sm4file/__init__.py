from dataclasses import dataclass
from typing import List

import numpy as np
from numpy._typing import NDArray

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
        self.channels: List[Sm4Channel] = []
        for ch in sm4file.pages:
            if isinstance(ch.header, Sm4PageHeaderDefault):
                self.channels.append(
                    Sm4Channel(
                        page_type=ch.header.page_type,
                        line_type=ch.header.line_type,
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
