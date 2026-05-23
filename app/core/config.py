from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Nama Aplikasi
    PROJECT_NAME: str = "GymAI Persona"
    
    # API Key Google Gemini
    GEMINI_API_KEY: str
    
    # Konfigurasi Pydantic untuk membaca file .env
    model_config = SettingsConfigDict(env_file=".env")

# Inisialisasi object settings
settings = Settings()