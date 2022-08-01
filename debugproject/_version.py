def _get_version() -> str:
    from pathlib import Path

    import versioningit


    prioject_path = Path(__file__).parent.parent
    return versioningit.get_version(project_dir=prioject_path)


__version__ = _get_version()
