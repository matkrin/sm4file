from __future__ import annotations
from typing import List, Union, TypeAlias
from io import BufferedReader
from dataclasses import dataclass, field
from enum import Enum

from .cursor import Cursor
from .page_types import (
    ApiInfo,
    ImageDriftHeader,
    ImageDriftData,
    PageData,
    SpecDriftData,
    SpecDriftHeader,
    StringData,
    TipTrackHeader,
    TipTrackData,
    PrmHeader,
    PiezoSensitivity,
    FrequencySweepData,
    ScanProcessorInfo,
    PllInfo,
    ChannelDriveInfo,
    LockinInfo,
    PiControllerInfo,
    LowpassFilterInfo,
)


PageObject: TypeAlias = Union[
    ApiInfo,
    ImageDriftHeader,
    ImageDriftData,
    PageData,
    SpecDriftData,
    SpecDriftHeader,
    StringData,
    TipTrackHeader,
    TipTrackData,
    PrmHeader,
    PiezoSensitivity,
    FrequencySweepData,
    ScanProcessorInfo,
    PllInfo,
    ChannelDriveInfo,
    LockinInfo,
    PiControllerInfo,
    LowpassFilterInfo,
]


class RhkPageDataType(Enum):
    RHK_DATA_IMAGE = 0
    RHK_DATA_LINE = 1
    RHK_DATA_XY_DATA = 2
    RHK_DATA_ANNOTATED_LINE = 3
    RHK_DATA_TEXT = 4
    RHK_DATA_ANNOTATED_TEXT = 5
    RHK_DATA_SEQUENTIAL = 6
    RHK_DATA_MOVIE = 7


class RhkObjectType(Enum):
    RHK_OBJECT_UNDEFINED = 0
    RHK_OBJECT_PAGE_INDEX_HEADER = 1
    RHK_OBJECT_PAGE_INDEX_ARRAY = 2
    RHK_OBJECT_PAGE_HEADER = 3
    RHK_OBJECT_PAGE_DATA = 4
    RHK_OBJECT_IMAGE_DRIFT_HEADER = 5
    RHK_OBJECT_IMAGE_DRIFT = 6
    RHK_OBJECT_SPEC_DRIFT_HEADER = 7
    RHK_OBJECT_SPEC_DRIFT_DATA = 8
    RHK_OBJECT_COLOR_INFO = 9
    RHK_OBJECT_STRING_DATA = 10
    RHK_OBJECT_TIP_TRACK_HEADER = 11
    RHK_OBJECT_TIP_TRACK_DATA = 12
    RHK_OBJECT_PRM = 13
    RHK_OBJECT_THUMBNAIL = 14
    RHK_OBJECT_PRM_HEADER = 15
    RHK_OBJECT_THUMBNAIL_HEADER = 16
    RHK_OBJECT_API_INFO = 17
    RHK_OBJECT_HISTORY_INFO = 18
    RHK_OBJECT_PIEZO_SENSITIVITY = 19
    RHK_OBJECT_FREQUENCY_SWEEP_DATA = 20
    RHK_OBJECT_SCAN_PROCESSOR_INFO = 21
    RHK_OBJECT_PLL_INFO = 22
    RHK_OBJECT_CH1_DRIVE_INFO = 23
    RHK_OBJECT_CH2_DRIVE_INFO = 24
    RHK_OBJECT_LOCKIN0_INFO = 25
    RHK_OBJECT_LOCKIN1_INFO = 26
    RHK_OBJECT_ZPI_INFO = 27
    RHK_OBJECT_KPI_INFO = 28
    RHK_OBJECT_AUX_PI_INFO = 29
    RHK_OBJECT_LOWPASS_FILTER0_INFO = 30
    RHK_OBJECT_LOWPASS_FILTER1_INFO = 31


class RhkPageSourceType(Enum):
    RHK_SOURCE_RAW = 0
    RHK_SOURCE_PROCESSED = 1
    RHK_SOURCE_CALCULATED = 2
    RHK_SOURCE_IMPORTED = 3


