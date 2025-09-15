
from ..config import AppConfig
from ..utils.io import ensure_dirs

class CreditnoteDoctorAgent:
    def __init__(self, cfg: AppConfig):
        self.cfg = cfg
        ensure_dirs(cfg)
