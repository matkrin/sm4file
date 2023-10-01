from __future__ import annotations
from typing import TYPE_CHECKING, List
from dataclasses import dataclass

from cursor import Cursor

if TYPE_CHECKING:
    from sm4file.sm4file import RhkDriftOptionType


@dataclass
class ImageDriftHeader:
    imagedrift_filetime: int
    imagedrift_drift_option_type: RhkDriftOptionType

    @classmethod
    def from_buffer(cls, cursor: Cursor, offset: int) -> ImageDriftHeader:
        cursor.set_position(offset)

        imagedrift_filetime = cursor.read_u64_le()
        imagedrift_drift_option_type = RhkDriftOptionType(cursor.read_u32_le())
        return cls(imagedrift_filetime, imagedrift_drift_option_type)


@dataclass
class ImageDriftData:
    imagedrift_time: int
    imagedrift_dx: int
    imagedrift_dy: int
    imagedrift_cumulative_x: int
    imagedrift_cumulative_y: int
    imagedrift_vector_x: int
    imagedrift_vector_y: int

    @classmethod
    def from_buffer(cls, cursor: Cursor, offset: int) -> ImageDriftData:
        cursor.set_position(offset)

        imagedrift_time = cursor.read_u32_le()
        imagedrift_dx = cursor.read_u32_le()
        imagedrift_dy = cursor.read_u32_le()
        imagedrift_cumulative_x = cursor.read_u32_le()
        imagedrift_cumulative_y = cursor.read_u32_le()
        imagedrift_vector_x = cursor.read_u32_le()
        imagedrift_vector_y = cursor.read_u32_le()
        return cls(
            imagedrift_time,
            imagedrift_dx,
            imagedrift_dy,
            imagedrift_cumulative_x,
            imagedrift_cumulative_y,
            imagedrift_vector_x,
            imagedrift_vector_y,
        )


@dataclass
class SpecDriftHeader:
    specdrift_filetime: int
    specdrift_drift_option_type: int
    specdrift_drift_option_type_name: str
    specdrift_channel: str

    @classmethod
    def from_buffer(cls, cursor: Cursor, offset: int) -> SpecDriftHeader:
        cursor.set_position(offset)
        # unix epoch
        specdrift_filetime = cursor.read_u64_le()
        specdrift_drift_option_type = cursor.read_u32_le()
        if specdrift_drift_option_type == 0:
            specdrift_drift_option_type_name = "RHK_DRIFT_DISABLED"
        elif specdrift_drift_option_type == 1:
            specdrift_drift_option_type_name = "RHK_DRIFT_EACH_SPECTRA"
        elif specdrift_drift_option_type == 1:
            specdrift_drift_option_type_name = "RHK_DRIFT_EACH_LOCATION"
        else:
            specdrift_drift_option_type_name = "RHK_DRIFT_UNKNOWN"

        _ = cursor.read_u32_le()
        specdrift_channel = cursor.read_sm4_string()

        return cls(
            specdrift_filetime,
            specdrift_drift_option_type,
            specdrift_drift_option_type_name,
            specdrift_channel,
        )


@dataclass
class SpecDriftData:
    specdrift_time: List[float]
    specdrift_x_coord: List[float]
    specdrift_y_coord: List[float]
    specdrift_dx: List[float]
    specdrift_dy: List[float]
    specdrift_cumulative_x: List[float]
    specdrift_cumulative_y: List[float]

    @classmethod
    def from_buffer(
        cls, cursor: Cursor, offset: int, y_size: int
    ) -> SpecDriftData:
        cursor.set_position(offset)

        specdrift_time = []
        specdrift_x_coord = []
        specdrift_y_coord = []
        specdrift_dx = []
        specdrift_dy = []
        specdrift_cumulative_x = []
        specdrift_cumulative_y = []

        for _ in range(y_size):
            specdrift_time.append(cursor.read_f32_le())
            specdrift_x_coord.append(cursor.read_f32_le())
            specdrift_y_coord.append(cursor.read_f32_le())
            specdrift_dx.append(cursor.read_f32_le())
            specdrift_dy.append(cursor.read_f32_le())
            specdrift_cumulative_x.append(cursor.read_f32_le())
            specdrift_cumulative_y.append(cursor.read_f32_le())

        return cls(
            specdrift_time,
            specdrift_x_coord,
            specdrift_y_coord,
            specdrift_dx,
            specdrift_dy,
            specdrift_cumulative_x,
            specdrift_cumulative_y,
        )