class RhkPageType(Enum):
    RHK_PAGE_UNDEFINED = 0
    RHK_PAGE_TOPOGRAPHIC = 1
    RHK_PAGE_CURRENT = 2
    RHK_PAGE_AUX = 3
    RHK_PAGE_FORCE = 4
    RHK_PAGE_SIGNAL = 5
    RHK_PAGE_FFT_TRANSFORM = 6
    RHK_PAGE_NOISE_POWER_SPECTRUM = 7
    RHK_PAGE_LINE_TEST = 8
    RHK_PAGE_OSCILLOSCOPE = 9
    RHK_PAGE_IV_SPECTRA = 10
    RHK_PAGE_IV_4x4 = 11
    RHK_PAGE_IV_8x8 = 12
    RHK_PAGE_IV_16x16 = 13
    RHK_PAGE_IV_32x32 = 14
    RHK_PAGE_IV_CENTER = 15
    RHK_PAGE_INTERACTIVE_SPECTRA = 16
    RHK_PAGE_AUTOCORRELATION = 17
    RHK_PAGE_IZ_SPECTRA = 18
    RHK_PAGE_4_GAIN_TOPOGRAPHY = 19
    RHK_PAGE_8_GAIN_TOPOGRAPHY = 20
    RHK_PAGE_4_GAIN_CURRENT = 21
    RHK_PAGE_8_GAIN_CURRENT = 22
    RHK_PAGE_IV_64x64 = 23
    RHK_PAGE_AUTOCORRELATION_SPECTRUM = 24
    RHK_PAGE_COUNTER = 25
    RHK_PAGE_MULTICHANNEL_ANALYSER = 26
    RHK_PAGE_AFM_100 = 27
    RHK_PAGE_CITS = 28
    RHK_PAGE_GPIB = 29
    RHK_PAGE_VIDEO_CHANNEL = 30
    RHK_PAGE_IMAGE_OUT_SPECTRA = 31
    RHK_PAGE_I_DATALOG = 32
    RHK_PAGE_I_ECSET = 33
    RHK_PAGE_I_ECDATA = 34
    RHK_PAGE_I_DSP_AD = 35
    RHK_PAGE_DISCRETE_SPECTROSCOPY_PP = 36
    RHK_PAGE_IMAGE_DISCRETE_SPECTROSCOPY = 37
    RHK_PAGE_RAMP_SPECTROSCOPY_RP = 38
    RHK_PAGE_DISCRETE_SPECTROSCOPY_RP = 39


class RhkLineType(Enum):
    RHK_LINE_NOT_A_LINE = 0
    RHK_LINE_HISTOGRAM = 1
    RHK_LINE_CROSS_SECTION = 2
    RHK_LINE_LINE_TEST = 3
    RHK_LINE_OSCILLOSCOPE = 4
    RHK_LINE_RESERVED = 5
    RHK_LINE_NOISE_POWER_SPECTRUM = 6
    RHK_LINE_IV_SPECTRUM = 7
    RHK_LINE_IZ_SPECTRUM = 8
    RHK_LINE_IMAGE_X_AVERAGE = 9
    RHK_LINE_IMAGE_Y_AVERAGE = 10
    RHK_LINE_NOISE_AUTOCORRELATION_SPECTRUM = 11
    RHK_LINE_MULTICHANNEL_ANALYSER_DATA = 12
    RHK_LINE_RENORMALIZED_IV = 13
    RHK_LINE_IMAGE_HISTOGRAM_SPECTRA = 14
    RHK_LINE_IMAGE_CROSS_SECTION = 15
    RHK_LINE_IMAGE_AVERAGE = 16
    RHK_LINE_IMAGE_CROSS_SECTION_G = 17
    RHK_LINE_IMAGE_OUT_SPECTRA = 18
    RHK_LINE_DATALOG_SPECTRUM = 19
    RHK_LINE_GXY = 20
    RHK_LINE_ELECTROCHEMISTRY = 21
    RHK_LINE_DISCRETE_SPECTROSCOPY = 22
    RHK_LINE_DATA_LOGGER = 23
    RHK_LINE_TIME_SPECTROSCOPY = 24
    RHK_LINE_ZOOM_FFT = 25
    RHK_LINE_FREQUENCY_SWEEP = 26
    RHK_LINE_PHASE_ROTATE = 27
    RHK_LINE_FIBER_SWEEP = 28


