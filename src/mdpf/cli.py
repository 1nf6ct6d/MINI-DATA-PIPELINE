from __future__ import annotations

from .pipeline.runner import PipelineRunner


def main() -> None:
    runner = PipelineRunner("config.json")
    code = runner.run()
    raise SystemExit(code)