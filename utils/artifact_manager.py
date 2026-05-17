from __future__ import annotations
import re
import uuid
from datetime import datetime
from pathlib import Path
from typing import Optional


REPORT_DIR = (
    Path(__file__)
    .resolve()
    .parent.parent
    / "reports"
)


class ArtifactManager:

    def __init__(
        self,
        report_dir: Optional[Path] = None
    ) -> None:

        self.report_dir = (
            report_dir
            if report_dir
            else REPORT_DIR
        )

    @staticmethod
    def sanitize_filename(
        value: str
    ) -> str:

        value = re.sub(
            r"[^\w\-_.]",
            "_",
            value
        )

        return value.strip("_")

    @staticmethod
    def generate_timestamp() -> str:

        return datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

    @staticmethod
    def generate_uuid(
        length: int = 8
    ) -> str:

        return uuid.uuid4().hex[:length]

    def generate_path(
        self,
        folder: str,
        prefix: str,
        extension: str
    ) -> str:

        artifact_dir = (
            self.report_dir
            / folder
        )

        artifact_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        timestamp = self.generate_timestamp()

        filename = (
            f"{prefix}_{timestamp}.{extension}"
        )

        return str(
            artifact_dir / filename
        )

    def screenshot_path(
        self,
        test_name: str
    ) -> str:

        return self.generate_path(
            folder="screenshots",
            prefix=test_name,
            extension="png"
        )

    def log_path(
        self,
        log_name: str = "test"
    ) -> str:

        return self.generate_path(
            folder="logs",
            prefix=log_name,
            extension="log"
        )


artifact_manager = ArtifactManager()