class RhkImageType(Enum):
    RHK_IMAGE_NORMAL = 0
    RHK_IMAGE_AUTOCORRELATED = 1


class RhkScanType(Enum):
    RHK_SCAN_RIGHT = 0
    RHK_SCAN_LEFT = 1
    RHK_SCAN_UP = 2
    RHK_SCAN_DOWN = 3


class RhkDriftOptionType(Enum):
    RHK_DRIFT_DISABLED = 0
    RHK_DRIFT_EACH_SPECTRA = 1
    RHK_DRIFT_EACH_LOCATION = 2


@dataclass
class Sm4Object:
    obj_type: RhkObjectType
    offset: int
    size: int

    @classmethod
    def from_buffer(cls, cursor: Cursor):
        object_type_id = RhkObjectType(cursor.read_u32_le())
        offset = cursor.read_u32_le()
        size = cursor.read_u32_le()
        return cls(object_type_id, offset, size)


@dataclass
class Sm4Header:
    size: int
    signature: str
    page_count: int
    object_list_count: int
    object_field_size: int
    object_list: List[Sm4Object]

    @classmethod
    def from_buffer(cls, cursor: Cursor) -> Sm4Header:
        size = cursor.read_u16_le()
        signature = cursor.read_string(36)
        page_count = cursor.read_u32_le()
        object_list_count = cursor.read_u32_le()
        object_field_size = cursor.read_u32_le()

        _ = cursor.read_u32_le()
        _ = cursor.read_u32_le()

        object_list = []
        for _ in range(object_list_count):
            object_list.append(Sm4Object.from_buffer(cursor))

        return cls(
            size,
            signature,
            page_count,
            object_list_count,
            object_field_size,
            object_list,
        )


@dataclass
class Sm4PageIndexHeader:
    offset: int
    page_count: int
    object_list_count: int
    object_list: List[Sm4Object]

    @classmethod
    def from_buffer(
        cls, cursor: Cursor, header_object_list: List[Sm4Object]
    ) -> Sm4PageIndexHeader:
        offset = None
        for obj in header_object_list:
            if obj.obj_type == RhkObjectType.RHK_OBJECT_PAGE_INDEX_HEADER:
                offset = obj.offset
                break
        if offset is None:
            raise BufferError("No Page Index Header in Buffer")

        cursor.set_position(offset)
        page_count = cursor.read_u32_le()
        object_list_count = cursor.read_u32_le()
        _reserved_1 = cursor.read_u32_le()  # pyright: ignore
        _reserved_2 = cursor.read_u32_le()  # pyright: ignore

        object_list = []
        for _ in range(object_list_count):
            object_list.append(Sm4Object.from_buffer(cursor))

        return Sm4PageIndexHeader(
            offset, page_count, object_list_count, object_list
        )


@dataclass
class Sm4PageHeaderSequential:
    data_type: int
    data_length: int
    param_count: int
    object_list_count: int
    data_info_size: int
    data_info_string_count: int
    object_list: List[Sm4Object]

    @classmethod
    def from_buffer(cls, cursor: Cursor) -> Sm4PageHeaderSequential:
        data_type = cursor.read_u32_le()
        data_length = cursor.read_u32_le()
        param_count = cursor.read_u32_le()
        object_list_count = cursor.read_u32_le()
        data_info_size = cursor.read_u32_le()
        data_info_string_count = cursor.read_u32_le()

        object_list = []
        object_list.append(Sm4Object.from_buffer(cursor))
        sequential_param_gain: List[float] = []
        sequential_param_label: List[str] = []
        sequential_param_unit: List[str] = []
        for _ in range(param_count):
            sequential_param_gain.append(cursor.read_f32_le())
            sequential_param_label.append(cursor.read_sm4_string())
            sequential_param_unit.append(cursor.read_sm4_string())

        return Sm4PageHeaderSequential(
            data_type,
            data_length,
            param_count,
            object_list_count,
            data_info_size,
            data_info_string_count,
            object_list,
        )


