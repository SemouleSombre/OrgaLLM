import logging

from dotenv import load_dotenv
from pydantic import HttpUrl, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal, Optional
from pathlib import Path

logger = logging.getLogger(__name__)

class Settings(BaseSettings):
    """Application configuration with validation"""
    # Application Settings
    DEBUG: bool = True
    LOG_LEVEL: str = "DEBUG"
    
# Global configuration instance
def load_settings() -> Settings:
    return Settings() # pyright: ignore[reportCallIssue]

try:
    settings = load_settings()
    logger.info("Configuration chargée avec succès !")
except Exception as e:
    raise RuntimeError(f"Erreur lors du chargement de la configuration : {e}")

def get_setting() -> Settings:
    """Get the global configuration instance"""
    return settings

def get_config() -> Settings:
    """Get the global configuration instance (alias for get_setting)"""
    return settings