from app.core.config import get_settings


def test_settings_load():
    settings = get_settings()
    assert settings.APP_ENV in ("development", "staging", "production")


def test_app_name_is_set():
    settings = get_settings()
    assert settings.APP_NAME is not None
    assert len(settings.APP_NAME) > 0