@dataclass
class Sm4PageHeaderDefault:
    string_count: int
    page_type: RhkPageType
    data_sub_source: int
    line_type: RhkLineType
    x_corner: int
    y_corner: int
    x_size: int
    y_size: int
    image_type: RhkImageType
    scan_type: RhkScanType
    group_id: int
    page_data_size: int
    min_z_value: int
    max_z_value: int
    x_scale: float
    y_scale: float
    z_scale: float
    xy_scale: float
    x_offset: float
    y_offset: float
    z_offset: float
    period: float
    bias: float
    current: float
    angle: float
    color_info_count: int
    grid_x_size: int
    grid_y_size: int
    object_list_count: int
    _32_bit_data_flag: int
    object_list: List[Sm4Object]

    @classmethod
    def from_buffer(cls, cursor: Cursor) -> Sm4PageHeaderDefault:
        _ = cursor.read_u16_le()
        string_count = cursor.read_u16_le()
        page_type = RhkPageType(cursor.read_u32_le())
        data_sub_source = cursor.read_u32_le()

        line_type = RhkLineType(cursor.read_u32_le())

        x_corner = cursor.read_u32_le()
        y_corner = cursor.read_u32_le()
        x_size = cursor.read_u32_le()
        y_size = cursor.read_u32_le()

        image_type = RhkImageType(cursor.read_u32_le())

        scan_type = RhkScanType(cursor.read_u32_le())

        group_id = cursor.read_u32_le()
        page_data_size = cursor.read_u32_le()

        min_z_value = cursor.read_u32_le()
        max_z_value = cursor.read_u32_le()

        x_scale = cursor.read_f32_le()
        y_scale = cursor.read_f32_le()
        z_scale = cursor.read_f32_le()
        xy_scale = cursor.read_f32_le()
        x_offset = cursor.read_f32_le()
        y_offset = cursor.read_f32_le()
        z_offset = cursor.read_f32_le()
        period = cursor.read_f32_le()
        bias = cursor.read_f32_le()
        current = cursor.read_f32_le()
        angle = cursor.read_f32_le()

        color_info_count = cursor.read_u32_le()
        grid_x_size = cursor.read_u32_le()
        grid_y_size = cursor.read_u32_le()

        object_list_count = cursor.read_u32_le()
        _32_bit_data_flag = cursor.read_u8_le()

        # reserved
        cursor.skip(63)

        object_list = [Sm4Object.from_buffer(cursor)]

        return Sm4PageHeaderDefault(
            string_count,
            page_type,
            data_sub_source,
            line_type,
            x_corner,
            y_corner,
            x_size,
            y_size,
            image_type,
            scan_type,
            group_id,
            page_data_size,
            min_z_value,
            max_z_value,
            x_scale,
            y_scale,
            z_scale,
            xy_scale,
            x_offset,
            y_offset,
            z_offset,
            period,
            bias,
            current,
            angle,
            color_info_count,
            grid_x_size,
            grid_y_size,
            object_list_count,
            _32_bit_data_flag,
            object_list,
        )


Sm4PageHeader: TypeAlias = Union[Sm4PageHeaderSequential, Sm4PageHeaderDefault]


@dataclass
class Sm4Page:
    header: Sm4PageHeader = field(init=False)
    data: PageData = field(init=False)
    page_id: int
    page_data_type: RhkPageDataType
    page_source_type: RhkPageSourceType
    object_list_count: int
    minor_version: int
    object_list: List[Sm4Object]
    additional_page_objects: List[PageObject] = field(default_factory=list)

    @classmethod
    def from_buffer(cls, cursor: Cursor) -> Sm4Page:
        page_id = cursor.read_u16_le()
        cursor.skip(14)
        page_data_type = RhkPageDataType(cursor.read_u32_le())
        page_source_type = RhkPageSourceType(cursor.read_u32_le())
        object_list_count = cursor.read_u32_le()
        minor_version = cursor.read_u32_le()

        object_list = []
        for _ in range(object_list_count):
            object_list.append(Sm4Object.from_buffer(cursor))

        return cls(
            page_id,
            page_data_type,
            page_source_type,
            minor_version,
            object_list_count,
            object_list,
        )

    def add_header(self, header: Sm4PageHeader) -> None:
        self.header = header

    def read_data(self, cursor: Cursor) -> None:
        tiptrack_info_count = None
        for obj in self.object_list:
            if (
                obj.offset != 0
                and obj.size != 0
                and isinstance(self.header, Sm4PageHeaderDefault)
            ):
                cursor.set_position(obj.offset)

                if obj.obj_type == RhkObjectType.RHK_OBJECT_PAGE_DATA:
                    self.data = PageData.from_buffer(
                        cursor,
                        obj.size,
                        self.header.z_scale,
                        self.header.z_offset,
                    )

                elif (
                    obj.obj_type == RhkObjectType.RHK_OBJECT_IMAGE_DRIFT_HEADER
                ):
                    self.additional_page_objects.append(
                        ImageDriftHeader.from_buffer(cursor)
                    )

                elif obj.obj_type == RhkObjectType.RHK_OBJECT_IMAGE_DRIFT:
                    self.additional_page_objects.append(
                        ImageDriftData.from_buffer(cursor)
                    )

                elif (
                    obj.obj_type == RhkObjectType.RHK_OBJECT_SPEC_DRIFT_HEADER
                ):
                    self.additional_page_objects.append(
                        SpecDriftHeader.from_buffer(cursor)
                    )

                elif obj.obj_type == RhkObjectType.RHK_OBJECT_SPEC_DRIFT_DATA:
                    self.additional_page_objects.append(
                        SpecDriftData.from_buffer(cursor, self.header.y_size)
                    )

                elif obj.obj_type == RhkObjectType.RHK_OBJECT_COLOR_INFO:
                    pass

                elif obj.obj_type == RhkObjectType.RHK_OBJECT_STRING_DATA:
                    self.additional_page_objects.append(
                        StringData.from_buffer(
                            cursor, self.header.string_count
                        )
                    )

                elif obj.obj_type == RhkObjectType.RHK_OBJECT_TIP_TRACK_HEADER:
                    read_obj = TipTrackHeader.from_buffer(cursor)
                    tiptrack_info_count = read_obj.tiptrack_tiptrack_info_count
                    self.additional_page_objects.append(read_obj)

                elif obj.obj_type == RhkObjectType.RHK_OBJECT_TIP_TRACK_HEADER:
                    if tiptrack_info_count is not None:
                        self.additional_page_objects.append(
                            TipTrackData.from_buffer(
                                cursor, tiptrack_info_count
                            )
                        )
                    else:
                        raise ValueError("tiptrack_info_count not found")

                elif obj.obj_type == RhkObjectType.RHK_OBJECT_PRM:
                    pass

                elif obj.obj_type == RhkObjectType.RHK_OBJECT_THUMBNAIL:
                    pass

                elif obj.obj_type == RhkObjectType.RHK_OBJECT_PRM_HEADER:
                    prm_data_offset = None
                    for i in self.header.object_list:
                        if i.obj_type == RhkObjectType.RHK_OBJECT_PRM:
                            prm_data_offset = i.offset
                            self.additional_page_objects.append(
                                PrmHeader.from_buffer(cursor, prm_data_offset)
                            )
                            break

                elif obj.obj_type == RhkObjectType.RHK_OBJECT_THUMBNAIL_HEADER:
                    pass

                elif obj.obj_type == RhkObjectType.RHK_OBJECT_API_INFO:
                    self.additional_page_objects.append(
                        ApiInfo.from_buffer(cursor)
                    )

                elif obj.obj_type == RhkObjectType.RHK_OBJECT_HISTORY_INFO:
                    pass

                elif (
                    obj.obj_type == RhkObjectType.RHK_OBJECT_PIEZO_SENSITIVITY
                ):
                    self.additional_page_objects.append(
                        PiezoSensitivity.from_buffer(cursor)
                    )

                elif (
                    obj.obj_type
                    == RhkObjectType.RHK_OBJECT_FREQUENCY_SWEEP_DATA
                ):
                    self.additional_page_objects.append(
                        FrequencySweepData.from_buffer(cursor)
                    )

                elif (
                    obj.obj_type
                    == RhkObjectType.RHK_OBJECT_SCAN_PROCESSOR_INFO
                ):
                    self.additional_page_objects.append(
                        ScanProcessorInfo.from_buffer(cursor)
                    )

                elif obj.obj_type == RhkObjectType.RHK_OBJECT_PLL_INFO:
                    self.additional_page_objects.append(
                        PllInfo.from_buffer(cursor)
                    )

                elif obj.obj_type == RhkObjectType.RHK_OBJECT_CH1_DRIVE_INFO:
                    self.additional_page_objects.append(
                        ChannelDriveInfo.from_buffer(cursor)
                    )

                elif obj.obj_type == RhkObjectType.RHK_OBJECT_CH2_DRIVE_INFO:
                    self.additional_page_objects.append(
                        ChannelDriveInfo.from_buffer(cursor)
                    )

                elif obj.obj_type == RhkObjectType.RHK_OBJECT_LOCKIN0_INFO:
                    self.additional_page_objects.append(
                        LockinInfo.from_buffer(cursor)
                    )

                elif obj.obj_type == RhkObjectType.RHK_OBJECT_LOCKIN1_INFO:
                    self.additional_page_objects.append(
                        LockinInfo.from_buffer(cursor)
                    )

                elif obj.obj_type == RhkObjectType.RHK_OBJECT_ZPI_INFO:
                    self.additional_page_objects.append(
                        PiControllerInfo.from_buffer(cursor)
                    )

                elif obj.obj_type == RhkObjectType.RHK_OBJECT_KPI_INFO:
                    self.additional_page_objects.append(
                        PiControllerInfo.from_buffer(cursor)
                    )

                elif obj.obj_type == RhkObjectType.RHK_OBJECT_AUX_PI_INFO:
                    self.additional_page_objects.append(
                        PiControllerInfo.from_buffer(cursor)
                    )

                elif (
                    obj.obj_type
                    == RhkObjectType.RHK_OBJECT_LOWPASS_FILTER0_INFO
                ):
                    self.additional_page_objects.append(
                        LowpassFilterInfo.from_buffer(cursor)
                    )

                elif (
                    obj.obj_type
                    == RhkObjectType.RHK_OBJECT_LOWPASS_FILTER1_INFO
                ):
                    self.additional_page_objects.append(
                        LowpassFilterInfo.from_buffer(cursor)
                    )


