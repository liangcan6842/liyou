from lib.read_files_tools.yaml_control import GetYamlData
from common.setting import ensure_path_sep
from lib.other_tools.models import Config


_data = GetYamlData(ensure_path_sep("\\common\\config.yml")).get_yaml_data()
config = Config(**_data)

