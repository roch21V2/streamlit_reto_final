import os

from dotenv import load_dotenv

load_dotenv()

DATASET_OCUPACIONES_LIMPIA = "./data/ia_ocupaciones_gigante_limpia.csv"
DATASET_TS_BY_EMPRESA = "./data/ocupaciones_time_series_by_empresa.xlsx"
DATASET_TS_BY_ENTIDAD = "./data/ocupaciones_time_series_by_entidad.xlsx"
DATASET_TS_BY_ROOM_TYPE = "./data/reservaciones_time_series_by_room_type.xlsx"
DATASET_OCUPACIONES_N = "./data/ocupaciones_time_seriesN.xlsx"

BACKEND_BASE_URL = os.getenv("BACKEND_BASE_URL")

TABLE_NAMES = [
    "ia_ocupaciones_gigante_limpia2",
    "ocupaciones_time_series_by_empresa",
    "ocupaciones_time_series_by_entidad",
    "reservaciones_time_series_by_room_type",
]


VIEWS_NAMES = [
    "ocupaciones_time_series_by_entidad_con_nombre",
    "ocupaciones_con_nombre",
]