class Sm4File:
    def __init__(self, filepath: str):
        self.filepath = filepath
        with open(filepath, "rb") as f:
            self._read_sm4_file(f)

    def _read_sm4_file(self, f: BufferedReader):
        cursor = Cursor(f)
        header = Sm4Header.from_buffer(cursor)

        page_index_header = Sm4PageIndexHeader.from_buffer(
            cursor, header.object_list
        )

        page_index_array_offset = None
        for obj in page_index_header.object_list:
            if obj.obj_type == RhkObjectType.RHK_OBJECT_PAGE_INDEX_ARRAY:
                page_index_array_offset = obj.offset
                break
        if page_index_array_offset is None:
            raise BufferError("No page index array in buffer")
        cursor.set_position(page_index_array_offset)

        self.pages: List[Sm4Page] = []
        for _ in range(page_index_header.page_count):
            page = Sm4Page.from_buffer(cursor)
            self.pages.append(page)

        offset = None
        for page in self.pages:
            for obj in page.object_list:
                if obj.obj_type == RhkObjectType.RHK_OBJECT_PAGE_HEADER:
                    offset = obj.offset
                    break
            if offset is None:
                raise BufferError(f"No page header in page")
            cursor.set_position(offset)

            if page.page_data_type == RhkPageDataType.RHK_DATA_SEQUENTIAL:
                page_header: Sm4PageHeader = (
                    Sm4PageHeaderSequential.from_buffer(cursor)
                )

            else:
                page_header = Sm4PageHeaderDefault.from_buffer(cursor)

            page.add_header(page_header)
            page.read_data(cursor)