@dataclass
class StringData:
    label: str
    system_text: str
    session_text: str
    user_text: str
    filename: str
    date: str
    time: str
    x_units: str
    y_units: str
    z_units: str
    x_label: str
    y_label: str
    status_channel_text: str
    completed_line_count: str
    oversampling_count: str
    sliced_voltage: str
    pll_pro_status: str
    setpoint_unit: str
    channel_list: str

    @classmethod
    def from_buffer(
        cls, cursor: Cursor, offset: int, count: int
    ) -> StringData:
        cursor.set_position(offset)

        label = cursor.read_sm4_string()
        system_text = cursor.read_sm4_string()
        session_text = cursor.read_sm4_string()
        user_text = cursor.read_sm4_string()
        filename = cursor.read_sm4_string()
        date = cursor.read_sm4_string()
        time = cursor.read_sm4_string()
        x_units = cursor.read_sm4_string()
        y_units = cursor.read_sm4_string()
        z_units = cursor.read_sm4_string()
        x_label = cursor.read_sm4_string()
        y_label = cursor.read_sm4_string()
        status_channel_text = cursor.read_sm4_string()
        completed_line_count = cursor.read_sm4_string()
        oversampling_count = cursor.read_sm4_string()
        sliced_voltage = cursor.read_sm4_string()
        pll_pro_status = cursor.read_sm4_string()
        setpoint_unit = cursor.read_sm4_string()
        channel_list = cursor.read_sm4_string()

        return cls(
            label,
            system_text,
            session_text,
            user_text,
            filename,
            date,
            time,
            x_units,
            y_units,
            z_units,
            x_label,
            y_label,
            status_channel_text,
            completed_line_count,
            oversampling_count,
            sliced_voltage,
            pll_pro_status,
            setpoint_unit,
            channel_list,
        )


@dataclass
class TipTrackHeader:
    tiptrack_filetime: int
    tiptrack_feature_height: float
    tiptrack_feature_width: float
    tiptrack_time_constant: float
    tiptrack_cycle_rate: float
    tiptrack_phase_lag: float
    tiptrack_tiptrack_info_count: int
    tiptrack_channel: str

    @classmethod
    def from_buffer(cls, cursor: Cursor, offset: int) -> TipTrackHeader:
        cursor.set_position(offset)
        # unix epoch
        tiptrack_filetime = cursor.read_u64_le()
        tiptrack_feature_height = cursor.read_f32_le()
        tiptrack_feature_width = cursor.read_f32_le()
        tiptrack_time_constant = cursor.read_f32_le()
        tiptrack_cycle_rate = cursor.read_f32_le()
        tiptrack_phase_lag = cursor.read_f32_le()
        _ = cursor.read_u32_le()
        tiptrack_tiptrack_info_count = cursor.read_u32_le()
        tiptrack_channel = cursor.read_sm4_string()

        return cls(
            tiptrack_filetime,
            tiptrack_feature_height,
            tiptrack_feature_width,
            tiptrack_time_constant,
            tiptrack_cycle_rate,
            tiptrack_phase_lag,
            tiptrack_tiptrack_info_count,
            tiptrack_channel,
        )


