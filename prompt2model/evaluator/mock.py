"""A dummy evaluator for testing purposes."""
from __future__ import annotations  # noqa FI58

from typing import Any

import datasets

from prompt2model.evaluator.base import Evaluator
from prompt2model.model_executor import ModelOutput
from prompt2model.prompt_parser import PromptSpec


class MockEvaluator(Evaluator):
    """A dummy evaluator that always returns the same metric value."""

    def __init__(self) -> None:
        """Initialize the evaluation setting."""

    def evaluate_model(
        self,
        dataset: datasets.Dataset,
        gt_column: str,
        predictions: list[ModelOutput],
        metrics: list[datasets.Metric] | None = None,
        prompt_spec: PromptSpec | None = None,
    ) -> dict[str, Any]:
        """Return empty metrics dictionary.

        Args:
            dataset: The dataset to evaluate metrics on.
            gt_column: The dataset column to use as ground truth.
            predictions: Corresponding model outputs to evaluate.
            metrics: (Optional) The metrics to use.
            prompt_spec: (Optional) A PromptSpec to infer the metrics from.

        Returns:
            An empty dictionary (for testing purposes).
        """
        return {}