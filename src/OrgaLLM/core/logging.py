"""Logging configuration for the application"""

import logging
import sys
from core.config import get_setting

def setup_logging() -> None:
    """Setup application logging"""
    config = get_setting()
    level = getattr(logging, config.LOG_LEVEL.upper(), logging.DEBUG)
    
    # Configure root logger
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout)
        ],
        force=True,
    )