@dataclass
class TipTrackData:
    tiptrack_cumulative_time: List[float]
    tiptrack_time: List[float]
    tiptrack_dx: List[float]
    tiptrack_dy: List[float]

    @classmethod
    def from_buffer(
        cls, cursor: Cursor, offest: int, tiptrack_tiptrack_info_count: int
    ) -> TipTrackData:
        tiptrack_cumulative_time = []
        tiptrack_time = []
        tiptrack_dx = []
        tiptrack_dy = []

        for _ in range(tiptrack_tiptrack_info_count):
            tiptrack_cumulative_time.append(cursor.read_f32_le())
            tiptrack_time.append(cursor.read_f32_le())
            tiptrack_dx.append(cursor.read_f32_le())
            tiptrack_dy.append(cursor.read_f32_le())

        return cls(
            tiptrack_cumulative_time,
            tiptrack_time,
            tiptrack_dx,
            tiptrack_dy,
        )


@dataclass
class Prm:
    

    @classmethod
    def from_buffer(cls, cursor: Cursor, offset: int) -> Prm:
        return cls()



@dataclass
class PrmHeader:
    prm_compression_flag: int
    prm_data_size: int
    prm_compression_size: int
    prm_data: List[int]
    

    @classmethod
    def from_buffer(cls, cursor: Cursor, offset: int, prm_data_offset: int) -> PrmHeader:
        cursor.set_position(offset)

        prm_compression_flag = cursor.read_u32_le()
        prm_data_size = cursor.read_u32_le()
        prm_compression_size = cursor.read_u32_le()

        prm_data = []
        if prm_compression_flag == 0:
            for _ in range(prm_data_size):
                prm_data.append(cursor.read_u32_le())
        else:


       
        
        



@dataclass
class ApiInfo
    

    @classmethod
    def from_buffer(cls, cursor: Cursor, offset: int) -> ApiInfo:



@dataclass
class HistoryInfo
    

    @classmethod
    def from_buffer(cls, cursor: Cursor, offset: int) -> HistoryInfo:



@dataclass
class PiezoSensitivity
    

    @classmethod
    def from_buffer(cls, cursor: Cursor, offset: int) -> PiezoSensitivity:



@dataclass
class FrequencySweepData:
    

    @classmethod
    def from_buffer(cls, cursor: Cursor, offset: int) -> FrequencySweepData:



@dataclass
class ScanProcessorInfo
    

    @classmethod
    def from_buffer(cls, cursor: Cursor, offset: int) -> ScanProcessorInfo



@dataclass
class PllInfo
    

    @classmethod
    def from_buffer(cls, cursor: Cursor, offset: int) -> PllInfo



@dataclass
class Ch1DriveInfo:
    

    @classmethod
    def from_buffer(cls, cursor: Cursor, offset: int) -> Ch1DriveInfo:



@dataclass
class Ch2DriveInfo:
    

    @classmethod
    def from_buffer(cls, cursor: Cursor, offset: int) -> Ch2DriveInfo:



@dataclass
class Lockin0Info:
    

    @classmethod
    def from_buffer(cls, cursor: Cursor, offset: int) -> Lockin0Info:



@dataclass
class Lockin1Info:
    

    @classmethod
    def from_buffer(cls, cursor: Cursor, offset: int) -> Lockin1Info:



@dataclass
class ZpiInfo:
    

    @classmethod
    def from_buffer(cls, cursor: Cursor, offset: int) -> ZpiInfo:



@dataclass
class KpiInfo:
    

    @classmethod
    def from_buffer(cls, cursor:Cursor, offset: int) ->  KpiInfo:



@dataclass
class AuxPiInfo:
    

    @classmethod
    def from_buffer(cls, cursor:Cursor, offset: int) ->  AuxPiInfo:



@dataclass
class LowpassFilterR0Info:
    

    @classmethod
    def from_buffer(cls, cursor:Cursor, offset: int) ->  LowpassFilterR0Info:



@dataclass
class LowpassFilterR1Info:
    

    @classmethod
    def from_buffer(cls, cursor:Cursor, offset: int) ->  LowpassFilterR1Info:


